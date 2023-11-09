# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver import ActionChains
from logger import set_info
from time import sleep


class Test:
    # 静态方法
    # @staticmethod
    def __init__(self, max: bool = False):
        """ 
        @max:最大化状态
        :param max:布尔值类型，True为窗口的最大化显示
        """
        # chromedrive = r'D:/Bencky/Software/CentBrowser/soft/CentBrowser/Application/chromedriver.exe'
        chromedrive = r'chromedriver.exe'
        self.chrome_drive = Service(chromedrive)
        # 选项配置
        self.chrome_option = Options()
        option = {
            'HEAD': '--headless',
            'GPU': '--disable-gpu',
            'MAX': '--start-maximized',
            'CERTIFICATE': '--ignore-certificate-errors',
            'SSL': '--ignore-ssl-errors',
            'exclude': {
                'NAME': 'excludeSwitches',
                'CONFIG': ['enable-automation', 'enable-logging']
            },
            'detach': {'NAME': 'detach', 'CONFIG': True}
        }
        ename = option['exclude']['NAME']
        ecfg = option['exclude']['CONFIG']
        dname = option['detach']['NAME']
        dcfg = option['detach']['CONFIG']
        # self.chrome_option.add_argument(option[HEAD])           # 无界面模式
        self.chrome_option.add_argument(option['GPU'])            # 禁用GPU
        self.chrome_option.add_argument(option['CERTIFICATE'])    # 处理证书错误问题
        self.chrome_option.add_argument(option['SSL'])            # 处理SSL错误问题
        # self.chrome_option.add_argument(option[MAX])            # 最大化运行
        self.chrome_option.add_argument(
            option['MAX']) if max == True else max == False
        self.chrome_option.add_experimental_option(ename, ecfg)   # 自动测试软件的控制提示
        self.chrome_option.add_experimental_option(dname, dcfg)   # 不自动关闭浏览器
        self.drive = webdriver.Chrome(
            service=self.chrome_drive, options=self.chrome_option)

        print('初始化成功，最大化状态：{}.'.format(max))
        # return self.drive

    # 定位方法
    def loc_el(self, loctype='', value=''):
        """
        @loctype：元素类型
        @value：值
        """
        el = None
        if loctype == 'id':
            el = self.drive.find_element(By.ID, value)
        if loctype == 'name':
            el = self.drive.find_element(By.NAME, value)
        if loctype == 'class_name':
            el = self.drive.find_element(By.CLASS_NAME, value)
        if loctype == 'tag_name':
            el = self.drive.find_elements(By.TAG_NAME, value)
        if loctype == 'link':
            el = self.drive.find_element(By.LINK_TEXT, value)
        if loctype == 'css':
            el = self.drive.find_element(By.CSS_SELECTOR, value)
        if loctype == 'partial_link':
            el = self.drive.find_element(By.PARTIAL_LINK_TEXT, value)
        if loctype == 'xpath':
            el = self.drive.find_element(By.XPATH, value)
        return el if el else None

    # 输入内容
    def input(self, loctype='', value='', data=''):
        """
        @loctype：元素类型
        @value：值
        @data：输入的数据
        """
        self.loc_el(loctype, value).send_keys(data)

    # 点击
    def click(self, loctype='', value=''):
        self.loc_el(loctype, value).click()
        return self

    # 组合键（基于元素）
    def keys_comp(self, loctype='', value='', key_down=Keys.CONTROL, *keys):
        """
        发送组合键（基于元素），如：点击input输入框后Ctrl+A（全选）

        示例：drive.keys_comp('xpath', '//*[@id="app"]/input',Keys.CONTROL,'a')
        @*keys：可以接收多个参数
        """
        element = self.loc_el(loctype, value)
        action = ActionChains(self.drive)
        action.key_down(key_down, element).send_keys(keys).perform()

    # 组合键（不基于元素）
    def keys_com(self, key_down=Keys.CONTROL, *keys):
        """
        发送组合键（不基于元素），如：Ctrl+A（全选）

        示例：drive.keys_com(Keys.CONTROL,'a')
        @*keys：可以接收多个参数
        """
        action = ActionChains(self.drive)
        action.key_down(key_down).send_keys(*keys).perform()

    # 功能键（不基于元素）
    def keys_fun(self, *key):
        """
        发送功能键（不基于元素），如：Tab（下一个制表位）
        """
        ActionChains(self.drive).send_keys(*key).perform()

    # 功能键（基于元素）
    def keys_func(self, loctype='', value='', key=Keys.CONTROL):
        """
        发送功能键（基于元素），如：Ctrl（Keys.CONTROL），←←（keys.LEFT*2）
        """
        self.loc_el(loctype, value).send_keys(key)

    # 普通按键（基于元素）
    def keys_normal(self, loctype='', value='', data=''):
        """
        发送普通按键（基于元素），与input()方法相同
        """
        self.input(loctype, value, data)

    # 普通按键（不基于元素）
    def keys(self, *keys):
        """
        发送普通按键（不基于元素）
        """
        ActionChains(self.drive).send_keys(*keys).perform()

    # 获取元素文本内容
    def get_text(self, loctype, value):
        """
        获取元素的文本内容，如：<a href="http://news.baidu.com">新闻</a>

        获取：drive.get_text('xpath','//*[@href="http://news.baidu.com"]')
        """
        # print(self.loc_el(loctype, value).text)
        return self.loc_el(loctype, value).text

    # 获取元素的指定属性
    def get_attr(self, loctype, value, attr='value'):
        """
        获取元素的指定属性，如：<a href="http://news.baidu.com">新闻</a>

        获取：drive.get_attr('xpath','//*[@href="http://news.baidu.com"]','value')
        """
        # print(self.loc_el(loctype, value).get_attribute(attr))
        return self.loc_el(loctype, value).get_attribute(attr)

    # 悬浮
    def hover(self, loctype, value):
        sleep(1)
        ActionChains(self.drive).move_to_element(
            self.loc_el(loctype, value)).perform()
        sleep(3)

    # 访问页面
    def get(self, url: str):
        """
        @url：访问网址
        """
        self.drive.get(url)
        return self.drive

    # 强制等待
    def sleep(self, tm=3, msg='等待', show=True) -> None:
        if type(tm) == 'int':
            if (show):
                for i in range(tm):
                    # print(f'{msg}：{i+1}秒')
                    set_info(f'{msg}：{i+1}秒')
                    sleep(1)
            else:
                # print(f'{msg}{tm}秒')
                set_info(f'{msg}{tm}秒')
                sleep(tm)
        else:  # 毫秒延迟
            # print(f'{msg}{tm}秒')
            set_info(f'{msg}{tm}秒')
            sleep(tm)

    # 显示等待
    def webDriverWait(self, timeout, poll_frequency=0.5):
        return WebDriverWait(self.drive, timeout, poll_frequency)


        # from selenium.webdriver.support.wait import WebDriverWait

        # element = WebDriverWait(self.drive, timeout).until(lambda x: x.loc_el(By.ID, "someId"))

        # is_disappeared = WebDriverWait(self.drive, 30, 1, (ElementNotVisibleException)).until_not(
        #     lambda x: x.find_element(By.ID, "someId").is_displayed())

def test():
    # 初始化配置
    drive = Test(1)
    # 访问地址
    baseurl = 'http://192.168.0.121:80/#/'
    driver = drive.get(baseurl)

