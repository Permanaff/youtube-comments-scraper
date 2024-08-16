#you tube comments on  you tube orignal Ai series.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

video_title = input('Video Title : ')

driver=webdriver.Chrome()
driver.set_page_load_timeout(60)
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(5)
search=driver.find_element(By.NAME,"search_query")
search.clear()
search.send_keys(video_title)

search.send_keys(Keys.ENTER)
sleep(5)
link=driver.find_element(By.XPATH,"""//*[@id="video-title"]/yt-formatted-string""")
link.click()
sleep(20)
for i in range(500):
    driver.execute_script("window.scrollBy(0,700)","")
    sleep(2)
sleep(20)
list=[]

comment=driver.find_elements(By.XPATH,"""//*[@id="content-text"]/span""")
for i in comment:
    print(i)
    list.append(i.text)

print(list)
print(len(list))
import pandas as pd
df=pd.DataFrame({"comment":list})
df.to_csv("comment_youtube_4.csv",index=False)
assert "No results found." not in driver.page_source
driver.close()