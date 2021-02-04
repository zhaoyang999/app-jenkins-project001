from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MyPage(BaseAction):
    set_button = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'
    address_button = By.XPATH, '//*[@text="地址管理"]'


    def click_set_button(self):
        self.click(self.set_button)

    def click_adress_button(self):
        self.click(self.address_button)

