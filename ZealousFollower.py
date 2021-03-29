from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class ZealBot():
    def __init__(self, email, password, driver_path):
        self.user_email = email
        self.user_password = password
        self.driver = webdriver.Chrome(driver_path)

    def monkey_see(self, url, email, password, user):
        driver = self.driver
        driver.get(url)

        time.sleep(5)

        email_field = driver.find_element_by_xpath('//input[@name="username"]')
        email_field.send_keys(email)

        password_field = driver.find_element_by_xpath('//input[@name="password"]')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

        search_box = driver.find_element_by_tag_name('input')
        search_box.send_keys(user)

        time.sleep(2)

        search_box.send_keys(Keys.RETURN)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)


    def monkey_do(self):
        driver = self.driver
        main_handle = driver.current_window_handle

        followers_link = driver.find_element_by_partial_link_text('followers')
        followers_link.click()

        time.sleep(5)

        pop_up_handle = driver.current_window_handle

        while pop_up_handle:

            followers_list = driver.find_elements_by_link_text('Follow')

            for follower in followers_list:
                follower.click()
                time.sleep(2)

driver = webdriver.Chrome('/Users/Jope/development/chromedriver')

driver.get('https://google.com')