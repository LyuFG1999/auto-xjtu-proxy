# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:28:47 2024

@author: Lyu
"""

import subprocess
import threading
import sys
import os
from pystray import Icon, Menu, MenuItem
from PIL import Image

#1 直连状态； 2 代理状态

# 子进程变量
child1 = None
child2 = None
image1 = None
image2 = None

# 初始化状态为True表示初始状态，False表示状态2
state = True

# 更新图标和启动子进程的函数
def update_state(icon, script1, script2):
    global state, child1, child2

    if state:
        # 切换到状态2
        if child1:
            child1.terminate()  # 终止child1进程
        icon.icon = Image.open("proxy.png")
        icon.title = " [Status] Proxying... \n [Port] 127.0.0.1:12380"
        child2 = subprocess.Popen(['python', script2])
    else:
        # 切换回初始状态
        if child2:
            child2.terminate()  # 终止child2进程
        icon.icon = Image.open("direct.png")
        icon.title = " [Status] Directing...\n [Port] 127.0.0.1:12380"
        child1 = subprocess.Popen(['python', script1])

    state = not state

# 退出程序的函数
def quit_app(icon):
    global child1, child2
    if child1:
        child1.terminate()  # 终止child1进程
    if child2:
        child2.terminate()  # 终止child2进程
    icon.stop()
    os._exit(1)
    
# 创建托盘图标
def create_tray_icon():
    global child1, child2

    # 初始化托盘图标
    image1 = Image.open("direct.png")
    image2 = Image.open("proxy.png")
    
    # 启动初始状态的子进程
    script_path1 = "direct_port.py"  # 替换为实际脚本路径
    script_path2 = "proxy_port.py"  # 替换为实际脚本路径
    child1 = subprocess.Popen(['python', script_path1])

    # 创建托盘菜单
    menu = Menu(
        MenuItem('Switch Mode', lambda icon: update_state(icon, script_path1, script_path2)),
        MenuItem('Quit Script', quit_app)
    )

    # 设置托盘图标及菜单
    icon = Icon("tray_icon", image1, " [Status] Directing...\n [Port] 127.0.0.1:12380", menu)
    
    # 运行托盘
    icon.run()

if __name__ == "__main__":
    create_tray_icon()
