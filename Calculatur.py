import tkinter
from tkinter import messagebox,ttk
class GuiDemo():
    def __init__(self,windowtitle):    
        #实例化一个窗口对象,windowtitle为窗口名
        self.root = tkinter.Tk()
        #窗口的标题
        self.root.title(windowtitle)
        #指定主框体大小
        self.root.geometry('400x90')
        return
    def operation(self):
        operator = self.operator.get()
        value1 = self.input_value1.get()
        value2 = self.input_value2.get()
        if operator == '+':
            result = value1 + value2
        elif operator == '-':
            result = value1 - value2
        elif operator == '*':
            result = value1 * value2
        elif operator == '÷':
            result = value1 / value2
#【bug】将显示结果的部分写在这个函数里会造成每次计算的结果不断叠加在前一个结果上，如果结果比之前的长度长就显示正常，
#否则数字显示叠加混乱,因此将控件布置写在calculator里，这里只做属性配置更新
#         ret = tkinter.StringVar()
#         tkinter.Label(self.root,textvariable=ret,bg='Red').grid(column=4,row=1)
#         print(result)
#         ret.set('    '+str(result))
        self.lab.config(text=result)
        self.butt.configure(text='结果',bg='green')
        messagebox.showinfo(title='这是个提示信息', message=result)

  
        return
    def calculator(self):
        root = self.root
        
        self.input_value1 = tkinter.IntVar()
        input1 = tkinter.Entry(root,textvariable=self.input_value1,width=12)
        input1.grid(column=0,row=1)
        self.input_value1.set('')#不设置初始值的话会默认显示0
        #当程序运行时,光标默认会出现在该文本框中
        input1.focus()
        
        #与Entry类似但可以指定输入范围值，当用户只需要从极少的数值中进行选择的时候，就可以使用Spinbox取代Entry
        #increment表示增量
        #Spinbox(root,from_=0,to=10,increment=2).grid(column=1,row=0)
        #Spinbox(root,values=('+','-','*','/')).grid(column=1,row=0)
        
        #创建下拉列表
        self.operator = tkinter.StringVar()
        selec = ttk.Combobox(root,textvariable=self.operator,width=8)
        # 设置下拉列表的值元组或者列表
        selec['values'] = ['+','-','*','÷']
        selec.grid(column=1,row=1)
        #设置下拉列表默认显示的值,0为 selec['values'] 的下标值
        selec.current(0)
        
        
        self.input_value2 = tkinter.IntVar()
        tkinter.Entry(root,textvariable=self.input_value2,width=12,show='*').grid(column=2,row=1)
        self.input_value2.set('')
        
        tkinter.Label(root,text='请输入：',font=("黑体",10, "bold")).grid(column=0,row=0)
        tkinter.Label(root,text='请选择：',font=("黑体",10, "bold")).grid(column=1,row=0)
        tkinter.Label(root,text='请输入：',font=("黑体",10, "bold")).grid(column=2,row=0)
        self.butt = tkinter.Button(root,text='=',font=("黑体",11, "bold"),command=self.operation)
        self.lab = tkinter.Label(self.root,text='          ',bg='green')
        self.lab.grid(column=4,row=1)
        self.butt.grid(column=3,row=1)
        return
    def runGui(self):
        # 进入消息循环
        self.root.mainloop()
if __name__ == '__main__':
    app = GuiDemo('计算')
    app.calculator()
    app.runGui()
