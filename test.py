# -*- coding: gb18030 -*-
# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep

ServerUrl = 'http://127.0.0.1:4723/wd/hub'


desired_caps = {
    'noReset': True,  # ����APP����Ҫ���app���ԭ�е�����
    'fullReset' : False,
    'platformName': 'Android',
    'platformVersion': '8.0',
    'unicodeKeyboard': True,  # ʹ��Unicode���뷨
    'resetKeyboard': True,  # �������뷨����ʼ״̬
    'deviceName': 'WTKDU16C07002694',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
}
driver = webdriver.Remote(ServerUrl, desired_caps)

sleep(3)
driver.find_element_by_id("com.tencent.mm:id/e3x").click()
sleep(3)
driver.find_element_by_id("com.tencent.mm:id/al_").send_keys(u"���")
