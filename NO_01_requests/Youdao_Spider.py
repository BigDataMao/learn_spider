"""
有道翻译爬虫
有输入,打印翻译结果
2023年3月11日
"""
import json
import time
import requests
from hashlib import md5


def md5_string(string):
    # 功能函数01:对一个字符串md5加密
    s = md5()
    s.update(string.encode())

    return s.hexdigest()


class Youdao_Spider:
    def __init__(self):
        self.url = 'https://dict.youdao.com/webtranslate'
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '247',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=120629523@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=1075376228.6027513',
            'Host': 'dict.youdao.com',
            'Origin': 'https://fanyi.youdao.com',
            'Referer': 'https://fanyi.youdao.com/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
        }

    def get_sign_mysticTime(self):
        # 获取不同情况下的sign和mysticTime值
        mysticTime = round(time.time() * 1000)
        key = 'fsdsogkndfokasodnaso'
        e = str(mysticTime)
        ll = 'fanyideskweb'
        d = 'webfanyi'
        str01 = f'client={ll}&mysticTime={e}&product={d}&key={key}'
        sign = md5_string(str01)

        return sign, mysticTime

    def attack_yd(self, word):
        # 用生成的form表单访问有道
        sign, mysticTime = self.get_sign_mysticTime()
        data = {
            'i': word,
            'from': 'auto',
            'to': '',
            'domain': '0',
            'dictResult': 'true',
            'keyid': 'webfanyi',
            'sign': sign,
            'client': 'fanyideskweb',
            'product': 'webfanyi',
            'appVersion': '1.0.0',
            'vendor': 'web',
            'pointParam': 'client,mysticTime,product',
            'mysticTime': mysticTime,
            'keyfrom': 'fanyi.web'
        }
        html = requests.post(url=self.url, data=data, headers=self.headers).json()
        print(html)


    def run(self):
        word = input('请输入您要翻译的单词:')
        self.attack_yd(word=word)


if __name__ == '__main__':
    spider = Youdao_Spider()
    spider.run()
