# -*- encoding=utf8 -*-
__author__ = "PAICS"

from time import sleep
import allure
from page.page_base import PageBase
from airtest.core.api import *


@allure.feature('测试实时检查PagePaics功能模块')  # 标注主要功能模块
class PagePaics(PageBase):

    # 定位
    def paics_logo_loc(self):  # 定位paics_logo图标， 第1个值表示图片的名称，第2个值表示点击的坐标，第3个值表示滑动的比例（可以为空）
        pic_filename = "tpl_paics_logo.png"
        pos = (-0.262, 0.27)
        return pic_filename, pos

    def paics_letterA_loc(self):  # 定位A按钮
        pic_filename = "tpl_paicsA.png"
        pos = (-0.214, -0.021)
        return pic_filename, pos

    def paics_letterB_loc(self):  # 定位B按钮
        pic_filename = "tpl_paicsB.png"
        pos = (0.011, -0.02)
        return pic_filename, pos

    def paics_closed_loc(self):   # 定位关闭按钮
        pic_filename = "tpl_paics_closed.png"
        pos = (0.294, -0.236)
        return pic_filename, pos

    def paics_stop_loc(self):  # 定位停止检查按钮
        pic_filename = "tpl_paics_stop.png"
        pos = (-0.45, 0.12)
        return pic_filename, pos

    # 操作
    @allure.step('点击任务栏下的paics_logo图标')
    def touch_paics_logo(self):
        # pic_filename, pos = self.paics_logo_loc()
        # print(pic_filename, pos)
        try:
            assert self.base_touch_loc(*self.paics_logo_loc())  # 点击任务栏下的paics_logo图标,需要先对返回的元祖数据进行解包才能正常填充参数，*表示拆包
            self.base_log("点击任务栏下的paics_logo图标成功")
            return True
        except Exception as e:
            self.base_log(e)  # 输出日志
            return False

    @allure.step('点击A按钮进入实时检查')
    def touch_paics_letterA_loc(self):
        try:
            assert self.base_touch_loc(*self.paics_letterA_loc()) # 点击A按钮进入实时检查
            self.base_log("点击A按钮成功")
            return True
        except Exception as e:
            self.base_log(e)
            return False


    @allure.step('点击B进行国家级中孕实时检查')
    def touch_paics_letterB_loc(self):
        try:
            assert self.base_touch_loc(*self.paics_letterB_loc())  # 点击B进行国家级中孕实时检查
            self.base_log("点击B按钮成功")  # 输出日志
            return True
        except Exception as e:
            self.base_log(e)
            return False

    @allure.step('点击关闭按钮')
    def touch_paics_closed_loc(self):
        try:
            assert self.base_touch_loc(*self.paics_closed_loc())  # 点击关闭按钮
            self.base_log("点击关闭按钮成功")  # 输出日志
            return True
        except Exception as e:
            self.base_log(e)
            return False

    @allure.step('点击停止检查')
    def touch_paics_stop_loc(self):
        try:
            self.base_touch_loc(*self.paics_stop_loc())  # 点击停止检查
            self.base_log("点击停止检查按钮成功")  # 输出日志
            return True
        except Exception as e:
            self.base_log(e)
            return False

    # 组合操作
    # 点击A按钮进入实时检查，手动点击停止检查
    def paicsA_stop(self, video_length):
        """
        1.点击任务栏的paics图标
        2.点击A进行实时检查
        3. 等待视频的时长
        4. 点击关闭按钮
        5. 按下RWIN键
        """
        touch_paics_letterA = self.touch_paics_letterA_loc()  # 点击A按钮进入实时检查
        sleep(float(video_length))  # 等待视频的时长
        touch_paics_stop = self.touch_paics_stop_loc()  # 点击停止检查
        touch_paics_closed = self.touch_paics_closed_loc()  # 点击关闭按钮
        try:
            assert touch_paics_letterA & touch_paics_stop & touch_paics_closed
            return True
        except:
            self.base_log("点击A按钮进入实时检查，手动点击停止检查失败")
            return False
        # print("测试国家级早孕产筛长视频3s")

    # 点击B按钮进入实时检查，手动点击停止检查
    def paicsB_stop(self, video_length):
        """
        1.点击任务栏的paics图标
        2.点击B进行实时检查
        3. 等待视频的时长
        4. 点击停止检查
        5. 点击关闭按钮
        6. 按下WIN键
        """
        self.touch_paics_letterB_loc()  #点击B进行国家级中孕实时检查
        sleep(float(video_length))  # 等待视频的时长
        # print(video_length)
        self.touch_paics_stop_loc()  # 点击停止检查
        self.touch_paics_closed_loc()        # 点击关闭按钮
        # print("测试国家级中孕产筛长视频3s")

    # 点击A按钮进入实时检查，自动停止检查
    def paicsA_auto(self, video_length):
        """
        1.点击任务栏的paics图标
        2.点击A进行国家级早孕实时检查
        3. 等待视频的时长
        4. 点击关闭按钮
        5. 按下RWIN键
        """
        self.touch_paics_letterA_loc()  # 点击A按钮进入实时检查
        sleep(float(video_length))  # 等待视频的时长
        # sleep(1.5)  # 等待1.5秒
        self.touch_paics_closed_loc()  # 点击关闭按钮

    # 点击B按钮进入实时检查，自动停止检查
    def paicsB_auto(self, video_length):
        """
        1.点击任务栏的paics图标
        2.点击B进行国家级中孕实时检查
        3. 等待视频的时长
        4. 点击关闭按钮
        5. 按下RWIN键
        """
        self.touch_paics_letterB_loc()  # 点击B进行国家级中孕实时检查
        sleep(float(video_length))  # 等待视频的时长
        # sleep(1.5)  # 等待1.5秒
        self.touch_paics_closed_loc()  # 点击关闭按钮

    # 初始化
    @allure.story('paics初始化,返回系统首页')
    def paics_initialization(self):
        """
        1、如果找不到任务栏的paics_logo，那么启动它
        2、如果找不到A/B/C按钮，尝试依次点击停止检查，关闭按钮
        """
        self.touch_paics_logo()  # 点击任务栏paics的logo
        existsB = self.base_exists(self.paics_letterB_loc()[0])  # 判断客户端页面是否存在B按钮
        if not existsB:
            if self.base_exists(self.paics_stop_loc()[0]):  # 如果存在停止检查按钮，点击停止检查按钮，再点击关闭按钮
                self.touch_paics_stop_loc()
                self.touch_paics_closed_loc()
            elif self.base_exists(self.paics_closed_loc()[0]):  # 如果存在关闭按钮，点击关闭按钮
                self.touch_paics_closed_loc()



