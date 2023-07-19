import time
from selenium import webdriver
from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_header_xpath = "//h6[text()='Scouts Panel']"
    main_page_button_xpath = "//span[text()='Main page']"
    players_button_xpath = "//span[text()='Players']"
    language_polish_button_xpath = "//span[text()='Polski']"
    sing_out_button_xpath = "//span[text()='Sign out']"
    players_count_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]"
    matches_count_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]"
    reports_count_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[3]"
    events_count_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[4]"
    scouts_panel_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[3]/div[1]/div[1]"
    shortcuts_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[1]]"
    activity_box_xpath = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[3]/div[3]/div[1]"
    add_player_button_xpath = "//span[text()='Add player']"
    dev_team_contact_button_xpath = "//span[text()='Dev team contact']"
    logo_scouts_panel_xpath = "//div[@title='Logo Scouts Panel']"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title_dashboard = "Scouts panel"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.dev_team_contact_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title_dashboard

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)