#-*- coding:utf-8 -*-

info_switch = 0 #信息打印开关 0 打开
dbg_switch = 1  #调试打印开关 0 打开

def print_info(msg):
    if info_switch == 0 :
        print(msg)
    return

def print_dbg(msg):
    if dbg_switch == 0:
        print('[dbg]:'+ str(msg))
