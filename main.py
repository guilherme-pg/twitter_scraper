
# https://stackoverflow.com/questions/31147660/importerror-no-module-named-selenium

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://twitter.com/i/flow/login')
time.sleep(12)


# LOGIN
login = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login.send_keys(LOGIN)
time.sleep(3)
button_next = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
time.sleep(5)



if driver.find_element('xpath', '//*[@id="modal-header"]/span/span').text == 'Digite sua senha':
    # PASSWORD
    password = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(PASSWORD)
    time.sleep(3)
    button_enter = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
    time.sleep(5)
    
else:
    # VALIDATION
    validation = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    validation.send_keys(LOGIN_NAME)
    time.sleep(2)
    button_advance = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
    time.sleep(5)
    
    # PASSWORD
    password = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys('Pandora00')
    time.sleep(3)
    button_enter = driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
    time.sleep(5)
    



# wait until a specific part of the page loads
WebDriverWait(driver, 10).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input' )))

researched = "Ciro Gomes"

search = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search.send_keys(researched)
search.send_keys(Keys.ENTER)
time.sleep(5)




# click on the tag to search for people on twitter
people = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a').click()
time.sleep(5)

# PATH to the profile searched for
profile = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[4]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span').click()


soup = BeautifulSoup(driver.page_source, 'lxml')


# PROBLEMA: JUMPING TWEETS
postings = soup.find_all('div', class_= 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
dates = soup.find_all('a', class_= 'css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-xoduu5 r-1q142lx r-1w6e6rj r-37j5jr r-a023e6 r-16dba41 r-9aw3ui r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0')







twetts = []
time_interval = []

while True:
  for post in postings:
      twetts.append(post.text)
  
  for date in dates:
      time_interval.append(date.text)
  
    
  driver.execute_script('window.scroll(0, document.body.scrollHeight)')
  time.sleep(5)
  soup = BeautifulSoup(driver.page_source, 'lxml')
  
  postings = soup.find_all('div', class_='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
  dates = soup.find_all('a', class_= 'css-4rbku5 css-18t94o4 css-901oao r-14j79pv r-1loqt21 r-xoduu5 r-1q142lx r-1w6e6rj r-37j5jr r-a023e6 r-16dba41 r-9aw3ui r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0')


  if len(time_interval) > 20:
      break
  
  if len(twetts) > 20:
      break
  
    tweets2 = list(set(twetts))
  if len(tweets2) > 20:
      break




