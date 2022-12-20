class AlarmClock(Tk):
    def __init__(self):
        super().__init__()
        self.title('我的闹钟')
        self.minsize(width=300, height=300)

        # 设置控件
        Label(self, text='现在时间：', font=('Arial', 15)).place(x=10, y=10)

        self.now_time = str(datetime.now()).split('.')[0]    #获取本地时间
        self.var_nowtime = StringVar(value=self.now_time)
        Label(self, textvariable=self.var_nowtime, font=('Arial', 15), bg='#D6EAF8').place(x=50, y=50)

        # 闹钟的时间设置部分用了三个entry控件输入时分秒
        Label(self, text='设置闹钟：', font=('Arial', 15)).place(x=10, y=90)
        self.var_hour = StringVar(value='00')
        self.var_min = StringVar(value='00')
        self.var_sec = StringVar(value='00')
        self.entry_hour = Entry(self, textvariable=self.var_hour, font=('Arial', 15), bg='#D6EAF8', width=3,
                                justify='center')
        self.entry_hour.place(x=60, y=130)
        Label(self, text=':', font=('Arial', 15)).place(x=105, y=130)
        self.entry_min = Entry(self, textvariable=self.var_min, font=('Arial', 15), bg='#D6EAF8', width=3,
                               justify='center')
        self.entry_min.place(x=120, y=130)
        Label(self, text=':', font=('Arial', 15)).place(x=165, y=130)
        self.entry_sec = Entry(self, textvariable=self.var_sec, font=('Arial', 15), bg='#D6EAF8', width=3,
                               justify='center')
        self.entry_sec.place(x=180, y=130)

        # 因为只能设定一个闹钟，所以再次设定的话要重置
        self.btn_replace = Button(self, text='重置', font=('Arial', 12), width=5, command=self.replace)
        self.btn_replace.place(x=70, y=180)
        # 开关按钮控制闹钟的开和关，初始是OFF状态，点击变成ON状态启动闹钟
        self.btn_begin = Button(self, text='OFF', font=('Arial', 12), width=5, command=self.beginning)
        self.btn_begin.place(x=150, y=180)
        def beginning(self):
            flag = self.btn_begin['text']      # 定义一个flag来表示闹钟的状态
        # 如果是打开状态就什么也不做
        if flag == 'ON':
            return
        # 如果是关闭状态，就把text变为ON，三个输入框变为不可编辑
        else:
            self.btn_begin['text'] = 'ON'
            self.entry_hour['state'] = DISABLED
            self.entry_min['state'] = DISABLED
            self.entry_sec['state'] = DISABLED
            # 获取三个输入框内的时间
            set_time = '%s:%s:%s' % (self.entry_hour.get(), self.entry_min.get(), self.entry_sec.get())
            list_time = []
            for i, j in zip(set_time.split(':'), self.now_time.split(' ')[-1].split(':')):
                # 计算离闹钟启动还有多少时间
                list_time.append(abs(int(i) - int(j)))
            messagebox.showinfo(title='设置成功', message='距离启动还有%d小时%d分%d秒' % tuple(list_time))
            def replace(self):
        # 重置按钮把三个输入框内容变为00，同时变为可编辑状态，开关按钮变为OFF
                self.var_hour.set('00')
                self.var_min.set('00')
                self.var_sec.set('00')
                self.btn_begin['text'] = 'OFF'
                self.entry_hour['state'] = NORMAL
                self.entry_min['state'] = NORMAL
                self.entry_sec['state'] = NORMAL
        messagebox.showinfo(title='重置成功', message='重置成功')
        def timer(self):
            player = ctypes.windll.kernel32    # 这个模块我也不是太清楚，这里是用来产生蜂鸣的
        while True:
            self.now_time = str(datetime.now()).split('.')[0]    
            self.var_nowtime.set(self.now_time)
            self.update()

            set_time = '%s:%s:%s' % (self.entry_hour.get(), self.entry_min.get(), self.entry_sec.get())
            if self.btn_begin['text'] == 'ON':
                # 设定时间和本地时间一致，闹钟就响1.5秒
                if set_time == self.now_time.split(' ')[-1]:
                    for i in range(3):
                         # 人耳能听到的频率是20~20000HZ，这里设定2000HZ，500ms
                        player.Beep(2000, 500)   

            time.sleep(1)    # 1秒钟更新一次
