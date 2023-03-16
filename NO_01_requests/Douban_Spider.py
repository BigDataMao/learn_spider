# 导包
import requests
import time
from lxml import etree
import pymysql

# base_url,parse,headers
base_url = 'https://movie.douban.com/top250'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
}
params = {
    'start': '0',
    'filter': ''
}
i = 1
conn = pymysql.connect(
    host='124.221.228.129',
    user='root',
    password='mxw19910712@MYSQL'
)
cursor = conn.cursor()
for page in range(0, 250, 25):
    params['start'] = str(page)
    html = requests.get(url=base_url, params=params, headers=headers).text

    # xpath模块解码
    etree_html = etree.HTML(html)
    film_list = etree_html.xpath('//li/div/div[2]')

    for film in film_list:
        no = i
        name = film.xpath('./div/a/span[1]/text()')[0].strip()
        star = film.xpath('./div/p/text()')[0].replace("\'", '').strip()
        score = round(float(film.xpath('./div/div/span[2]/text()')[0].strip()),1)
        row = [no, name, star, score]
        print(row)
        cursor.execute(f"insert into spider_data.t_douban values({no},'{name}','{star}',{score});")
        conn.commit()
        i += 1
    time.sleep(2)
conn.close()
# 打印一页尝试

# 更改多页

# 更改进入数据库
