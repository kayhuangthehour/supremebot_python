#-*- coding: UTF-8 -*-
import time
try:  
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except ImportError:
    print ("Selenium module is not installed...Exiting program.")
    exit(1)
     
def Check(keywords, text):
    for i in keywords:
        if i not in text:
            return False
    return True
 
def searchCommodity(browser, category, keywords, color):    
    print ("[/i][/i][/i][i][i][i] Searching Commodity ...")
    browser.get("http://www.supremenewyork.com/shop/all/" + category)
    links = browser.find_elements_by_class_name("name-link")
    i = 0
    while i < len(links):
        if (Check(keywords, links[i].text) & (color in links[i+1].text)):
            print ("Description : " + links[i].text)
            print ("Color : " + links[i+1].text)
            links[i].click()
            print ("[/i][/i][/i][/i][/i][/i][i][i][i] Commodity found")
            return True
        i += 2
    print ("[/i][/i][/i][i][i][i] Commodity not found")
    return False
def fillForm(browser):
    billing_name = "bjyxszd"
    email = "bjyxszd.work@gmail.com"
    tel = "10050805"
    billing_address = "xxxxxxxxx"
    billing_city = "YunMeng"
    billing_zip = "11111"
    billing_state = "Hubei"
    billing_country = "China"
    nlb = "9999 999 999 9999"
    month = "02"
    year = "2018"
    rvv = "888"
    name = browser.find_element_by_name("order[billing_name]").send_keys(billing_name)
    email = browser.find_element_by_name("order[email]").send_keys(email)
    tel = browser.find_element_by_name("order[tel]").send_keys(tel)
    address = browser.find_element_by_name("order[billing_address]").send_keys(billing_address)
    address = browser.find_element_by_name("order[billing_city]").send_keys(billing_city)
    postCode = browser.find_element_by_name("order[billing_zip]").send_keys(billing_zip)
    billing_state = browser.find_element_by_name('order[billing_state]').send_keys(billing_state)
    countrySelect = Select(browser.find_element_by_name("order[billing_country]")).select_by_visible_text(billing_country)
    creditCardSelect = browser.find_element_by_name('credit_card[nlb]').send_keys(nlb)
    monthExpirationSelect = Select(browser.find_element_by_name("credit_card[month]")).select_by_visible_text(month)
    yearExpirationSelect = Select(browser.find_element_by_name("credit_card[year]")).select_by_visible_text(year)
    cvv = browser.find_element_by_name("credit_card[rvv]").send_keys(rvv)
    browser.find_element_by_class_name("terms").click()
def main():
    print (" _____________博君一肖是真的 ———————————————————————————————— ")
    print (" ____                                      ____   ___ _____ ")
    print ("/ ___| _   _ _ __  _ __ ___ _ __ ___   ___| __ ) / _ \_   _|")
    print ("\___ \| | | | '_ \| '__/ _ \ '_ ` _ \ / _ \  _ \| | | || |")
    print (" ___) | |_| | |_) | | |  __/ | | | | |  __/ |_) | |_| || |")
    print ("|____/ \__,_| .__/|_|  \___|_| |_| |_|\___|____/ \___/ |_|  ")
    print ("            |_|                                             ")
    print ("[/i][/i][/i][i][i][i] Opening Browser ...")
    browser = webdriver.Chrome('/Users/kayhuang/Downloads/chromedriver')
    browser.implicitly_wait(3)  #隐性等待3s，隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
    print ("[/i][/i][/i][i][i][i] Browser Opened")
    raw_input('[/i][/i][/i][i][i][i]Press Enter to buy your Commodity')
    category = "pants"  #商品类别
    keywords = []
    keywords.append("Tiger Stripe Track Pant")  #商品关键字
    color = "Brown"  #颜色
    size = 'Medium'
    if searchCommodity(browser, category, keywords, color) == False:
        return -1
    if size != "":
        try:
            sizeSelect = Select(browser.find_element_by_id("s"))
            sizeSelect.select_by_visible_text(size)
        except:
            print ("[/i][/i][/i][i][i][i] Commodity sold out.......")
            return -1
    try:
        browser.find_element_by_name("commit").click()
    except:
         print ("[/i][/i][/i][i][i][i] Commodity sold out")
         return -1
    time.sleep(1)  #睡一秒，主要是怕报错
    browser.find_element_by_class_name("checkout").click()
    print ("Filling in the information")
    fillForm(browser)
    print ("Filled...")
    print ("Prepare to buy a bill.....")
    browser.find_element_by_name("commit").click()
    print ("bjyxszd")
 
if __name__ == '__main__':
    main()