import os
import csv
import time
import pyautogui
from datetime import datetime

from setting import DEFAULT_SCREEN_HEIGHT, DEFAULT_SCREEN_WIDTH, BASE_DIR

screenWidth, screenHeight = pyautogui.size()

if not os.path.exists(os.path.join(BASE_DIR, "output")):
    os.makedirs(os.path.join(BASE_DIR, "output"))


TEST_CSV_HEADER = ["测试步骤", "结果"]


def program_exit(func):
    """
    测试装饰器，写测试结果
    :param func:
    :return:
    """
    def wrapper(*args, **kw):
        res = func(*args, **kw)
        write_test_result(res)
        return res
    return wrapper


def write_test_result(data):
    """
    记录测试结果到csv文件中
    :return:
    """

    filename = os.path.join(BASE_DIR, "output", datetime.now().strftime("%Y%m%d") + "_test.csv")
    file_exists = os.path.exists(filename)
    with open(filename, "a+", encoding="utf-8", newline="") as f:
        f_csv = csv.writer(f)
        if not file_exists:
            f_csv.writerow(TEST_CSV_HEADER)
        f_csv.writerow(data)


def move_to(x, y):
    """
    移动鼠标
    :param x: 移动的x坐标
    :param y: 移动的y坐标
    :return:
    """

    rate_x, rate_y = 1, 1
    if screenWidth / screenHeight == DEFAULT_SCREEN_WIDTH / DEFAULT_SCREEN_HEIGHT:
        rate_x = screenWidth / DEFAULT_SCREEN_WIDTH
        rate_y = screenHeight / DEFAULT_SCREEN_HEIGHT
    pyautogui.moveTo(x * rate_x, y * rate_y, duration=0.3)


def has_image(target, region=None):
    """
    查找目标图片，返回第一个符合的坐标
    :param target: bmp图谱路径
    :param region: 检索区域
    :return: 目标坐标（left, top, width, height）
    """

    try:
        if region:
            location_point = pyautogui.locateOnScreen(target, region=region, confidence=0.9)
        else:
            location_point = pyautogui.locateOnScreen(target, confidence=0.9)
        if location_point:
            return location_point.left, location_point.top, location_point.width, location_point.height
        else:
            return 0, 0, 0, 0
    except Exception as e:
        print("exception: ", str(e))
        return -1, -1, -1, -1


def drag_password(pos_index_list, drag_times=10):
    """
    绘制密码
    :param pos_index_list: 密码的圆点索引列表
    :param drag_times: 绘制次数
    :return: success: 绘制是否成功
    :return: err: 错误信息
    """

    err = ""
    success = False

    # 至少五个坐标
    if len(pos_index_list) < 5 or len(pos_index_list) > 9:
        err = "invalid params"
        return success, err

    i = drag_times
    while i > 0:
        pos_list = list(pyautogui.locateAllOnScreen('static/add_user/password_icon.bmp'))
        if len(pos_list) > 6:
            if i == 1:
                err = "drag password overrun"
                break
            start_pos = pos_index_list[0]
            move_to(pos_list[start_pos].left + pos_list[start_pos].width // 2, pos_list[start_pos].top +
                    pos_list[start_pos].height // 2)
            pyautogui.mouseDown()
            for pos_index in pos_index_list[1:]:
                move_to(pos_list[pos_index].left + pos_list[pos_index].width // 2, pos_list[pos_index].top +
                        pos_list[pos_index].height // 2)
            pyautogui.mouseUp()
            time.sleep(1)
        elif len(pos_list) > 0:
            err = 'drag password error!'
            continue
        else:
            success = True
            break
        i -= 1
    return success, err


def back_to_home():
    """
    返回首页
    :return:
    """

    move_to(40, 25)
    pyautogui.click()

