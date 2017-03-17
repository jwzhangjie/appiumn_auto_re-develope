__author__ = 'shikun'
# 查找元素的方式
class GetVariable(object):
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    SELENIUM = "selenium"
    APPIUM = "appium"
    ANDROID = "android"
    IOS = "ios"
    IE = "ie"
    FOXFIRE = "foxfire"
    CHROME = "chrome"
    SELENIUM_APPIUM = "appium"
    DRIVER = ""

    OPERATION_TYPE_CLICK = "click"
    OPERATION_TYPE_SWIPE_LEFT = "swipeLeft"
    OPERATION_TYPE_WAITE = "wait"
    OPERATION_TYPE_SEND_KEYS = "send_keys"
    OPERATION_TYPE_TAP = "tap"
    # OPERATION_TYPE_FIND_STR = "find_str"

    WAIT_TIME = 5

    # 本地存储记录所有的case情况的路径
    REPORT_INFO_PATH = "d:/info.txt"
    REPORT_INIT = "d:/init.txt"
    REPORT_COLLECT_PATH = "d:/collect.txt"
    # 存放crash的json文件名
    CRASH_LOG_PATH = "d:/crash.txt"
    # my server
    HOST = '127.0.0.1'
    PORT = 8088

    # 协议
    PROTOCOL = "http://"
    # apache器的地址，开发可以在这个上面下载异常日志
    APACHE_PATH = "D:/log/"
    # 截图地址
    SCREEN_IMG_PATH = "D:/img/"

