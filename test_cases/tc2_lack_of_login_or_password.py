import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import BasePage, Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestLoginPage2(unittest.TestCase):
    driver_service = None
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() # nie mam pojęcia dlaczego to  raz działa a raz nie działa!
        user_login.click_on_the_sign_in_button()
        time.sleep(20)

    @classmethod
    def tearDown(self):
        self.driver.quit()
