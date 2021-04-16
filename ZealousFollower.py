from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ZealBot:
    def __init__(self, email, password, driver_path):
        self.user_email = email
        self.user_password = password
        self.driver = webdriver.Chrome(driver_path)
        
        
    # this function logs into instagram and locates a desired user
    def monkey_see(self, url, email, password, user):
        driver = self.driver
        driver.get(url)
        
        # time.sleep improves likelihood of driver finding elements
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
        
        # sending RETURN here helps avoid finding, clicking a search button
        search_box.send_keys(Keys.RETURN)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

    # picking up where the previous left off, this function automates following user's followers
    def monkey_do(self):

        driver = self.driver
        
        # open followers window
        followers_link = driver.find_element_by_partial_link_text('followers')
        followers_link.click()

        time.sleep(2)

        counter = 0
        follower_window = driver.find_element_by_xpath('//div[@class="isgrP"]')

        # scrolls down to bottom of followers window, assuming sixty downward scrolls brings full view
        while counter < 60:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                  follower_window)
            # sleeping here gives the driver some breathing room
            time.sleep(1)
            counter += 1

        follow_buttons = driver.find_elements_by_css_selector('li button')

        for button in follow_buttons:
            if button.text == 'Follow':
                button.click()
                # sleeping helps to appear a little more human
                time.sleep(3)
            else:
                # prevents clicking on an account bot's presently following
                continue
        
        # admire what your hubris has wrought 
        time.sleep(10)

        driver.close()


