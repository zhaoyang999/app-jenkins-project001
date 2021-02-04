import random
from time import sleep

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddAddressPage(BaseAction):

    edit_receipt_name = By.ID, 'com.yunmall.lc:id/address_receipt_name'
    edit_receipt_phone = By.ID, 'com.yunmall.lc:id/address_add_phone'
    edit_address = By.ID, 'com.yunmall.lc:id/address_detail_addr_info'
    edit_postcode = By.ID, 'com.yunmall.lc:id/address_post_code'
    default_address_button = By.ID, 'com.yunmall.lc:id/address_default'
    save_button = By.XPATH, '//*[@text="保存"]'
    choice_province_button = By.ID, 'com.yunmall.lc:id/address_province'
    # province_button = By.XPATH, '//*[@text="北京市"]'
    # province2_button = By.ID, 'com.yunmall.lc:id/area_title'
    # district_button = By.XPATH, '//*[@text="东城区"]'
    province_lable = By.ID, 'com.yunmall.lc:id/area_title'

    def input_name(self, text):
        self.input(self.edit_receipt_name, text)

    def input_phone(self, text):
        self.input(self.edit_receipt_phone, text)

    def click_province(self):
        # self.click(self.chonice_province_button)
        # self.click(self.province_button)
        # sleep(1)
        # self.click(self.province2_button)
        # self.click(self.district_button)
        self.click(self.choice_province_button)
        while True:
            try:
                ret = self.driver.find_elements_by_id('com.yunmall.lc:id/area_title')
                num = random.randint(0, len(ret) - 1)
                ret[num].click()
            except:
                break

    def input_address(self, text):
        self.input(self.edit_address, text)

    def input_postcode(self, text):
        self.input(self.edit_postcode, text)

    def click_default_address(self):
        self.click(self.default_address_button)

    def click_save(self):
        self.click(self.save_button)
        




