"""
网易云音乐Cookie爬虫
功能：使用Cookie进行登录状态爬取，支持多种Cookie输入方式
特点：支持登录验证、Cookie管理、状态保持
作者：Tempest
创建时间：2025
"""

import requests
import json
import os
from urllib.parse import urljoin
import time

class NeteaseMusicCrawler:
    """网易云音乐Cookie爬虫类"""
    
    def __init__(self):
        """初始化爬虫，配置请求会话"""
        self.session = requests.Session()
        self.base_url = "https://music.163.com"
        
        # 配置更完整的请求头，增强反检测能力
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
        self.session.headers.update(self.headers)
        
    # ==================== Cookie管理方法 ====================
        
    def load_cookies_from_file(self, cookie_file="cookies.json"):
        """
        从文件加载Cookie
        支持JSON格式和Netscape格式
        
        Args:
            cookie_file (str): Cookie文件路径
            
        Returns:
            bool: 加载成功返回True，失败返回False
        """
        try:
            if not os.path.exists(cookie_file):
                print(f"Cookie文件不存在: {cookie_file}")
                return False
                
            with open(cookie_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
            # 处理JSON格式Cookie
            if content.startswith('[') or content.startswith('{'):
                cookies_data = json.loads(content)
                if isinstance(cookies_data, list):
                    # 处理Cookie数组格式
                    for cookie in cookies_data:
                        if 'domain' in cookie and '.163.com' in cookie['domain']:
                            self.session.cookies.set(
                                name=cookie['name'],
                                value=cookie['value'],
                                domain=cookie['domain'],
                                path=cookie.get('path', '/'),
                                secure=cookie.get('secure', False)
                            )
                elif isinstance(cookies_data, dict):
                    # 处理Cookie对象格式
                    for name, value in cookies_data.items():
                        self.session.cookies.set(name, value, domain='.163.com')
            else:
                # 处理文本格式Cookie
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            name, value = line.split('=', 1)
                            self.session.cookies.set(name.strip(), value.strip(), domain='.163.com')
                            
            print(f"成功加载Cookie，共{len(self.session.cookies)}个")
            return True
            
        except Exception as e:
            print(f"加载Cookie失败: {e}")
            return False
    
    def set_cookies_from_string(self, cookie_string):
        """
        从Cookie字符串设置Cookie
        
        Args:
            cookie_string (str): Cookie字符串，格式: "name1=value1; name2=value2; ..."
            
        Returns:
            bool: 设置成功返回True，失败返回False
        """
        try:
            cookies = {}
            for cookie in cookie_string.split(';'):
                cookie = cookie.strip()
                if '=' in cookie:
                    name, value = cookie.split('=', 1)
                    cookies[name.strip()] = value.strip()
                    self.session.cookies.set(name.strip(), value.strip(), domain='.163.com')
            
            print(f"成功设置Cookie，共{len(cookies)}个")
            return True
        except Exception as e:
            print(f"设置Cookie失败: {e}")
            return False
    
    def input_cookies_manually(self):
        """
        手动输入Cookie
        
        Returns:
            bool: 输入成功返回True，失败返回False
        """
        print("\n请输入Cookie (格式: name1=value1; name2=value2; ...):")
        print("或者输入单个重要Cookie (如: MUSIC_U=xxx):")
        cookie_string = input().strip()
        
        if cookie_string:
            return self.set_cookies_from_string(cookie_string)
        return False
    
    # ==================== 登录状态验证 ====================
    
    def verify_login_status(self):
        """
        验证登录状态
        
        Returns:
            bool: 登录有效返回True，无效返回False
        """
        try:
            # 访问用户信息接口验证登录状态
            verify_url = "https://music.163.com/api/nuser/account/get"
            response = self.session.get(verify_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('account'):
                    print(f"登录验证成功！用户: {data['account'].get('userName', '未知')}")
                    return True
                else:
                    print("Cookie可能已过期或无效")
                    return False
            else:
                print(f"验证请求失败，状态码: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"验证登录状态失败: {e}")
            return False
    
    # ==================== 页面爬取方法 ====================
    
    def crawl_toplist(self):
        """
        爬取排行榜页面
        
        Returns:
            str: HTML页面内容，失败时返回None
        """
        try:
            url = "https://music.163.com/discover/toplist"
            print(f"正在爬取排行榜页面: {url}")
            
            # 设置Referer头部，模拟正常访问
            headers = self.headers.copy()
            headers['Referer'] = 'https://music.163.com'
            
            response = self.session.get(url, headers=headers, timeout=15)
            response.encoding = 'utf-8'
            
            if response.status_code == 200:
                print(f"成功获取页面内容，大小: {len(response.text)} 字符")
                return response.text
            else:
                print(f"获取页面失败，状态码: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"爬取页面失败: {e}")
            return None
    
    # ==================== 文件操作方法 ====================
    
    def save_html(self, html_content, filename):
        """
        保存HTML内容到文件
        
        Args:
            html_content (str): HTML内容
            filename (str): 保存的文件名
            
        Returns:
            bool: 保存成功返回True，失败返回False
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTML内容已保存到: {filename}")
            return True
        except Exception as e:
            print(f"保存文件失败: {e}")
            return False
    
    def save_cookies_to_file(self, filename):
        """
        保存当前Cookie到文件
        
        Args:
            filename (str): 保存的文件名
            
        Returns:
            bool: 保存成功返回True，失败返回False
        """
        try:
            cookies_dict = {}
            for cookie in self.session.cookies:
                cookies_dict[cookie.name] = cookie.value
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(cookies_dict, f, indent=2, ensure_ascii=False)
            
            print(f"Cookie已保存到: {filename}")
            return True
        except Exception as e:
            print(f"保存Cookie失败: {e}")
            return False

# ==================== 主程序入口 ====================
if __name__ == "__main__":
    crawler = NeteaseMusicCrawler()
    
    print("=== 网易云音乐Cookie爬虫 ===\n")
    
    # Cookie输入选择
    print("请选择Cookie输入方式:")
    print("1. 从文件加载")
    print("2. 手动输入")
    
    choice = input("请输入选择 (1或2): ").strip()
    
    cookie_loaded = False
    
    # 根据用户选择加载Cookie
    if choice == '1':
        cookie_file = input("请输入Cookie文件名 (默认: cookies.json): ").strip() or "cookies.json"
        if cookie_file:
            cookie_loaded = crawler.load_cookies_from_file(cookie_file)
    elif choice == '2':
        cookie_loaded = crawler.input_cookies_manually()
    else:
        print("无效选择")
    
    if not cookie_loaded:
        print("未能加载Cookie，程序退出")
        exit(1)
    
    # 验证登录状态
    print("\n正在验证登录状态...")
    if not crawler.verify_login_status():
        print("登录验证失败，尝试继续爬取页面...")
    
    # 开始爬取
    print("\n开始爬取排行榜页面...")
    html_content = crawler.crawl_toplist()
    
    if html_content:
        filename = "netease_toplist_cookie.html"
        crawler.save_html(html_content, filename)
        
        # 询问是否保存Cookie
        save_cookies = input("\n是否保存当前Cookie到文件？(y/n，默认yes): ").lower().strip() or 'y'
        if save_cookies == 'y':
            cookie_filename = input("请输入保存Cookie的文件名 (默认: cookies.json): ").strip()
            if not cookie_filename:
                cookie_filename = "cookies.json"
            crawler.save_cookies_to_file(cookie_filename)
        
        print(f"\n爬取完成！")
        print(f"HTML文件: {filename}")
        print(f"文件大小: {len(html_content)} 字符")
            
    else:
        print("爬取失败！")