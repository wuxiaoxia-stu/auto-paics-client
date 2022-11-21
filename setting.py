import os
from enum import Enum

# 工作目录
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 默认屏幕大小
DEFAULT_SCREEN_WIDTH = 1920
DEFAULT_SCREEN_HEIGHT = 1080

# 登录界面选中用户大小
DEFAULT_ACTIVE_USER_WIDTH = 304
DEFAULT_ACTIVE_USER_HEIGHT = 436


# 用户组类型
class UserGroup(Enum):
    MANAGE_GROUP = 1
    PUBLIC_GROUP = 2
    PRIVATE_GROUP = 3


UserGroupImgDict = {UserGroup.MANAGE_GROUP: "manager_b.bmp", UserGroup.PRIVATE_GROUP: "private_b.bmp",
                    UserGroup.PUBLIC_GROUP: "public_b.bmp"}


# 循环次数
ROUND_TOTAL = 10

# 密码图案索引列表
PASSWORD_INDEX = [0, 1, 2, 3, 4, 5]
ERROR_PASSWORD_INDEX = [0, 3, 2, 1]

# 用户名
USER_NAME = "Andy"
