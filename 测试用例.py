import jdSpider
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# 如果重复开启driver会很慢，因此先开启然后将driver传入函数中
options = webdriver.ChromeOptions()
#options.add_argument('--headless')  #开启无头模式
#更改chromedriver.exe路径
driver = webdriver.Chrome(executable_path = 'D:\chromedriver.exe',options = options)
driver.maximize_window()

url='https://item.jd.com/11062841516.html'
needlist=['商品名称','商品编号','商品产地','制作口味','适用场景']
result=jdSpider.spider(driver,url,needlist)

print(result)
