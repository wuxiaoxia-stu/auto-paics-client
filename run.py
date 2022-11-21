# -*- encoding=utf8 -*-

__author__ = "PAICS"

import pytest
from launch import launch

if __name__ == '__main__':
    # 启动连接设备模块
    launch()
    # 生成报告路径
    # 运行pytest主运行程序
    pytest.main(['-vs', '-q', '-ra', '--alluredir', './report/allure'])
    # os.system('allure generate %s -o ./report --clean' % report_path)
    # os.system('allure serve %s' % report_path)


    #TODO allure报告
