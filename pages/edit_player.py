import time
from pages.base_page import BasePage


class EditPlayer(BasePage):
    edit_player_url = "https://scouts-test.futbolkolektyw.pl/players/edit"
    edit_player_expected_title = 'Edit player Joanna Testowa'
    add_player_title_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/div[1]/div[2]/span[1]"  # dodane
    add_player_text = 'Joanna Testowa'  # dodane

    def edit_player_title_of_page(self):
        assert self.get_page_title(self.edit_player_url) == self.edit_player_expected_title
        time.sleep(15)
