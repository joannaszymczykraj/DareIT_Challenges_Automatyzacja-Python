from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    main_page_button_xpath = "//span[text()='Main page']"
    players_button_xpath = "//span[text()='Players']"
    player_name_button_xpath = "//span[contains(@class,'body1') and text()='Test Test']"
    matches_button_xpath = "//span[text()='Matches']"
    reports_button_xpath = "//span[text()='Reports']"
    language_polish_button_xpath = "//span[text()='Polski']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    side_menu_box_xpath = "//div[contains(@class, 'jss16')]"
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    match_at_home_button_xpath = "//span[text()='Match at home']"
    match_out_home_button_xpath = "//span[text()='Match out home']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[contains(@class,'containedSecondary')]"
    adding_match_player_name_field_xpath = "//span[contains(@class,'MuiCardHeader')]"
    adding_match_menu_box_xpath = "//main[@class='jss2 jss113']"

    pass