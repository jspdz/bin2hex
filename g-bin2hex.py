import tkinter
import os
from tkinter import messagebox
from bin2hex import Bin2Hex

class b2h_ui(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("gary bin2hex tools 2018年12月30日 ")
        # 创建一个输入框,并设置尺寸
        #self.ip_input = tkinter.Entry(self.root,width=90)
        # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root,  width=90)
        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command = self.hex_output, text = "执行转换")

    # 完成布局
    def gui_arrang(self):
        #  self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    #列出本目录的文件列表
    def file_list(self):
        path= os.getcwd()
        fl = os.listdir(path)
         #清空回显列表可见部分,类似clear命令
        #for item in range(10):
        #    self.display_info.insert(0,"")
        # 为回显列表赋值
        END = 'end'
        self.display_info.delete(0, END)
        i = 1
        for item in fl:
            if os.path.isfile(item):
                self.display_info.insert(END,"xxx " + str(i) + ": "+ item)
                i=i+1
        # 选中列表中的第0行。
        if(i>1):
            self.display_info.selection_set(0)
        return fl



    def hex_output(self):
        current_index = self.display_info.curselection()
        #print(current_index)
        if(current_index == ()):
            tc3=messagebox.showinfo(title='消息弹窗',message="未选中需要转换的文件。 curselection=()")  # return ok
            print("未选中需要转换的文件。 curselection=()")
            return
        current_string = self.display_info.get(current_index)
        print(current_string)
        bin_filename = bin_file_name(str(current_string))
        print(bin_filename)
        hex_filename = str(bin_filename)+"_hex.txt"

        thread = Bin2Hex(bin_filename, hex_filename)
        thread.start()
        
        '''
        fWrite=open(bin_filename+".hex","w")
        with open(bin_filename, 'rb') as f:
            fsize = os.path.getsize(bin_filename)
            while f.tell() != fsize:
                bindata = f.read(16)
                for b in bindata:
                    fWrite.write("0x%02X, " % b)
                fWrite.write("\n")
        fWrite.close()
        '''

        tc3=messagebox.showinfo(title='消息弹窗',message="文件 "+bin_filename+"  已经处理。")  # return ok
        print (tc3)

#将列表里的头去掉 "xxx 1: b.py"，剩下 “b.py”
def bin_file_name(ss):
    result = ""
    max_index = len(ss)-1
    index = 0

    while ((ss[index] != ":") and (index < 10)):
        index = index+1
    index+=2
    while (index <= max_index) :
        result += ss[index]
        index = index+1
    return result

def main():
    # 初始化对象
    bh = b2h_ui()
    # 进行布局
    bh.gui_arrang()
    bh.file_list()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
