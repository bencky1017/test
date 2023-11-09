# -*- coding=utf-8 -*-
""" 
tkinter界面设计
"""

import tkinter as tk
from configparser import ConfigParser
from os.path import exists
from time import time

# 配置的路径
CONFIG_PATH = "./config.ini"
# 预设配置项
TITLE = "自动化测试配置箱"
WIDTH = 550
HEIGHT = 150
RESIZABLE_X, RESIZABLE_Y = 0, 0
# POINT_X, POINT_Y = 0, 0
LEFT, TOP = 500, 200
X, Y = LEFT, TOP
# 修改时间
DATE = int(time())
con = ConfigParser(allow_no_value=True)
[node_list, option_list, items_list, created, node, option, items] = ['']*7


def config_setting(node_list, option_list, items_list):
    """
    包含路径、配置项、修改时间、账号密码等信息 
    """
    config_created = 0
    if not exists(CONFIG_PATH):
        print('配置文件"config.ini"创建成功。')
        con['PATH'] = {'#配置文件出错时，删除此文件': None, "CONFIG_PATH": CONFIG_PATH}
        con['CONFIG'] = {
            "TITLE": TITLE,
            "WIDTH": WIDTH,
            "HEIGHT": HEIGHT,
            "RESIZABLE_X": RESIZABLE_X,
            "RESIZABLE_Y": RESIZABLE_Y,
            # "POINT_X": POINT_X,
            # "POINT_Y": POINT_Y,
            "LEFT": LEFT,
            "TOP": TOP,
            "X": LEFT,
            "Y": TOP,
        }
        con['MODIFY'] = {"DATE": DATE}
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            con.write(f)
        config_created = 1
    else:
        print('文件"config.ini"已存在，正在读取...')
        con.read(CONFIG_PATH, encoding='utf-8')  # 读取
        con['PATH'] = {'#配置文件出错时，删除此文件': None, "CONFIG_PATH": CONFIG_PATH}
        # con.set('PATH', 'CONFIG_PATH', CONFIG_PATH)  # 修改
        con['MODIFY'] = {'DATE': DATE}  # 添加键add_section删除节remove_option

        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            con.write(f)

        # 获取‘节’列表
        node_list = con.sections()
        # print(node_list)

        # 获取‘选项’列表，不含数据
        option_list = ['']*len(node_list)
        for i in range(len(node_list)):
            option_list[i] = con.options(node_list[i])

        # 获取‘行’列表，含数据
        items_list = [None]*len(node_list)
        for i in range(len(node_list)):
            items_list[i] = con.items(node_list[i])

        # 获取某个选项的值
        # item_val = con.get('CONFIG','TITLE')
        # item_val = con.getint('MODIFY', 'DATE')
        config_created = 0

    return config_created, node_list, option_list, items_list


def config_getting():
    """ 获取config文件数据到控制台 """
    created, node, option, items = config_setting(
        node_list, option_list, items_list)
    # print(created, node, option, items,sep='\n\n',end='\n\n')

    if (not created):
        print('已存在')
        cfg_get = {
            "TITLE": con.get('CONFIG', 'TITLE'),
            "WIDTH": con.get('CONFIG', 'WIDTH'),
            "HEIGHT": con.get('CONFIG', 'HEIGHT'),
            "RESIZABLE_X": con.get('CONFIG', 'RESIZABLE_X'),
            "RESIZABLE_Y": con.get('CONFIG', 'RESIZABLE_Y'),
            # "POINT_X": con.get('CONFIG', 'POINT_X'),
            # "POINT_Y": con.get('CONFIG', 'POINT_Y'),
            "LEFT": con.get('CONFIG', 'LEFT'),
            "TOP": con.get('CONFIG', 'TOP'),
            "X": con.get('CONFIG', 'X'),
            "Y": con.get('CONFIG', 'Y'),
        }

    else:
        print('已创建')
        cfg_get = {
            "TITLE": TITLE,
            "WIDTH": WIDTH,
            "HEIGHT": HEIGHT,
            "RESIZABLE_X": RESIZABLE_X,
            "RESIZABLE_Y": RESIZABLE_Y,
            # "POINT_X": POINT_X,
            # "POINT_Y": POINT_Y,
            "LEFT": LEFT,
            "TOP": TOP,
            "X": X,
            "Y": Y,
        }

    return cfg_get


def cfg_box():
    def update_size():
        """ 更新窗口大小 """
        con.read(CONFIG_PATH, encoding='utf-8')
        con.set('CONFIG', 'WIDTH', str(win.winfo_width()))
        con.set('CONFIG', 'HEIGHT', str(win.winfo_height()))
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            con.write(f)

    def get_point(event):
        """ 获取鼠标刚点击时候相对于当前窗口的坐标 """
        POINT_X, POINT_Y = event.x, event.y
        e = event.widget
        e.POINT_X = POINT_X
        e.POINT_Y = POINT_Y
        update_size()

    def move(event):
        """ 移动窗口 """
        e = event.widget
        move_x = event.x + win.winfo_x() - e.POINT_X
        move_y = event.y + win.winfo_y() - e.POINT_Y
        # print("X:"+str(win.winfo_x()), "Y:"+str(win.winfo_y()))
        move_x = -10 if move_x < 0-10 else move_x
        move_y = 0 if move_y < 0 else move_y

        RIGHT = win.winfo_screenwidth() - win.winfo_width() - 8  # 误差校正
        BOTTOM = win.winfo_screenheight() - win.winfo_height() - 30  # 误差校正
        move_x = RIGHT if move_x > RIGHT else move_x
        move_y = BOTTOM if move_y > BOTTOM else move_y

        cfg["WIDTH"] = win.winfo_width()
        cfg["HEIGHT"] = win.winfo_height()
        win.geometry(f'{cfg["WIDTH"]}x{cfg["HEIGHT"]}+{move_x}+{move_y}')
        update_size()

    # 创建配置文件，并获取数据
    cfg = config_getting()
    print(cfg["HEIGHT"])

    # 创建窗口
    win = tk.Tk()
    win.title(cfg["TITLE"])
    # win['width'] = WIDTH
    # win['height'] = HEIGHT
    win.geometry(f'{cfg["WIDTH"]}x{cfg["HEIGHT"]}+{cfg["X"]}+{cfg["Y"]}')
    win.resizable(cfg["RESIZABLE_X"], cfg["RESIZABLE_Y"])

    win.bind('<Button-1>', get_point)
    win.bind('<B1-Motion>', move)

    f1 = win.frame()

    # 执行程序
    win.update()
    win.mainloop()
