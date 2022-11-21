# -*- encoding=utf8 -*-

__author__ = "PAICS"

from airtest.core.api import *
import os


# 封装需要用到的模拟按键key
class KeysUtil:

    def keyevent_win(self):
        """
        作用：模拟按下win按键,名称为{VK_RWIN}
        keyname: 键的名称，比如：{VK_ADD}表示“+”   参考： https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
        """
        keyevent("{VK_RWIN}")

    def keyevent_tab(self):
        """
        作用：模拟按下tab按键,名称为{VK_TAB}
        """
        keyevent("{VK_TAB}")

    def keyevent_ctrl_h(self):
        """
        作用：模拟按下ctrl+h按键,名称为"^h"
        """
        keyevent("^h")

    def keyevent_ctrl_s(self):
        """
        作用：模拟按下ctrl+s按键,名称为"^a^s"
        """
        keyevent("^a^s")

    def keyevent_esc(self):
        """
        作用：模拟按下esc按键
        """
        keyevent("{ESC}")

    def keyevent_Ctrl_C(self):
        """
        作用：模拟按下ctrl+c按键,名称为"^a^c"
        """
        keyevent("^a^c")
