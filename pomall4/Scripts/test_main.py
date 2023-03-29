#coding=utf-8
   # os模块调用CMD命令有两种方式：os.popen()，os.system() 都是用当前进程来调用 属于阻塞式调用方式
    # 当控制台中文乱码时 将File→Settings→Editor→File Encodings→Project Encoding，将这个值设置为GBK #控制台的编码格式需要和windows保持一致。
   # a=os.system("ipconfig")
   # print(a) #系统层面的直接调用 os.system是无法获取返回值的。当运行结束后接着往下面执行程序。
   #   #OS.popen带返回值的，如何获取返回值。#新开线程方式 利用os.popen可以执行windows的程序并可以获得返回内容
   # p = os.popen('ipconfig')
   # print("p.read(): {}\n".format(p.read()))#popen需要关闭close().当执行成功时，close()不返任何值，失败时，close()返回系统返回值

   #python调用linux  os库、subprocess库、commands库 官方比较推荐的是subprocess模块。 commands在python3失效
   # print(os.system('ping www.baidu.com'))
   # print(os.listdir("/")) #打印出当前目录下的所有文件
   # print(os.getcwd())#打印出当前目录
import time
import unittest

from pomall4.tools.BeautifulReport import BeautifulReport

class testmain():
    def mainf(self):
        su = unittest.defaultTestLoader.discover("./", pattern="test*.py")
        filepath = "{}.html".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
        BeautifulReport(su).report(description="beautify", filename=filepath, log_path="../log/")

if __name__=="__main__":
    # unittest.main()
    testmain().mainf()
