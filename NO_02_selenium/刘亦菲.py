from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# 创建驱动配置
chrome_options = webdriver.ChromeOptions()
# 配置保持不关闭
chrome_options.add_experimental_option('detach', True)
# 创建驱动本体
driver = webdriver.Chrome(options=chrome_options)
# 驱动打开网页
driver.get('https://image.baidu.com')
# 找到输入框并输入文字
driver.find_element_by_id('kw').send_keys('刘亦菲')
# 点击搜索
driver.find_element_by_class_name('s_newBtn').click()
# 点击第一张图片
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[1]/ul/li[1]/div/div[2]/a/img').click()
# 切换句柄
handles = driver.window_handles
driver.switch_to.window(handles[1])

for i in range(1, 11, 1):
    # 获取本页图片元素
    time.sleep(5)
    image_element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/img')
    time.sleep(1)
    # 获取此元素的链接
    url = image_element.get_attribute('src')
    print(url)
    img = requests.get(url=url).content
    # 写入文件
    j = f'{i:02d}'
    with open(f'../output/刘亦菲/刘亦菲{j}.jpg', 'wb') as f:
        f.write(img)

    # 点击下一张图片按钮
    driver.find_element_by_class_name('img-next').click()
    time.sleep(1)

print('爬取完毕')