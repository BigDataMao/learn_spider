from selenium import webdriver
# 新版selenium的写法
from selenium.webdriver.common.by import By

# 运行完毕不关窗口
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://image.baidu.com')
driver.find_element(By.ID, 'kw').send_keys('刘亦菲')
driver.find_element(By.XPATH, '//*[@id="homeSearchForm"]/span[2]/input').click()
element_list = driver.find_elements(By.CLASS_NAME, 'imgitem')
for element in element_list:
    img_url = element.get_attribute('data-fromurl')
    print(img_url)
