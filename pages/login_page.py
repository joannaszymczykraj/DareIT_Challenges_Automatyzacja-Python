from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//span[@class='MuiButton-label']"
    header_scouts_panel_xpath = "//h5[contains(@class,'gutterBottom')]"
    login_label_xpath = "//label[@id='login-label']"
    password_label_xpath = "//label[@id=’password-label’]"
    reminder_password_label_xpath = "//a[text()='Remind password']"
    language_change_button_xpath = "//div[contains(@class,'MuiSelect')]"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    header_of_box = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title



