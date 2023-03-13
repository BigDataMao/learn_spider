# encoding:utf-8
import time
import datetime
import requests
import json
import urllib.parse
import urllib.request
import urllib.request
from bs4 import BeautifulSoup



def get_soup(url, url1):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()

    my_json = data.decode().replace("'", '"')
    data = json.loads(my_json)
    url0 = data["data"]["dataList"][0]["docPubUrl"]
    url = url1 + url0[url0.index('/', url0.index('/', url0.index('/') + 1) + 1) + 1:]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4512.6 Safari/537.36'
    }  # 爬虫[Requests设置请求头Headers],伪造浏览器
    proxies = {"http": None, "https": None}
    response = requests.get(url, proxies=proxies, headers=headers)  # 访问url
    soup = BeautifulSoup(response.content.decode("utf-8"), 'html.parser')  # 获取网页源代码
    return soup


def crawl_data(soup):
    tr = soup.find('table', class_='MsoNormalTable').find_all('tr')  # .find定位到所需数据位置  .find_all查找所有的tr（表格）
    ym = soup.find('div', class_='job-tit').get_text().strip()
    m_index = ym.index('月')
    busi_month = ym[:4] + ym[5:m_index].zfill(2)
    busi_month_m = 202212
    print(busi_month)

    if int(busi_month) > busi_month_m:
        for j in tr[1:]:  # tr2[1:]遍历第1列到最后一列，表头为第0列
            td = j.find_all('p')  # td表格
            rank_0 = td[0].get_text().strip()  # 遍历排名
            print(rank_0)
            member_id0 = td[1].get_text().strip()  # 遍历城市
            print(member_id0)


url = 'http://www.cfachina.org//qx-search/api/wcmSearch/searchDocsByProgram?pageNo=1&keyword=&programName=%E6%9C%9F%E8%B4%A7%E5%85%AC%E5%8F%B8%E6%9C%88%E5%BA%A6%E7%BB%8F%E8%90%A5%E6%95%B0%E6%8D%AE'
url1 = 'http://www.cfachina.org/informationpublicity/qhgsydjysj/'
soup = get_soup(url, url1)
crawl_data(soup)




