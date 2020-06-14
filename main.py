# WHATSAPP WEB AUTOMATION

#importing libraries
import time
import selenium
from selenium import webdriver
#specifying the path to chromedriver
PATH = "/Users/architlal/Desktop/untitled folder/chromedriver"

driver = webdriver.Chrome(PATH)
#url to open
driver.get("https://web.whatsapp.com")

#wait
time.sleep(10)

#Enter the name of the person you want to text
user_name = "Mom"

#opening the chat
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(user_name))
user.click()

#this is an infinite loop
while True :
    #wait
    time.sleep(1)
    message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
    #Enter the text to be sent
    message_box.send_keys("I love you!!!")
    #clicking send button
    send_button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
    send_button.click()
