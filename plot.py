## cjf9plot
## 一个类似于Gnuplot的画图软, 输入helpme显示全部命令.
## 需要matplotlib, math


import matplotlib.pyplot as plt
from math import *


def welcome():
    print("\n\ncjf9plot是一个画图软件\n")
    print("输入help查看全部命令\n\n\n")

def help():
    print("\n\n目前的全部命令如下, 尖括号<>及其里的内容表示由用户替换：\n")
    print("1 查看全部命令： help")
    print("2 画出f(x)的图像： plot <f(x)> ")
    print("3 重画上一次命令画的图： replot ")
    print("4 设置采样点： set samples <start stop setp> ")
    print("5 定义函数： f(x) = <具体的表达式> 靠这个忘了实现了。。。")
    print("6 还要定义将多个函数画在一个图里的。plot <f(x) g(x) ...>")


class Data:
    '''数据结合结构体.像CPP的static， 不需要实例化就有了，大概在堆区'''
    expr = "x**2+x*sin(10*x)"
    x_set = [0.01*i for i in range(1, 1001)]

def toplot():
    '''根据Data.x_set和Data.expr生成y_set, 然后绘制图形并显示'''
    y_set = [eval(Data.expr) for x in Data.x_set]
    plt.plot(Data.x_set, y_set) 
    plt.show()

replot = toplot #'''绘制上一次绘制的函数的图像，如果取样点被改变了，则用新的取样点来画'''

def set_samples(start=0.1, stop=10, step=0.01):
    '''修改取样点'''
    Data.x_set = [start]
    stop_tmp = start + step
    while stop_tmp <= stop:
        Data.x_set.append(stop_tmp)
        stop_tmp = stop_tmp + step

def process(str_cmd):
    '''将用户输入的命令进行解析，以元组返回该做什么的信号，以及分离出来的、下一步操作将用到的参数'''
    cmd_1 = str_cmd.split(" ")[0]                              # cmd_1为str_cmd的第一个单词，用来识别这个命令想做什么
    if cmd_1 == "replot":
        return (":replot", "占位符。神经病python把单元素tuple直接剥离了")
    elif cmd_1 == "plot":
        return (":toplot", str_cmd.replace("plot", " "))
    elif cmd_1 == "set":                                    # 将来如果出了set samples以外的set xxx命令， 这里记得修改。。。可以考虑用抽象类改写。哎。
         return (tuple(str_cmd.replace("set samples", ":set_samples").split(" ")))        # tuple和list互为反函数
    elif cmd_1 == "help":
        return (":help", "占位字符")
    else:
        return (":done", "占位字符")

def main():
    '''显示欢迎界面，不断接受用户输入的指令，解析并做出反应'''
    welcome()
    while True:
        str_cmd = input("\ncjf9plot>>> ")
        tuple_signal = process(str_cmd)
        if tuple_signal[0] == ":replot":
            toplot()
        elif tuple_signal[0] == ":toplot":
            Data.expr = tuple_signal[1]
            toplot()
        elif tuple_signal[0] == ":set_samples":
            set_samples(float(tuple_signal[1]), float(tuple_signal[2]), float(tuple_signal[3]))  # 这里犯错告诉我，动态类型是拿来方便用的，不是拿来偷懒的。要时刻明白自己在处理什么类型！！
        elif tuple_signal[0] == ":help":
            help()
        elif tuple_signal[0] == ":done":
            print("若要关闭,请直接关闭脚本！\n")
            main()
       


main()




### ---------------------------------------------------------------------------------------------------------
# ???误操作发现类变量可以被实例私有化！！不知道为什么。一般实例变量都用self.var_name的方式在__init__()中创建。
# private方的方法和变量用__打头即可
