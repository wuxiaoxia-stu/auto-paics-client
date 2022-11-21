# -*- encoding=utf8 -*-
__author__ = "PAICS"

from time import sleep
from page.page_base import PageBase


class PagePaicsLogin(PageBase):
    """
    用户登录页面
    第1个值表示图片的名称，第2个值表示点击的坐标，第3个值表示滑动的比例
    """
    # login_admin_loc = "tpl_paics_user_admin.png", (-0.248, -0.012)   # 管理员头像图像
    # login_password_loc = "tpl_paics_password_img.png", (-0.277, -0.019), vector   # 密码图形图像
    # 定位
    def login_admin_loc(self):  # 定位停止检查按钮
        pic_filename = "tpl_paics_user_admin.png"
        pos = (-0.248, -0.012)
        return pic_filename, pos

    def login_password_loc(self):  # 定位停止检查按钮
        pic_filename = "tpl_paics_password_img.png"
        pos = (-0.277, -0.019)
        vector = (-0.277, -0.019)
        return pic_filename, pos, vector

    # 操作
    def touch_login_admin_loc(self):
        self.base_touch_loc(self.login_admin_loc())  # 点击管理员头像

    def swipe_login_password_loc(self):
        self.base_swipe(self.login_password_loc())   # 滑动密码，输入密码

    # 组合业务
    def login(self):
        self.touch_login_admin_loc()  # 点击管理员头像
        sleep(1)  # 等待1s
        self.swipe_login_password_loc()  # 输入密码
        sleep(1)  #等待1s


