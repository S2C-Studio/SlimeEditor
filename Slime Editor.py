#初始化
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
window=Tk()
window.title('Slime Editor')
window.geometry("500x650")
#新建菜单栏
menuBar = Menu(window)
#创建一个文件菜单项
file=Menu(menuBar,tearoff=0)
#设置当前路径
path = ""
#设置窗口图标
window.iconbitmap("icon.ico")
#——————分割线，下面是函数区———————
#写入文件(注意不弹出保存窗口)
def writeFile(path):
    if path != "":
        file = open(path,"w",encoding='utf-8')
        fileIn = text.get('0.0','end')
        file.write(fileIn)
        file.close()
        #弹出保存成功信息
        tkinter.messagebox.showinfo(title='提示', message='保存成功！') 
#新建文件
def newFile():
    #弹出警告窗口
    fileMode = tkinter.messagebox.askyesno(title='你确定要新建文件吗？', message='如果你没有保存该文件，您的文件可能会丢失！')
    #如果选择yes就清空文本框
    if fileMode:
        text.delete('1.0','end')
        window.title('Slime Editor')
def openFile():
    #询问文件路径
    global path
    path = filedialog.askopenfilename(title="选择打开的文件",filetypes=(("sli files", "*.sli"),))
    #打开并读取文件
    if path != "none" and path !="":
        file = open(path,"r",encoding='utf-8')
        fileIn = file.read()
        file.close()
        #清空文本框
        text.delete('1.0','end')
        #把内容写入到文本框
        text.insert(END,fileIn)
        #设置窗口名
        window.title('Slime Editor-'+path)
def saveFile():
    global path
    if path == "":
        #询问路径
        path = filedialog.asksaveasfilename(title="保存文件",filetypes=(("sli files", "*.sli"),))
    #写入文件
    writeFile(path)
    window.title('Slime Editor-'+path)
#另存为文件
def saveInAnotherFile():
    global path
    #设置路径
    path = filedialog.asksaveasfilename(title="保存文件",filetypes=(("sli files", "*.sli"),))
    writeFile(path)
    #设置窗口名
    window.title('Slime Editor-'+path)
#——————分割线——————
#菜单栏里的四个小菜单：新文件，打开文件，保存文件和另存为
file.add_command(label="新文件",command=newFile)
file.add_command(label="打开文件",command=openFile)
file.add_command(label="保存文件",command=saveFile)
file.add_command(label="另存为",command=saveInAnotherFile)
#让菜单栏显示出来
menuBar.add_cascade(label="文件",menu=file)
window['menu']=menuBar
#创建一个滚动条
scroll = Scrollbar()
#创建全屏文本框
text = Text(window,height=640,fg="blue",selectbackground='green',yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
text.pack()
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
#主循环
window.mainloop()
