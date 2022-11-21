# -*- encoding=utf8 -*-
__author__ = "PAICS"
from airtest.core.api import *
from page.page_base import PageBase
from utils.keys_util import KeysUtil
from utils.json_util import JsonUtil


class PageNote:

    # 定位
    note_logo_loc = "tpl_note_logo.png", (-0.338, 0.27) # 记事本任务栏图标
    note_replace_all_loc = "tpl_note_replace_all.png", (0.26, 0.006) # 全部替换按钮

    # 操作
    def touch_note_logo_loc(self):
        PageBase().base_touch_loc(self.note_logo_loc)  # 点击任务栏的记事本图标

    def touch_note_replace_all_loc(self):
        PageBase().base_touch_loc(self.note_replace_all_loc)  # 点击全部替换按钮

    # 组合操作
    def note_replace(self, text_find, text_replace):
        """
         1.点击任务栏的记事本图标
         2. 按下替换按键 crtl+h,呼出“替换”对话框
         3. 清空查找内容并输入查找内容
         4. 按下tab键定位到替换为输入框
         6. 清空替换内容并输入替换内容
         7. 点击全部替换
         8. 按下替换按键 crtl+s，保存内容
        """
        self.touch_note_logo_loc() #  点击任务栏的记事本图标
        KeysUtil().keyevent_ctrl_h()  # 按下替换按键 crtl+h,呼出“替换”对话框
        PageBase().base_text(text_find)  # 清空查找内容并输入查找内容
        KeysUtil().keyevent_tab()  # 按下tab键定位到替换为输入框
        PageBase().base_text(text_replace)  # 清空替换内容并输入替换内容
        self.touch_note_replace_all_loc() # 点击全部替换
        sleep(1.0)
        KeysUtil().keyevent_ctrl_s()  # 按下替换按键 crtl+s，保存内容

    # 将文件的数据初始化
    def note_data_initialization(self, filename_read, filename_write):
        # Keys().keyevent_win()
        # self.touch_note_logo_loc()  # 点击任务栏的记事本图标
        # Keys().keyevent_esc()  # 如果当前界面有其他弹窗，先将其关闭
        data = JsonUtil().read_json(filename_read)  # 读取json数据，返回data
        JsonUtil().write_json(filename_write, data) # 写入json数据
