import os
import ZealousFollower

EMAIL_ADDR = os.environ['ENV_USER_EMAIL']
PASSWORD = os.environ['ENV_USER_PW']
SITE_URL = os.environ['ENV_SITE_URL']
DRIVER_PATH = os.environ['ENV_DRIVER_PATH']
MY_HER0 = os.environ['ENV_USER_IDOL']

enthusiast = ZealousFollower.ZealBot(email=EMAIL_ADDR, password=PASSWORD,
                                                driver_path=DRIVER_PATH)

enthusiast.monkey_see(url=SITE_URL, email=EMAIL_ADDR,
                                 password=PASSWORD, user=MY_HER0)
enthusiast.monkey_do()

