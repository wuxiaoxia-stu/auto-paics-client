# -*- encoding=utf8 -*-

__author__ = "PAICS"

import os

import allure
import pytest
from testcases.base import Base
from page.page_paics import PagePaics


@allure.epic("AYJ PAICS客户端测试")
@allure.feature("实时检查模块")
class TestPaics(Base):

    @classmethod
    def setup_class(cls):
        cls.paics_page = PagePaics()  # 实例化PaicsPage
        cls.paics_page.paics_initialization()  # 初始化paics客户端，使其返回系统首页
        cls.base_config(cls.paics_path + 'appconfig.ini', 'DEBUG', 'video_path', cls.video_json_path)  # 修改配置文件的video_path的值，
        # 在此调用需要传入参数Base对Base进行实例化，否则调用异常，提示缺少参数

    @pytest.mark.check_demo
    @pytest.mark.parametrize('VideoInfo', Base.csv_util.read_csv('demo.csv', Base.video_name, Base.video_length))
    @allure.story('实时检查')
    @allure.title('选择A/B开始实时检查-手动点击停止检查按钮')
    @allure.description('校验实时检查功能是否正常')
    @allure.severity("critical")
    def test_paics_demo(self, VideoInfo):
        """demo测试视频3s"""
        video_name = self.video_path + VideoInfo[0]  # 测试视频路径加上视频名称
        self.base_modify_json(self.video_json_path, video_name, 'video_path_list')  # 修改json数据，修改视频文件名称
        if "FT" in VideoInfo[0]:
            self.paics_page.paicsA_stop(VideoInfo[1])
            self.base_write_log(VideoInfo[0] + " 已完成国家级早孕筛查测试")
        else:
            self.paics_page.paicsB_stop(VideoInfo[1])  # paics客户端点击B执行实时分析，手动停止检查
            self.base_write_log(VideoInfo[0] + " 已完成国家级中孕筛查测试")

    @pytest.mark.check
    @pytest.mark.parametrize('VideoInfo', Base.csv_util.read_csv('demo.csv', Base.video_name, Base.video_length))
    @allure.story('实时检查')
    @allure.title('选择A/B开始实时检查-无需手动点击停止检查按钮')
    @allure.description('校验实时检查功能是否正常')
    @allure.severity("critical")
    def test_paics_check(self, VideoInfo):
        """测试完整视频"""
        video_name = self.video_path + VideoInfo[0]  # 测试视频路径加上视频名称
        self.base_modify_json(self.video_json_path, video_name, 'video_path_list')  # 修改json数据，修改视频文件名称
        if "FT" in VideoInfo[0]:
            self.paics_page.paicsA_auto(VideoInfo[1])
            self.base_write_log(VideoInfo[0] + " 完成国家级早孕筛查测试")
        else:
            self.paics_page.paicsB_auto(VideoInfo[1])  # paics客户端点击B执行实时分析，手动停止检查
            self.base_write_log(VideoInfo[0] + " 完成国家级中孕筛查测试")

    @classmethod
    def teardown_class(cls):
        cls.keys_util.keyevent_win()  # 点击win键


#
# if __name__ == '__main__':
#     pytest.main(['-vs'])
