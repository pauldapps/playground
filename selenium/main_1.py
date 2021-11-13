from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.alarm.com/web/system/video/live-view?cameraGroupId=all"
 
driver = webdriver.Chrome()
driver.get(url)
"""
 search_box = driver.find_element_by_name('q')  # Find search input box.
search_box.send_keys('selenium')               # Type in selenium.
search_box.send_keys(Keys.RETURN)              # Press ENTER.
"""