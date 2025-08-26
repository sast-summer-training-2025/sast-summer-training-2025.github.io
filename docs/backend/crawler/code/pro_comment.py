"""
网易云音乐歌单评论爬虫
功能：爬取指定歌单的所有评论数据，包括热门评论和普通评论
特点：支持参数加密、分页获取、多种排序方式、数据格式化
技术：AES+RSA双重加密，模拟网易云官方API调用
作者：Tempest
创建时间：2025
"""

import requests
import json
import time
import base64
import binascii
import os
from datetime import datetime
from Crypto.Cipher import AES
import random
import string

class NeteaseCommentCrawler:
    """网易云音乐评论爬虫类"""
    
    def __init__(self):
        """初始化爬虫，配置加密参数"""
        self.session = requests.Session()
        
        # 配置请求头，模拟网易云官方客户端
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://music.163.com/',
            'Origin': 'https://music.163.com',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.session.headers.update(self.headers)
        
        # 网易云API加密常量（从官方JS逆向获取）
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'  # AES加密初始密钥
        self.pub_key = '010001'            # RSA公钥指数
        self.iv = b'0102030405060708'       # AES加密初始向量
        
    # ==================== Cookie管理 ====================
        
    def load_cookies_from_json(self, cookie_file="cookies.json"):
        """
        从JSON文件加载Cookie
        
        Args:
            cookie_file (str): Cookie文件路径
            
        Returns:
            bool: 加载成功返回True，失败返回False
        """
        try:
            with open(cookie_file, 'r', encoding='utf-8') as f:
                cookies_dict = json.load(f)
            
            for name, value in cookies_dict.items():
                self.session.cookies.set(name, value, domain='.music.163.com')
            
            print(f"成功加载{len(cookies_dict)}个Cookie")
            return True
        except Exception as e:
            print(f"加载Cookie失败: {e}")
            return False
    
    # ==================== 加密算法实现 ====================
    
    def _pad_data(self, data):
        """
        PKCS7填充算法
        
        Args:
            data (str): 待填充的数据
            
        Returns:
            str: 填充后的数据
        """
        pad_len = 16 - len(data) % 16
        return data + chr(pad_len) * pad_len
    
    def _aes_encrypt(self, text, key):
        """
        AES加密实现
        
        Args:
            text (str): 待加密文本
            key (str): 加密密钥
            
        Returns:
            str: Base64编码的加密结果
        """
        text = self._pad_data(text)
        cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, self.iv)
        encrypted = cipher.encrypt(text.encode('utf8'))
        return base64.b64encode(encrypted).decode('utf8')
    
    def _rsa_encrypt(self, text, pub_key, modulus):
        """
        RSA加密实现
        
        Args:
            text (str): 待加密文本
            pub_key (str): RSA公钥指数
            modulus (str): RSA模数
            
        Returns:
            str: 十六进制加密结果
        """
        text = text[::-1]  # 字符串反转
        rs = pow(int(binascii.hexlify(text.encode('utf8')), 16), int(pub_key, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)
    
    def _create_secret_key(self, size=16):
        """
        生成随机AES密钥
        
        Args:
            size (int): 密钥长度
            
        Returns:
            str: 随机密钥字符串
        """
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(size))
    
    def _encrypt_params(self, params_dict):
        """
        网易云API参数加密（AES+RSA双重加密）
        
        Args:
            params_dict (dict): 待加密的参数字典
            
        Returns:
            dict: 包含加密参数的字典
        """
        # 转换参数为JSON字符串
        params_json = json.dumps(params_dict, separators=(',', ':'))
        
        # 生成随机AES密钥
        secret_key = self._create_secret_key(16)
        
        # 第一次AES加密（使用固定密钥）
        enc_text = self._aes_encrypt(params_json, self.nonce)
        # 第二次AES加密（使用随机密钥）
        enc_text = self._aes_encrypt(enc_text, secret_key)
        
        # RSA加密随机密钥
        enc_sec_key = self._rsa_encrypt(secret_key, self.pub_key, self.modulus)
        
        return {
            'params': enc_text,
            'encSecKey': enc_sec_key
        }
    
    # ==================== 评论获取核心方法 ====================
    
    def get_comments(self, resource_id, resource_type='A_PL_0_', limit=20, cursor="-1", sort_type=3):
        """
        获取单页评论数据（支持cursor分页）
        
        Args:
            resource_id (str): 资源ID（歌单ID）
            resource_type (str): 资源类型（A_PL_0_表示歌单）
            limit (int): 每页评论数量（最大100）
            cursor (str): 分页游标，首次请求使用"-1"
            sort_type (int): 排序类型（1:推荐, 2:最热, 3:最新）
            
        Returns:
            dict: 包含评论数据的字典，失败时返回None
        """
        try:
            url = "https://music.163.com/weapi/comment/resource/comments/get"
            
            # 获取CSRF令牌（防跨站请求伪造）
            csrf_token = self.session.cookies.get('__csrf', '')
            
            # 构建API请求参数（基于网易云官方接口分析）
            params_dict = {
                'csrf_token': csrf_token,
                'cursor': str(cursor),      # 游标分页标识
                'offset': "0",              # 偏移量（使用cursor分页时固定为0）
                'orderType': sort_type,     # 排序类型
                'pageNo': "1",              # 页码（使用cursor分页时固定为1）
                'pageSize': str(limit),     # 每页大小
                'rid': f"{resource_type}{resource_id}",      # 资源标识
                'threadId': f"{resource_type}{resource_id}"  # 线程标识
            }
            
            # 使用网易云加密算法加密参数
            encrypted_data = self._encrypt_params(params_dict)
            encrypted_data['csrf_token'] = csrf_token
            
            print(f"正在获取歌单 {resource_id} 的评论 (cursor:{cursor}, 排序:{sort_type})...")
            
            response = self.session.post(url, data=encrypted_data, timeout=15)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 200:
                    data = result.get('data', {})
                    
                    # 解析返回数据
                    comments_count = len(data.get('comments', []))
                    hot_comments_count = len(data.get('hotComments', [])) if data.get('hotComments') else 0
                    total_count = data.get('totalCount', 0)
                    has_more = data.get('hasMore', False)
                    next_cursor = data.get('cursor', '')
                    
                    print(f"  API返回: 普通评论{comments_count}条, 热门评论{hot_comments_count}条, 总数{total_count}, 还有更多:{has_more}, 下一页cursor:{next_cursor}")
                    
                    return {
                        'comments': data.get('comments', []),
                        'hotComments': data.get('hotComments', []),
                        'total': total_count,
                        'hasMore': has_more,
                        'cursor': next_cursor,
                        'sortType': data.get('sortType', sort_type)
                    }
                else:
                    print(f"✗ API返回错误: {result.get('message', '未知错误')} (code: {result.get('code')})")
            else:
                print(f"✗ HTTP错误: {response.status_code}")
                print(f"响应内容: {response.text[:200]}...")
                
        except Exception as e:
            print(f"✗ 获取评论失败: {e}")
        
        return None
    
    def get_all_comments(self, playlist_id, max_pages=10, delay=1, sort_type=3):
        """
        获取歌单的所有评论（自动分页获取）
        
        Args:
            playlist_id (str): 歌单ID
            max_pages (int): 最大爬取页数
            delay (int): 请求间隔（秒）
            sort_type (int): 排序类型（1:推荐, 2:最热, 3:最新）
            
        Returns:
            dict: 包含所有评论数据的字典
        """
        all_comments = []
        hot_comments = []
        limit = 100  # 每页最大100条评论
        cursor = "-1"  # 首次请求使用特殊游标值
        
        print(f"\n=== 开始获取歌单 {playlist_id} 的所有评论 (排序类型: {sort_type}) ===")
        
        for page in range(max_pages):
            result = self.get_comments(playlist_id, 'A_PL_0_', limit, cursor, sort_type)
            
            if not result:
                print(f"第{page + 1}页获取失败，停止获取")
                break
            
            # 第一页获取热门评论
            if page == 0 and result.get('hotComments'):
                hot_comments = result['hotComments']
                print(f"获取到 {len(hot_comments)} 条热门评论")
            
            comments = result.get('comments', [])
            
            if not comments:
                if page == 0:
                    print("第一页无普通评论，可能只有热门评论")
                    # 检查API是否确认无更多数据
                    if not result.get('hasMore', False):
                        print("API确认无更多评论")
                        break
                else:
                    print(f"第{page + 1}页没有评论，停止获取")
                    break
            else:
                all_comments.extend(comments)
                print(f"第{page + 1}页获取到 {len(comments)} 条评论，累计 {len(all_comments)} 条")
            
            # 检查分页状态
            has_more = result.get('hasMore', False)
            next_cursor = result.get('cursor', '')
            
            if not has_more:
                print("API返回hasMore=False，已获取所有评论")
                break
            
            if not next_cursor or next_cursor == cursor:
                print("游标无变化，停止获取避免无限循环")
                break
            
            # 更新游标用于下一页请求
            cursor = next_cursor
            
            # 延迟避免触发反爬虫机制
            if page < max_pages - 1:
                time.sleep(delay)
        
        return {
            'comments': all_comments,
            'hotComments': hot_comments,
            'total': len(all_comments),
            'actualSortType': sort_type
        }
    
    # ==================== 数据处理方法 ====================
    
    def format_comments(self, comments_data):
        """
        格式化评论数据，统一数据结构
        
        Args:
            comments_data (dict): 原始评论数据
            
        Returns:
            dict: 格式化后的评论数据
        """
        if not comments_data:
            return {'comments': [], 'hotComments': []}
        
        def format_comment_list(comments):
            """格式化评论列表"""
            formatted = []
            for comment in comments:
                try:
                    # 数据有效性检查
                    if not isinstance(comment, dict):
                        continue
                    
                    # 检查必要字段
                    if not comment.get('commentId') or not comment.get('content'):
                        continue
                    
                    # 安全处理回复评论
                    replied = []
                    be_replied = comment.get('beReplied')
                    if be_replied and isinstance(be_replied, list):
                        for reply in be_replied:
                            if reply and isinstance(reply, dict) and reply.get('content'):
                                replied.append({
                                    'commentId': reply.get('beRepliedCommentId', ''),
                                    'content': reply.get('content', ''),
                                    'user': reply.get('user', {}).get('nickname', '') if reply.get('user') else '',
                                    'userId': reply.get('user', {}).get('userId', '') if reply.get('user') else ''
                                })
                    
                    # 安全处理IP位置信息
                    ip_location = comment.get('ipLocation', {})
                    location = ''
                    if isinstance(ip_location, dict):
                        location = ip_location.get('location', '')
                    
                    # 安全处理用户信息
                    user_info = comment.get('user', {})
                    if not isinstance(user_info, dict):
                        user_info = {}
                    
                    # 安全处理时间戳
                    timestamp = comment.get('time', 0)
                    formatted_time = ''
                    if timestamp and isinstance(timestamp, (int, float)) and timestamp > 0:
                        try:
                            formatted_time = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
                        except (ValueError, OSError):
                            formatted_time = str(timestamp)
                    
                    # 构建格式化的评论对象
                    formatted_comment = {
                        'commentId': comment.get('commentId', ''),
                        'content': comment.get('content', ''),
                        'time': formatted_time,
                        'timeStamp': timestamp,
                        'likedCount': comment.get('likedCount', 0),
                        'replyCount': comment.get('replyCount', 0),
                        'user': {
                            'userId': user_info.get('userId', ''),
                            'nickname': user_info.get('nickname', ''),
                            'avatarUrl': user_info.get('avatarUrl', ''),
                            'vipType': user_info.get('vipType', 0),
                            'userType': user_info.get('userType', 0)
                        },
                        'replied': replied,
                        'ipLocation': location
                    }
                    formatted.append(formatted_comment)
                except Exception as e:
                    print(f"格式化单条评论失败: {e}")
                    continue
            return formatted
        
        return {
            'comments': format_comment_list(comments_data.get('comments', [])),
            'hotComments': format_comment_list(comments_data.get('hotComments', [])),
            'total': comments_data.get('total', 0),
            'actualSortType': comments_data.get('actualSortType', 'unknown')
        }
    
    # ==================== 数据保存方法 ====================
    
    def save_comments_to_file(self, comments_data, playlist_id, filename=None):
        """
        保存评论数据到文件（同时保存JSON和CSV格式）
        
        Args:
            comments_data (dict): 评论数据
            playlist_id (str): 歌单ID
            filename (str): 文件名前缀，None时自动生成
        """
        try:
            if not filename:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'playlist_comments_{playlist_id}_{timestamp}'
            
            # 保存JSON格式（包含完整元数据）
            json_file = f'{filename}.json'
            data_to_save = {
                'playlist_id': playlist_id,
                'resource_type': 'A_PL_0_',
                'crawl_time': datetime.now().isoformat(),
                'total_comments': comments_data.get('total', 0),
                'hot_comments_count': len(comments_data.get('hotComments', [])),
                'regular_comments_count': len(comments_data.get('comments', [])),
                'actual_sort_type': comments_data.get('actualSortType', 'unknown'),
                'data': comments_data
            }
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, indent=2, ensure_ascii=False)
            
            # 保存CSV格式（便于数据分析）
            self.save_comments_to_csv(comments_data, f'{filename}.csv')
            
            print(f"\n✓ 评论数据已保存:")
            print(f"  JSON格式: {json_file}")
            print(f"  CSV格式: {filename}.csv")
            
        except Exception as e:
            print(f"✗ 保存数据失败: {e}")
    
    def save_comments_to_csv(self, comments_data, filename):
        """
        保存评论数据为CSV格式
        
        Args:
            comments_data (dict): 评论数据
            filename (str): CSV文件名
        """
        try:
            import csv
            
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                
                # 写入CSV表头
                writer.writerow([
                    '评论ID', '评论类型', '用户昵称', '用户ID', '评论内容', 
                    '点赞数', '回复数', '评论时间', 'IP位置'
                ])
                
                # 写入热门评论
                for comment in comments_data.get('hotComments', []):
                    writer.writerow([
                        comment.get('commentId', ''),
                        '热门评论',
                        comment.get('user', {}).get('nickname', ''),
                        comment.get('user', {}).get('userId', ''),
                        comment.get('content', '').replace('\n', ' ').replace('\r', ' '),
                        comment.get('likedCount', 0),
                        comment.get('replyCount', 0),
                        comment.get('time', ''),
                        comment.get('ipLocation', '')
                    ])
                
                # 写入普通评论
                for comment in comments_data.get('comments', []):
                    writer.writerow([
                        comment.get('commentId', ''),
                        '普通评论',
                        comment.get('user', {}).get('nickname', ''),
                        comment.get('user', {}).get('userId', ''),
                        comment.get('content', '').replace('\n', ' ').replace('\r', ' '),
                        comment.get('likedCount', 0),
                        comment.get('replyCount', 0),
                        comment.get('time', ''),
                        comment.get('ipLocation', '')
                    ])
                    
        except Exception as e:
            print(f"保存CSV失败: {e}")
    
    def print_comment_summary(self, comments_data, playlist_id):
        """
        打印评论数据摘要信息
        
        Args:
            comments_data (dict): 评论数据
            playlist_id (str): 歌单ID
        """
        if not comments_data:
            print("没有评论数据")
            return
        
        hot_comments = comments_data.get('hotComments', [])
        regular_comments = comments_data.get('comments', [])
        total = comments_data.get('total', 0)
        sort_type = comments_data.get('actualSortType', 'unknown')
        
        print(f"\n=== 歌单 {playlist_id} 评论摘要 ===")
        print(f"使用排序类型: {sort_type}")
        print(f"获取到的热门评论: {len(hot_comments)} 条")
        print(f"获取到的普通评论: {len(regular_comments)} 条")
        print(f"总计获取: {len(hot_comments) + len(regular_comments)} 条")

# ==================== 主程序入口 ====================
if __name__ == "__main__":
    print("=== 网易云音乐歌单评论爬虫 ===\n")
    
    # ==================== 可配置参数区域 ====================
    
    # 目标歌单配置
    PLAYLIST_ID = "19723756"        # 歌单ID（飙升榜）
    
    # 爬取配置
    MAX_PAGES = 20                  # 最大爬取页数
    REQUEST_DELAY = 2               # 请求间隔（秒）
    SORT_TYPE = 3                   # 排序类型（1:推荐, 2:最热, 3:最新）
    
    # 文件配置
    COOKIE_FILE = "cookies.json"    # Cookie文件路径
    OUTPUT_FILENAME = None          # 输出文件名（None为自动生成）
    
    # ==================== 执行爬取流程 ====================
    
    crawler = NeteaseCommentCrawler()
    
    # 1. 加载Cookie
    if not crawler.load_cookies_from_json(COOKIE_FILE):
        print("无法加载Cookie，程序退出")
        exit(1)
    
    try:
        # 2. 获取评论数据
        print(f"开始爬取歌单 {PLAYLIST_ID} 的评论...")
        
        comments_data = crawler.get_all_comments(
            playlist_id=PLAYLIST_ID,
            max_pages=MAX_PAGES,
            delay=REQUEST_DELAY,
            sort_type=SORT_TYPE
        )
        
        # 3. 处理和保存数据
        if comments_data and (comments_data.get('comments') or comments_data.get('hotComments')):
            # 格式化数据
            formatted_data = crawler.format_comments(comments_data)
            
            # 显示摘要
            crawler.print_comment_summary(formatted_data, PLAYLIST_ID)
            
            # 保存数据
            crawler.save_comments_to_file(
                formatted_data, 
                PLAYLIST_ID,
                OUTPUT_FILENAME
            )
            
            print(f"\n✓ 歌单评论数据爬取完成！")
            
        else:
            print("✗ 未获取到评论数据")
            
    except KeyboardInterrupt:
        print("\n用户中断程序")
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()