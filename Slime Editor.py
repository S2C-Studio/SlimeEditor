#初始化
import tkinter as tk
window = tk.Tk()
window.title('Slime Editor')
#新建菜单栏
menubar = tk.Menu(window)
#创建一个文件菜单项
fileMenu = tk.Menu(menubar,tearoff=0)
#——————分割线，下面是函数区———————
def newFile():
    pass
def openFile():
    pass
def saveFile():
    pass
#——————分割线——————
#菜单栏里的三个小菜单：新文件，打开文件和保存文件
fileMenu.add_command(label="新文件",command=newFile)
fileMenu.add_command(label="打开文件",command=openFile)
fileMenu.add_command(label="保存文件",command=saveFile)
#让菜单栏显示出来
window.config(menu=menubar)
#主循环
window.mainloop()
