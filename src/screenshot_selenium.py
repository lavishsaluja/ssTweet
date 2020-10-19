import time
from selenium import webdriver
import os

PATH_TO_CHROME_DRIVER = os.getcwd() + "/env/bin/chromedriver"


def save_screenshot(url, name):
    
    full = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div"
    tweet_text = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[1]/div/div"
    profile_image = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[1]/div/div/a/div[2]"
    header_name = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div/div/div"

    driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    driver.get(url)
    time.sleep(2) # waiting for the window to load completely before picking the element
    tweet = driver.find_element_by_xpath(full)
    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)
    tweet.screenshot(folder_name + '/' + name + ".png")
    driver.quit()
