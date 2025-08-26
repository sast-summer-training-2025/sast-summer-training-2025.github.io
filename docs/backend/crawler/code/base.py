"""
网易云音乐基础爬虫
功能：爬取网易云音乐排行榜页面HTML内容
作者：Tempest
创建时间：2025
"""

import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin, urlparse
import json

class NeteaseMusicCrawler:
    """网易云音乐基础爬虫类"""
    
    def __init__(self):
        """初始化爬虫"""
        self.session = requests.Session()
        self.base_url = "https://music.163.com"
        
        # 设置请求头，模拟真实浏览器访问
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        self.session.headers.update(self.headers)
    
    def get_page(self, url, params=None, retries=3):
        """
        获取页面内容
        
        Args:
            url (str): 目标URL
            params (dict): 请求参数
            retries (int): 重试次数
            
        Returns:
            requests.Response: 响应对象
            
        Raises:
            requests.RequestException: 请求失败时抛出异常
        """
        for attempt in range(retries):
            try:
                response = self.session.get(url, params=params, timeout=10)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"请求失败 (尝试 {attempt + 1}/{retries}): {e}")
                if attempt < retries - 1:
                    # 随机延迟，避免被反爬虫机制检测
                    time.sleep(random.uniform(1, 3))
                else:
                    raise
    
    def crawl_toplist(self):
        """
        爬取网易云音乐排行榜页面
        
        Returns:
            str: HTML页面内容，失败时返回None
        """
        try:
            url = "https://music.163.com/discover/toplist"
            print(f"正在爬取排行榜页面: {url}")
            
            response = self.get_page(url)
            
            # 检查响应状态并返回结果
            if response.status_code == 200:
                print(f"成功获取页面，状态码: {response.status_code}")
                print(f"页面大小: {len(response.text)} 字符")
                return response.text
            else:
                print(f"页面请求失败，状态码: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"爬取排行榜页面失败: {e}")
            return None
    
    def save_html(self, html_content, filename):
        """
        保存HTML内容到文件
        
        Args:
            html_content (str): HTML内容
            filename (str): 保存的文件名
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTML内容已保存到: {filename}")
        except Exception as e:
            print(f"保存HTML文件失败: {e}")

# ==================== 主程序入口 ====================
if __name__ == "__main__":
    # 创建爬虫实例
    crawler = NeteaseMusicCrawler()
    
    # 爬取排行榜页面
    html_content = crawler.crawl_toplist()
    
    # 保存结果
    if html_content:
        crawler.save_html(html_content, 'netease_toplist.html')
        print("爬取完成！")
    else:
        print("爬取失败！")