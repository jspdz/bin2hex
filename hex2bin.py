"""
File: hex2bin.py
实现C语言数组转换为二进制bin文件的功能，输入文件名，bin文件为原文件名加后缀bin。
2019年1月5日 gary 于福州。

"""

import sys
import os
import errno
import optparse
import struct
import threading

class Hex2Bin(threading.Thread):
    #初始化函数，输入 二进制文件名，十六进制文件名
    def __init__(self, hex, bin):
        threading.Thread.__init__(self) 
        self.__bin_filename = bin
        self.__hex_filename = hex
        pass
        '''
        if(os.path.getsize(self.__bin_filename) > 10*1024*1024):
            print("容量要小于10MBytes。")
            return -1
        '''

    def run(self):
        fWrite=open(self.__bin_filename,"w")
        with open(self.__hex_filename, 'rb') as f:
            fsize = os.path.getsize(self.__bin_filename)
            while f.tell() != fsize:
                bindata = f.read(16)
                for b in bindata:
                    fWrite.write("0x%02X, " % b)
                fWrite.write("\n")
        fWrite.close()

        
