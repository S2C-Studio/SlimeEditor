#初始化
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
window=Tk()
window.title('Slime Editor')
window.geometry("500x650")
#新建菜单栏
menuBar = Menu(window)
#创建一个文件菜单项，样板菜单项和关于菜单项
file=Menu(menuBar,tearoff=0)
fileHelp=Menu(menuBar,tearoff=0)
about=Menu(menuBar,tearoff=0)
#设置当前路径
path = ""
#设置窗口图标
window.iconbitmap("icon.ico")
#——————分割线，下面是函数区———————
#写入文件(注意不弹出保存窗口)
def quitwindow():
    teamWindow.destroy()
#写入文件(注意不弹出保存窗口) 
def writeFile(path):
    if path != "":
        file = open(path,"w",encoding='utf-8')
        fileIn = text.get('0.0','end')
        file.write(fileIn)
        file.close()
        #弹出保存成功信息
        tkinter.messagebox.showinfo(title='提示', message='保存成功！')
#开发者信息窗口
def windowOfTeam():
    #基本的东西
    global teamWindow
    teamWindow=Tk()
    teamWindow.title('关于开发者')
    teamWindow.geometry("300x100")
    #设置窗口图标
    teamWindow.iconbitmap("icon.ico")
    #文本
    em = Label(teamWindow,text="编辑器-由S2C工作室制作")
    em.pack()
    slm = Label(teamWindow,text="Slime语言-由ScerX制作")
    slm.pack()
    t = Label(teamWindow,text="感谢您的使用。")
    t.pack()
    #退出按钮
    qb = Button(teamWindow,text="关闭",command=quitwindow)
    qb.pack()
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
    path = filedialog.askopenfilename(title="选择打开的文件",filetypes=(("sl files", "*.sl"),))
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
        path = filedialog.asksaveasfilename(title="保存文件",filetypes=(("sl files", "*.sl"),))
    #写入文件
    writeFile(path)
    window.title('Slime Editor-'+path)
#另存为文件
def saveInAnotherFile():
    global path
    #设置路径
    path = filedialog.asksaveasfilename(title="保存文件",filetypes=(("sl files", "*.sl"),))
    writeFile(path)
    #设置窗口名
    window.title('Slime Editor-'+path)
#打开一个叫HelloWorld.sl的示例文件
def helloWorldFile():
    file = open("HelloWorld.sl","r")
    fileIn = file.read()
    #清空文本框
    text.delete('1.0','end')
    #把内容写入到文本框
    text.insert(END,fileIn)
    #设置窗口名
    window.title('Slime Editor-HelloWorld.sl')
#打开开发者档案窗口
def aboutProgramer():
    windowOfTeam()
#——————分割线——————
#菜单栏里的文件的四个小菜单：新文件，打开文件，保存文件和另存为
file.add_command(label="新文件",command=newFile)
file.add_command(label="打开文件",command=openFile)
file.add_command(label="保存文件",command=saveFile)
file.add_command(label="另存为",command=saveInAnotherFile)
#示例程序的示例：HelloWorld
fileHelp.add_command(label="HelloWorld.sl",command=helloWorldFile)
#关于菜单栏的一个项：关于
about.add_command(label="关于开发者",command=aboutProgramer)
#让菜单栏显示出来
menuBar.add_cascade(label="文件",menu=file)
menuBar.add_cascade(label="示例文件",menu=fileHelp)
menuBar.add_cascade(label="关于",menu=about)
window['menu']=menuBar
#创建一个滚动条
scroll = Scrollbar()
#创建全屏文本框
text = Text(window,height=640,fg="black",selectbackground='green',yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
text.pack()
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
#主循环
window.mainloop()
