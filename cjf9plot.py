## cjf9plot
## 一个类似于Gnuplot的画图软, 输入help显示全部命令.
## 需要matplotlib, math


import matplotlib.pyplot as plt
from math import *


class Data:
    expr = "x**2+x*sin(10*x)"
    x_set = [0.01*i for i in range(1, 1001)]


def welcome():
    print("\n\ncjf9plot是一个画图软件\n")
    print("输入help查看全部命令\n\n\n")


def help():
    print("\n\n目前的全部命令如下, 尖括号<>及其里的内容表示由用户替换：\n")
    print("1 查看全部命令： help")
    print("2 画出f(x)的图像： plot <f(x)> ")
    print("3 重画上一次命令画的图： replot ")
    print("4 设置采样点： set samples <start stop step> ")
    print("5 定义函数： f(x) = <具体的表达式> 靠这个忘了实现了。。。")
    print("6 还要定义将多个函数画在一个图里的。plot <f(x) g(x) ...>")


def toplot():
    '''根据Data.x_set和Data.expr生成y_set, 然后绘制图形并显示'''
    y_set = [eval(Data.expr) for x in Data.x_set]
    plt.plot(Data.x_set, y_set) 
    plt.show()


def replot():
    '''replot = toplot'''
    toplot() 


def set_samples(start=0.1, stop=10, step=0.01):
    '''修改取样点'''
    Data.x_set = [start]
    stop_tmp = start + step
    while stop_tmp <= stop:
        Data.x_set.append(stop_tmp)
        stop_tmp = stop_tmp + step


def parse_cmd(str_cmd):
    '''将用户输入的命令进行解析，以元组返回该做什么的信号，以及分离出来的、下一步操作将用到的参数'''
    cmd_1 = str_cmd.split(" ")[0]   # cmd_1为str_cmd的第一个单词，用来识别这个命令想做什么
    if cmd_1 == "replot":
        return (":replot",)
    elif cmd_1 == "plot":
        return (":toplot", str_cmd.replace("plot", " "))
    elif cmd_1 == "set":     # 将来如果出了set samples以外的set xxx命令， 这里记得修改。。。可以考虑用抽象类改写。哎。
         return (tuple(str_cmd.replace("set samples", ":set_samples").split(" ")))        
    elif cmd_1 == "help":
        return (":help",)
    else:
        return (":done", )



def main_loop():
    while True:
        str_cmd = input("\ncjf9plot>>> ")
        tuple_signal = parse_cmd(str_cmd)
        if tuple_signal[0] == ":replot":
            toplot()
        elif tuple_signal[0] == ":toplot":
            Data.expr = tuple_signal[1]
            toplot()
        elif tuple_signal[0] == ":set_samples":
            set_samples(float(tuple_signal[1]), float(tuple_signal[2]), float(tuple_signal[3])) 
        elif tuple_signal[0] == ":help":
            help()
        elif tuple_signal[0] == ":done":
            print("若要关闭,请直接关闭脚本！\n")
            main()

def main():
    welcome()
    main_loop()
       

main()




