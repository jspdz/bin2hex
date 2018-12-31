import tkinter
import os
from tkinter import messagebox


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
        return fl

    def hex_output(self):
        tc3=messagebox.showinfo(title='消息弹窗',message='已经执行完毕！')  # return ok
        print (tc3)


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
