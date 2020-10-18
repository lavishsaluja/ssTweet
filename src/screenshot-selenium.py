from selenium import webdriver

PATH_TO_CHROME_DRIVER = "/Users/lavishsaluja/Downloads/ssTweet/env/bin/chromedriver"
URL = "https://twitter.com/mikecvet/status/1317890418432901120"


def save_screenshot(url):
        
    full = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div"
    tweet_text = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[1]/div/div"
    profile_image = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[1]/div/div/a/div[2]"
    header_name = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div/div/div"

    driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)
    driver.get(URL)
    driver.implicitly_wait(10)
    tweet = driver.find_element_by_xpath(full)
    tweet.screenshot("image.png")
    driver.quit()
