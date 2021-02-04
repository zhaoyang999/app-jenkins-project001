from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    close_update_button = By.XPATH, '//*[@content-desc="关闭对话框"]'
    my_button = By.XPATH, '//*[@text="我"]'



    def click_close_update(self):
        self.click(self.close_update_button)

    def click_my_button(self):
        self.click(self.my_button)

