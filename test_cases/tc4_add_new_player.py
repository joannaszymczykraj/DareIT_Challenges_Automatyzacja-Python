import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.edit_player import EditPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayer2(unittest.TestCase):
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

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(25)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(20)
        dashboard_page.click_on_the_add_player_button()
        time.sleep(25)
        add_player = AddAPlayer(self.driver)
        add_player.title_of_page()
        add_player.type_in_name('Joanna')
        add_player.type_in_surname('Testowa')
        add_player.type_in_age('01.01.2000')
        add_player.type_in_main_position('Goalkeeper')
        add_player.click_on_submit_button()
        # edit_player = EditPlayer(self.driver)
        # edit_player.get_page_title() # zly url?
        time.sleep(20)

        # add_player.assert_add_player() #dodane
        time.sleep(15)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()
