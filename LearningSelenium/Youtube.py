from sys import executable

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Youtube():
    def home(self):
        options= webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options)
        #driver.manage().window().setSize()

        driver.get("https://www.youtube.com/")
        driver.find_element(By.NAME, 'search_query').send_keys('selenium python project')
        driver.find_element(By.CSS_SELECTOR, '.ytSearchboxComponentSearchButton').click()
        driver.find_element(By.CLASS_NAME, 'style-scope ytd-video-renderer').click()
searchpage= Youtube() #class name
searchpage.home() #function name