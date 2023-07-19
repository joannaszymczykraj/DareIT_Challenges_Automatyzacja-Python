import time

from pages.base_page import BasePage


class RemindPassword(BasePage):
    remind_password_header_xpath = "//h5[contains(text(),'Remind password')]"
    email_field_xpath = "//input[@name='email']"
    send_button_xpath = "//button[@type='submit']"

    expected_title_remind_password = "Remind password"
    remind_password_url = 'https://scouts-test.futbolkolektyw.pl/en/remind'


    def title_of_page(self):
        assert self.get_page_title(self.remind_password_url) == self.expected_title_remind_password
        time.sleep(10)

    def type_in_remind_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def click_on_send_button(self):
        self.click_on_the_element(self.send_button_xpath)




