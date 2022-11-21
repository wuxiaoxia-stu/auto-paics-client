# -*- encoding=utf8 -*-

__author__ = "PAICS"

import pytest
from page.page_paics_login import PagePaicsLogin

@pytest.mark.login
class TestLogin:

    def setup_class(self):
        self.page_login = PagePaicsLogin()  # 实例化

    def test_login(self):
        """
        测试登录
        """
        self.page_login.login()  # 登录

#
# if __name__ == '__main__':
#     pytest.main(['-vs'])
