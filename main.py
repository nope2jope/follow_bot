import os
import ZealousFollower

EMAIL_ADDR = os.environ['ENV_USER_EMAIL']
PASSWORD = os.environ['ENV_USER_PW']

DRIVER_PATH = os.environ['ENV_DRIVER_PATH']

to_emulate = 'mucasloser'

enthusiastic_follower = ZealousFollower.ZealBot(email=EMAIL_ADDR, password=PASSWORD, driver_path=DRIVER_PATH)

enthusiastic_follower.monkey_see(url='https://www.instagram.com/', email=EMAIL_ADDR, password=PASSWORD, user=to_emulate)

enthusiastic_follower.monkey_do()