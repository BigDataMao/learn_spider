import requests
from lxml import etree
'''
第一个爬虫:链家二手房第一页,目标是打印输出所有的房源标题
'''

class LianjiaSpider:
    # 初始化
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'

    # 获取结果的方法
    def get_html(self):
        res = requests.get(url=self.url, headers={'User-Agent': self.user_agent})
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    # 解析模块单列
    def parse_page(self, html):
        tree = etree.HTML(html)
        name_list = tree.xpath('//div/ul/li/div/div/a/text()')
        for name in name_list:
            print(name)

    # 程序入口函数
    def run(self):
        self.get_html()


# 实例化以后执行
if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
