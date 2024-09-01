import time
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.olx.com.pk/")
search=driver.find_element(By.CSS_SELECTOR,"#body-wrapper > div._1075545d.d059c029._4c726bfa._1709dcb4 > header > div.f6ca0ff5 > div._1e7904e8 > div > div > div._1075545d._1dc43551 > div > div._2cf807e6._828ba44c > input")
search.send_keys("Parrot")
btn = driver.find_element(By.CLASS_NAME, "a3e390b5")
btn.click()
time.sleep(5)
for i in range(1,35):
    time.sleep(2)
    # i=1
    # try:
    if i == 21:
        load=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/a/button/span")
        load.click()
        time.sleep(5)
        continue
    if i == 10:
        continue
    else:
        title_x=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li["+str(i)+"]/article/div[2]/div/div[2]/h2")
        price_x=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li["+str(i)+"]/article/div[2]/div/div[1]/span")
        address_x=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li["+str(i)+"]/article/div[2]/div/div[6]/span[1]")
        tim_x=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li["+str(i)+"]/article/div[2]/div/div[6]/span[2]")
        link_x=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li["+str(i)+"]/article/div[2]/div/a")
        img_x=driver.find_element(By.XPATH,"//*[@id='body-wrapper']/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li["+str(i)+"]/article/div[1]/picture/img")
        title=title_x.text
        price=price_x.text
        address=address_x.text
        tim=tim_x.text
        link=link_x.get_attribute("href")
        img=img_x.get_attribute("src")

        print(i,title,price,address,time,link,img)
    # except:
    #     print("x")
    #     continue

# //*[@id="body-wrapper"]/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/article/div[2]/div/div[1]/span
# //*[@id="body-wrapper"]/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[2]/article/div[2]/div/div[1]
# //*[@id="body-wrapper"]/div[2]/header[2]/div/div/div/div[2]/div[2]/div[2]/div/ul/li[3]/article/div[2]/div/div[1]/span
