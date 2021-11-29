def getData(driver,keyword):
    try:
        return(driver.find_element_by_xpath("//li[contains(text(),'"+keyword+"')]").text)
    except:
        return('fail')

def getPrice(driver):
    try:
        temp=driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]').text
        prices.append(temp)
    except NoSuchElementException:
        temp=driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]').text
        return temp
    except:
        return temp

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
    return temp
