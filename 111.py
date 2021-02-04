# 创建一个字典，包装相应的启动参数
import random
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(3)
driver.find_element_by_xpath('//*[@content-desc="关闭对话框"]').click()
# driver.press_keycode(4)
sleep(1)
driver.find_element_by_xpath('//*[@text="我"]').click()
driver.find_element_by_id('com.yunmall.lc:id/ymtitlebar_left_btn_image').click()




driver.find_element_by_xpath('//*[@text="地址管理"]').click()
# driver.find_element_by_xpath('//*[@text="新增地址"]').click()
# driver.find_element_by_id('com.yunmall.lc:id/address_province').click()
# ret = driver.find_elements_by_id('com.yunmall.lc:id/area_title')
# num = random.randint(0,len(ret)-1)
# ret[num].click()
# ret1 = driver.find_elements_by_id('com.yunmall.lc:id/area_title')
# num1 = random.randint(0,len(ret1))
# ret1[num1].click()
# ret2 = driver.find_elements_by_id('com.yunmall.lc:id/area_title')
# num2 = random.randint(0,len(ret1))
# ret2[num2].click()
# while True:
#     try:
#         ret = driver.find_elements_by_id('com.yunmall.lc:id/area_title')
#         num = random.randint(0, len(ret) - 1)
#         ret[num].click()
#     except:
#         break


# ret = driver.find_elements_by_id('com.yunmall.lc:id/receipt_name')
# print(type(ret[0]))

print('111')



