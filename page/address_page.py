from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressPage(BaseAction):
    add_address_button = By.XPATH, '//*[@text="新增地址"]'
    default_name_phone = By.ID, 'com.yunmall.lc:id/receipt_name'

    def click_add_address(self):
        self.click(self.add_address_button)

    def get_default_name_phone_text(self):
        return self.get_text(self.default_name_phone)

    # def get_names(self):
    #     li = []
    #     ret = self.find_elements(self.default_name_phone)
    #     for i in ret:
    #         text = i.text
    #         li.append(text)
    #         print(li)
    #
    #     return li


