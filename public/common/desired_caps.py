# -*- coding: gb18030 -*-
# -*- coding: utf-8 -*-
from appium import webdriver

ServerUrl = 'http://127.0.0.1:4723/wd/hub'


def desired():
    desired_caps = {
        'noReset': True,  # ����APP����Ҫ���app���ԭ�е�����
        'fullReset' : False,
        'platformName': 'Android',
        'platformVersion': '5.1',
        # 'unicodeKeyboard': True,  # ʹ��Unicode���뷨
        'resetKeyboard': True,  # �������뷨����ʼ״̬
       #'deviceName': 'WTKDU16C07002694',
        'deviceName':'127.0.0.1:62001',
        'appPackage': 'com.upqing.sunflower',
        # 'appPackage': 'com.tencent.mm',
        'appActivity': '.MainActivity',
        # 'appActivity': '.ui.LauncherUI'

    }
    driver = webdriver.Remote(ServerUrl, desired_caps)
    return driver


# ����
if __name__ == '__main__':
    des = desired()
