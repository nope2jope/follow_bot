import os
import ZealousFollower

#establish constants, reference environmental variables
EMAIL_ADDR = os.environ['ENV_USER_EMAIL']
PASSWORD = os.environ['ENV_USER_PW']
SITE_URL = os.environ['ENV_SITE_URL']
DRIVER_PATH = os.environ['ENV_DRIVER_PATH']
MY_HER0 = os.environ['ENV_USER_IDOL']

#initialize object from imported class 
enthusiast = ZealousFollower.ZealBot(email=EMAIL_ADDR, password=PASSWORD,
                                                driver_path=DRIVER_PATH)

#sign into instagram, search and click through to target follower list
enthusiast.monkey_see(url=SITE_URL, email=EMAIL_ADDR,
                                 password=PASSWORD, user=MY_HER0)

#start following
enthusiast.monkey_do()

