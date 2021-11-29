from selenium.common.exceptions import NoSuchElementException
def getData(driver,keyword):
    try:
        return(driver.find_element_by_xpath("//li[contains(text(),'"+keyword+"')]").text)
    except:
        return('fail')

def getPrice(driver):
    try:
        temp=driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]').text
        return temp
    except NoSuchElementException:
        temp=driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]').text
        return temp
    except:
        return ('fail')

def spider(driver,link,needlist):
    driver.get(link)
    temp=[]
    try:
        element=driver.find_element_by_class_name('p-parameter')
    except:
        temp=[['fail']*len(needlist) for x in range(len(needlist))]
    else:
        for i in needlist:
            temp.append(getData(driver,i))
    
    #如果想要价格信息开启
    temp.append(getPrice(driver))

    temp.append(link)
    return temp
