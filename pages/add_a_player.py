import time
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    expected_title_add_player = "Add player"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title_add_player
        time.sleep(5)
