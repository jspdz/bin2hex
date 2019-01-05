"""
File: bin2hex.py
实现bin文件转换为C语言数组的功能，输入文件名，hex文件为原文件名加后缀hex。
2019年1月5日 gary 于福州。

"""

import sys
import os
import errno
import optparse
import struct


class Bin2Hex:
    def __init__(self, BinFileName):
        self.__BinFileName = BinFileName
        self.__HexFileName = BinFileName + ".hex"
        if(os.path.getsize(binfile) > 10*1024*1024):
            print("容量要小于10MBytes。")
            return -1

    def readBinWriteHex(self):
        fWrite=open(self.__HexFileName,"w")
        with open(self.__BinFileName, 'rb') as f:
            fsize = os.path.getsize(self.__BinFileName)
            while f.tell() != fsize:
                # read up to recordlength bytes from the file, don't bridge segment.
                bindata = f.read(16)
                for b in bindata:
                    fWrite.write("%02X " % b)
                fWrite.write("\n")
        fWrite.close()

