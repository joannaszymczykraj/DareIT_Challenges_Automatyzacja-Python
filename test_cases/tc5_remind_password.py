import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import BasePage, Dashboard
from pages.login_page import LoginPage
from pages.remind_password import RemindPassword
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestRemindPassword(unittest.TestCase):
    driver_service = None
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.click_on_remind_password_button()
        time.sleep(10)
        remind_password_page = RemindPassword(self.driver)
        remind_password_page.title_of_page()
        remind_password_page.type_in_remind_email('user01@getnada.com')
        time.sleep(5)
        remind_password_page.click_on_send_button()
        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()
