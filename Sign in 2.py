import tkinter
import tkinter.messagebox
class LoginPage(object):
    def __init__(self):
        #声明两个变量
        self.win = tkinter.Tk()  # 窗口
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.createForm()
 
    def login(self):
        if self.username.get()=='admin' and self.password.get()=='123456':
            print('登录成功')
            tkinter.messagebox.showinfo(title='登录信息',message='登录成功')
            self.win.quit()
        else:
            print('登录失败')
            tkinter.messagebox.showerror(title='登录信息',message='登录失败')
    def createForm(self):
        self.win.title('登录界面')
        #创建标签
        labelname = tkinter.Label(self.win,text='用户名：',justify=tkinter.RIGHT,width = 80)
        #将标签放置在窗口上
        labelname.place(x=10,y=5,width=80,height=20)
        #创建文本框
        entryname = tkinter.Entry(self.win,width = 80,textvariable=self.username)
        entryname.place(x=100,y=5,width=80,height=20)
        #创建密码标签
        labelpwd = tkinter.Label(self.win,text='密  码：',justify=tkinter.RIGHT,width=80)
        labelpwd.place(x=10,y=30,width=80,height=20)
        #创建密码的文本框
        entrypwd = tkinter.Entry(self.win,width = 80,textvariable=self.password)
        entrypwd.place(x=100,y=30,width=80,height=20)
        #创建button按钮
        buttonOk = tkinter.Button(self.win,text='登录',command=self.login)
        buttonOk.place(x=30,y=70,width=50,height=20)
        #创建退出的按钮
        buttonQuit = tkinter.Button(self.win,text='退出',command=self.win.quit)
        buttonQuit.place(x=90,y=70,width=50,height=20)
        self.win.mainloop()
 
if __name__ == '__main__':
    lg = LoginPage()

