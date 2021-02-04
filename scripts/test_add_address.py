from time import sleep

import pytest
from appium import webdriver

from base.base_analyze import analyze_data
from page.add_address_page import AddAddressPage
from page.address_page import AddressPage
from page.home_page import HomePage
from page.my_page import MyPage


class TestAddAddress:

    def setup(self):
        # 创建一个字典，包装相应的启动参数
        desired_caps = dict()
        # 需要连接的手机的平台(不限制大小写)
        desired_caps['platformName'] = 'Android'
        # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
        desired_caps['platformVersion'] = '5.1'
        # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # 需要启动的程序的包名
        desired_caps['appPackage'] = 'com.yunmall.lc'
        # 需要启动的程序的界面名
        desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
        # 告诉appium不重置应用
        desired_caps['noReset'] = True
        # 支持中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 连接appium服务器
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.home_page = HomePage(self.driver)
        self.my_page = MyPage(self.driver)
        self.address_page = AddressPage(self.driver)
        self.add_address_page = AddAddressPage(self.driver)


    def teardown(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_data('address_data', 'test_add_address_case'))
    def test_add_address_case(self, args):
        name = args['name']
        phone = args['phone']
        address = args['address']
        postcode = args['postcode']
        # 关闭更新
        self.home_page.click_close_update()
        # 点击我的
        self.home_page.click_my_button()
        # 点击设置
        self.my_page.click_set_button()
        # 点击地址管理
        self.my_page.click_adress_button()
        # 点击新增地址
        self.address_page.click_add_address()
        # 点击输入姓名
        self.add_address_page.input_name(name)
        # 点击输入手机号码
        self.add_address_page.input_phone(phone)
        # 点击省市区
        self.add_address_page.click_province()
        # 点击添加输入详细地址
        self.add_address_page.input_address(address)
        # 点击输入邮编
        self.add_address_page.input_postcode(postcode)
        # 点击选择默认地址
        self.add_address_page.click_default_address()
        # 点击保存
        self.add_address_page.click_save()
        # 断言 新增默认地址是否是预期
        assert self.address_page.get_default_name_phone_text() == '%s  %s' %(name, phone)

        #断言获取全部的姓名和手机号
        # na = '%s  %s' %(name, phone)
        # assert na in self.address_page.get_names()


