"""
网易云音乐内部API爬虫
功能：使用网易云内部API获取音乐排行榜数据
特点：直接调用官方API接口，获取结构化JSON数据
技术：v3版本播放列表接口，无需解析HTML
作者：Tempest
创建时间：2025
"""

import requests
import json
import time
from datetime import datetime

class NeteaseInternalAPICrawler:
    """网易云音乐内部API爬虫类"""
    
    def __init__(self):
        """初始化爬虫，配置API访问参数"""
        self.session = requests.Session()
        
        # 配置请求头，模拟网易云官方客户端
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://music.163.com/',
            'Origin': 'https://music.163.com'
        }
        self.session.headers.update(self.headers)
        
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
            
            print(f"成功加载{len(cookies_dict)}个Cookie\n")
            return True
        except Exception as e:
            print(f"加载Cookie失败: {e}")
            return False
    
    # ==================== API调用方法 ====================
    
    def get_playlist_detail(self, playlist_id):
        """
        使用v3接口获取歌单详情
        
        Args:
            playlist_id (str): 歌单ID
            
        Returns:
            dict: 包含歌单信息和歌曲列表的字典，失败时返回None
        """
        try:
            url = "https://music.163.com/api/v3/playlist/detail"
            
            # API请求参数
            params = {
                'id': playlist_id,
                'n': 1000,  # 获取歌曲数量上限
                's': 8      # 详情级别参数
            }
            
            print(f"正在使用v3接口获取歌单 {playlist_id} 的详情...")
            response = self.session.get(url, params=params, timeout=15)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 200:
                    playlist = result.get('playlist', {})
                    tracks = playlist.get('tracks', [])
                    
                    print(f"✓ 成功获取歌单信息")
                    
                    # 提取关键信息并返回
                    return {
                        'playlist_info': {
                            'id': playlist.get('id'),
                            'name': playlist.get('name'),
                            'description': playlist.get('description'),
                            'creator': playlist.get('creator', {}).get('nickname'),
                            'playCount': playlist.get('playCount'),
                            'trackCount': playlist.get('trackCount'),
                            'coverImgUrl': playlist.get('coverImgUrl'),
                            'updateTime': playlist.get('updateTime')
                        },
                        'tracks': tracks
                    }
                else:
                    print(f"✗ API返回错误: {result.get('message', '未知错误')}")
                    print(f"  错误代码: {result.get('code')}")
            else:
                print(f"✗ HTTP错误: {response.status_code}")
                print(f"  响应内容: {response.text[:200]}...")
                
        except Exception as e:
            print(f"✗ 请求异常: {e}")
        
        return None
    
    def get_soaring_chart(self):
        """
        获取网易云音乐飙升榜数据
        飙升榜ID: 19723756（网易云官方榜单）
        
        Returns:
            dict: 飙升榜数据，失败时返回None
        """
        playlist_id = "19723756"  # 飙升榜官方ID
        
        print("=== 获取网易云音乐飙升榜 ===")
        
        # 调用v3接口获取榜单数据
        result = self.get_playlist_detail(playlist_id)
        
        return result
    
    # ==================== 数据处理方法 ====================
    
    def format_song_data(self, tracks):
        """
        格式化歌曲数据，提取关键信息
        
        Args:
            tracks (list): 原始歌曲数据列表
            
        Returns:
            list: 格式化后的歌曲数据列表
        """
        formatted_songs = []
        
        for i, track in enumerate(tracks):
            try:
                # 格式化艺术家信息
                artists = []
                if track.get('ar'):
                    artists = [artist.get('name', '') for artist in track['ar']]
                
                # 格式化歌曲时长
                duration_ms = track.get('dt', 0)
                duration_min = duration_ms // 60000
                duration_sec = (duration_ms % 60000) // 1000
                duration_str = f"{duration_min:02d}:{duration_sec:02d}"
                
                # 格式化专辑信息
                album_name = ""
                album_id = ""
                if track.get('al'):  
                    album_name = track['al'].get('name', '')
                    album_id = track['al'].get('id', '')
                
                # 构建格式化的歌曲数据对象
                song_data = {
                    'rank': i + 1,                                    # 排行榜排名
                    'id': track.get('id'),                           # 歌曲ID
                    'name': track.get('name', ''),                   # 歌曲名称
                    'artists': artists,                              # 艺术家列表
                    'artists_str': ' / '.join(artists),             # 艺术家字符串
                    'album_name': album_name,                        # 专辑名称
                    'album_id': album_id,                           # 专辑ID
                    'duration': duration_str,                        # 格式化时长
                    'duration_ms': duration_ms,                      # 毫秒时长
                    'popularity': track.get('pop', 0),               # 流行度
                    'mvid': track.get('mv', 0),                     # MV ID
                    'fee': track.get('fee', 0),                     # 付费类型
                    'status': track.get('st', 0),                   # 歌曲状态
                    'track_number': track.get('no', 0),             # 专辑曲目编号
                    'version': track.get('v', 0),                   # 版本号
                    'copyright': track.get('copyright', 0),          # 版权状态
                    'publishTime': track.get('publishTime', 0)       # 发布时间戳
                }
                
                formatted_songs.append(song_data)
                
            except Exception as e:
                print(f"格式化第{i+1}首歌曲失败: {e}")
                continue
        
        return formatted_songs
    
    def print_chart_summary(self, chart_data):
        """
        打印飙升榜数据摘要
        
        Args:
            chart_data (dict): 榜单数据
            
        Returns:
            list: 格式化的歌曲数据列表
        """
        if not chart_data:
            print("没有数据可显示")
            return []
        
        playlist_info = chart_data.get('playlist_info', {})
        tracks = chart_data.get('tracks', [])
        
        print(f"\n=== {playlist_info.get('name', '飙升榜')} ===")
        print(f"歌单ID: {playlist_info.get('id')}")
        print(f"播放次数: {playlist_info.get('playCount', 0):,}")
        print(f"歌曲总数: {len(tracks)}")
        print(f"更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 格式化歌曲数据并返回
        formatted_songs = self.format_song_data(tracks)
        
        return formatted_songs
    
    # ==================== 数据保存方法 ====================
    
    def save_chart_data(self, chart_data, songs_data):
        """
        保存飙升榜数据到文件
        
        Args:
            chart_data (dict): 原始榜单数据
            songs_data (list): 格式化的歌曲数据
        """
        try:
            # 构建保存数据结构
            data = {
                'chart_name': '网易云音乐飙升榜',
                'update_time': datetime.now().isoformat(),
                'total_songs': len(songs_data),
                'songs': songs_data
            }
            
            # 保存JSON格式（包含完整数据）
            with open('soaring_chart_songs.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # 保存CSV格式（便于数据分析）
            self.save_to_csv(songs_data, 'soaring_chart_songs.csv')
            
            print(f"\n✓ 数据已保存:")
            print(f"  歌曲数据: soaring_chart_songs.json")
            print(f"  CSV格式: soaring_chart_songs.csv")
            
        except Exception as e:
            print(f"✗ 保存数据失败: {e}")
    
    def save_to_csv(self, songs_data, filename):
        """
        保存歌曲数据为CSV格式
        
        Args:
            songs_data (list): 歌曲数据列表
            filename (str): CSV文件名
        """
        try:
            import csv
            
            with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                if songs_data:
                    # 使用第一首歌的字段作为CSV表头
                    writer = csv.DictWriter(f, fieldnames=songs_data[0].keys())
                    writer.writeheader()
                    writer.writerows(songs_data)
                    
        except Exception as e:
            print(f"保存CSV失败: {e}")

# ==================== 主程序入口 ====================
if __name__ == "__main__":
    print("=== 网易云音乐飙升榜API爬虫 (v3接口) ===\n")
    
    # 创建爬虫实例
    crawler = NeteaseInternalAPICrawler()

    # 加载Cookie（用于访问需要登录的接口）
    crawler.load_cookies_from_json("cookies.json")
    
    # 获取飙升榜数据
    chart_data = crawler.get_soaring_chart()
    
    if chart_data:
        # 显示摘要并获取格式化的歌曲数据
        songs_data = crawler.print_chart_summary(chart_data)

        # 保存数据到文件
        crawler.save_chart_data(chart_data, songs_data)
        
        print(f"\n✓ 飙升榜数据获取完成！")
        
    else:
        print("✗ 获取飙升榜数据失败")