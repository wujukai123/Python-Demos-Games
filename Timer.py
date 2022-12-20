import time
from pygame import mixer
t=int(input("请输入计时时间")
print('开始倒计时',time.ctime())
time.sleep(t)
print('定时结束', time.ctime())
mixer.Sound("beep.wav")
beep.play()
time.sleep(10)
