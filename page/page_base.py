# -*- encoding=utf8 -*-

__author__ = "PAICS"

from airtest.core.api import *
import os
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

class PageBase:

    def base_get_pic_path(self, pic_name):
        """
        作用：获取图片路径
        """
        pic_path = os.getcwd() + '/resources/' + pic_name
        return pic_path

    def base_exists(self, pic_filename):
        """
        作用：点击指定元素
        loc: 元素,包括图片的位置和点击图片的坐标
        record_pos： 坐标
        resolution： 分辨率,默认设定为1920,1080
        """
        return exists(Template(self.base_get_pic_path(pic_filename)))

    def base_touch_loc(self, pic_filename, pos, resolution=(1920, 1080)):
        """
        作用：点击指定元素
        loc: 元素,包括图片的位置和点击图片的坐标
        record_pos： 坐标
        resolution： 分辨率,默认设定为1920,1080
        """
        if exists(Template(self.base_get_pic_path(pic_filename))):
            touch(Template(self.base_get_pic_path(pic_filename), record_pos=pos, resolution=resolution))
            return True
        else:
            return False
        
    def base_text(self, input_text):
        """
        作用：先清空输入框的内容再输入新内容
        :param input_text:
        """
        text("")  # 清空内容
        text(input_text)  # 输入内容

    def base_swipe(self, pic_filename, pos, vector, resolution=(1920, 1080)):
        """
        作用：滑动
        vector: 滑动的比例
        :param pic_filename: 图片名称
        :param pos: 图片坐标
        :param vector: 滑动比例
        :param resolution: 分辨率
        """
        swipe(Template(self.base_get_pic_path(pic_filename), record_pos=pos, resolution=resolution), vector=vector)

    def base_log(self, message):
        """
        输出airtest中的log
        :param message: 输出日志信息
        :return:
        """
        log(message, timestamp=time.time())

    # os.system(r'notepad.exe I:\bd\AirtestIDE-win-1.2.13\paics\autopaics\data\VideoPathList.json')
    # os.system(r'notepad.exe %s/data/VideoPathList.json' % self.project_path)  # 用记事本将VideoPathList.json文件打开