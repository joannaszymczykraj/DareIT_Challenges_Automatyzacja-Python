from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='login']"
    sign_in_button_xpath = "//span[@class='MuiButton-label']"
    header_scouts_panel_xpath = "//h5[contains(@class,'gutterBottom')]"
    login_label_xpath = "//label[@id='login-label']"
    password_label_xpath = "//label[@id=’password-label’]"
    reminder_password_label_xpath = "//a[text()='Remind password']"
    language_change_button_xpath = "//div[contains(@class,'MuiSelect')]"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
