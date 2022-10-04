# SCRAPER version 3.0

# PROBLEM: JUMPING TWEETS
# PROBLEM: RETRIEVE DUPLICATED DATA



# IMPORT DEPENDECIES
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time
import os
from dotenv import load_dotenv

# https://www.youtube.com/watch?v=gpCnquo-HvQ

load_dotenv()

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://twitter.com/i/flow/login')

time.sleep(10)





# SETUP LOG IN
login = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login.send_keys(os.getenv('LOGIN'))
time.sleep(3)
button_next = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
button_next.click()
time.sleep(5)


if driver.find_element('xpath', '//*[@id="modal-header"]/span/span').text == 'Digite sua senha':
    # PASSWORD
    password = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(os.getenv('PASSWORD'))
    time.sleep(3)
    button_enter = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    button_enter.click()
    time.sleep(5)
    
else:
    # VALIDATION
    validation = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    validation.send_keys(os.getenv('VALIDATION'))
    time.sleep(3)
    button_advance = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
    button_advance.click()
    time.sleep(5)
    
    # PASSWORD
    password = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(os.getenv('PASSWORD'))
    time.sleep(3)
    button_enter = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
    button_enter.click()
    time.sleep(5)





# SEARCH ITEM AND FETCH IT

# wait until a specific part of the page loads
WebDriverWait(driver, 10).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input' )))

researched = "Ciro Gomes"

search = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search.send_keys(researched)
search.send_keys(Keys.ENTER)
time.sleep(5)



# click on the tag to search for PEOPLE on twitter
people = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a')
people.click()
time.sleep(5)

# PATH to the profile searched for
profile = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span')
profile.click()
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'lxml')



# UserTag = driver.find_element(By.XPATH, '//div[@data-testid="User-Names"]').text
# TimeStamp = driver.find_element(By.XPATH, "//time").get_attribute('datetime')
# Tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text

# Reply = driver.find_element(By.XPATH, "//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH, "//div[@data-testid='retweet']").text
# Likes = driver.find_element(By.XPATH, "//div[@data-testid='like']").text






# AUTOMATE PROCESS
UserTags = []
TimeStamps = []
Tweets = []
Likes = []
reTweets = []
Replys = []

articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

while True:
    for article in articles:
        UserTag = driver.find_element(By.XPATH, ".//div[@data-testid='User-Names']").text
        UserTags.append(UserTag)
    
        TimeStamp = driver.find_element(By.XPATH, ".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = driver.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
    
        Reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH, ".//div[@data-testid='like']").text
        Likes.append(Like)
        
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)
    
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    
    Tweets2 = list(set(Tweets));
    if len(Tweets2) >= 20:
        break





# EXPORT RETRIEVED DATA
# df = pd.DataFrame(zip(UserTags, TimeStamps, Tweets, Replys, reTweets, Likes),
#                  columns=["UserTags", "TimeStamps", "Tweets", "Replys", "reTweets", "Likes"])

df = pd.DataFrame({'UserTags':UserTags, 'TimeStamps':TimeStamps, 'Tweets':Tweets,'Replys':Replys, 'reTweets':reTweets, 'Likes':Likes})


#df.head()

df.to_excel('df_tweets.xlsx', index=False)







