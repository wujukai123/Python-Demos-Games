from tkinter import *
from time import *
from calendar import *
class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#create labels
        for i in range(7):
            label = Label(self, text=days[i])
            label.grid(row = 0, column = i)

        weekday, numDays = monthrange(year, month)
        week = 1
        for i in range(1, numDays + 1):
            button = Button(self, text = str(i))
            button.grid(row = week, column = weekday)

            weekday+=1
            if weekday > 6:
                week +=1
                weekday = 0
