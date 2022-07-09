from distutils.command.config import config
from logging import shutdown
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from time import *
import sys
import pyglet
import os

version = "1.1.2"




pyglet.font.add_file('digital-7.ttf')
count = 0

class StopWatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')
        self.timer_label.config(foreground='cyan')        
    def start(self):
        global count
        count=0
        self.timer()   
    def stop(self):
        self.timer_label.config(foreground='yellow')
        global count
        count=1
    def close(self):
        self.main.destroy()
    def timer(self):
        global count
        if(count==0):
            self.timer_label.config(foreground='red')
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.main.after(1000,self.timer)     

    def clock(self):
        self.tick = strftime('%H:%M:%S %p')
        self.clock_label .config(text = self.tick)
        self.clock_label .after(1000, self.clock)
    
    def save_time(self):
        self.saved_time.set(self.d)
        self.label_savedtime.config(foreground='green')
        print(str(self.saved_time))

    def reset_savedTime(self):
        self.saved_time.set("00:00:00")
        self.label_savedtime.config(foreground='cyan')
    
    def open_quit_messagebox(self):
        doClose = messagebox.askyesno(title="Exit?", message="Do you really want to exit?")
        if doClose:
            self.close()
        else:
            print('User choose NO')

    def open_shutdown_messagebox(self):
        self.shutdown_time = self.shutdown_entry.get()
        if self.shutdown_time == "":
            self.shutdown_time = "10"
        if not self.shutdown_time.isnumeric():
            self.shutdown_label.config(text="ERROR: Please enter a valid number!", foreground='red')
            return
        doShutdown = messagebox.askyesno(title='Shutdown?', message=f'Do you really want\nto shutdown your system in:\n {self.shutdown_time} seconds?')
        if doShutdown:
            self.shutdown_system()
        else:
            self.shutdown_timelabel.config(text='System-shutdown canceled!', foreground='green')
            self.shutdown_entry.delete(0)
            print('User cancled shutdown')

    def shutdown_system(self):
        self.shutdown_time = self.shutdown_entry.get()
        self.shutdown_timelabel.config(text="PC shutdown in : " + str(self.shutdown_time)  +" seconds...\nYou can Press 'Cancel' to cancel the shutdown!", foreground='red')
        print(self.shutdown_time)
        os.system(f'shutdown /s /t {self.shutdown_time}')
    
    def cancel_shutdown(self):
        os.system('shutdown /a')
        self.shutdown_timelabel.config(text="System-Shutdown successfully cancled!", foreground='green')
        self.shutdown_time = "0"
        self.shutdown_entry.delete(0)
        

    def __init__(self):
        self.main = Tk()
        self.saved_time= StringVar()
        self.saved_time.set("00:00:00")
        self.tick = ""
        self.timeInSeconds= ""
        self.shutdown_time =""
        self.t = StringVar()
        self.t.set("00:00:00")
        self.main.minsize(200, 150)
        self.main.title("Digitial Clock with Python")
        self.main.iconbitmap(default='icon.ico')

        self.savedtime_label = Label(self.main, font=('digital-7', 14), background='black', foreground='gold', text="-Your saved time-")
        self.label_savedtime= Label(self.main, font=('digital-7',20), background='black', foreground='orange', textvariable=self.saved_time) 
        self.label_stopwatch =Label(self.main, font=('digital-7',14), background='black', foreground='gold', text="-Stopwatch-")
        self.label_time =Label(self.main, font=('digital-7',14), background='black', foreground='gold', text="-Current Time-")
        self.mainLabel = Label(self.main, font= ('digital-7', 40), background='black', foreground='cyan', text='Python Watch')
        self.clock_label= Label(self.main, font = ('digital-7', 20), background = 'black', foreground = 'cyan')
        self.timer_label = Label(self.main, textvariable=self.t,font=('digital-7', 20), background = 'black', foreground='cyan')
        self.brand_label = Label(self.main, text=f'Stopwatch Version {version} | by S3R43o3', font=('digital-7', 9), background='black', foreground='cyan')
        self.shutdown_time = 5
        self.shutdown_entry = Entry(self.main, width= 5, foreground='black', background='black',justify='center', textvariable=self.shutdown_time)
        
        self.exit_button = Button(self.main, text = 'Exit Watch', width = 10, padding = 2, command = self.open_quit_messagebox)
        self.save_button = Button(self.main, text = 'Save Time', width = 10, padding = 2,command = self.save_time)
        self.start_button = Button(self.main, text = 'Timer Start', width=10, padding=2, command=self.start)
        self.stop_button = Button(self.main, text = "Timer Stop", width= 10, padding=2, command= self.stop)
        self.reset_button = Button(self.main, text = "Timer Reset", width=10, padding=2, command= self.reset)
        self.reset_savedtime_button = Button(self.main, text="Reset Save", width=10, padding=2, command=self.reset_savedTime)
        self.shutdown_button =Button(self.main, text="Shutdown System", width=18, padding=2, command=self.open_shutdown_messagebox)
        self.shutdown_label = Label(self.main, text="-Shutdown Time-", font=("digital-7",14),background='black', foreground='gold')
        self.shutdown_timelabel = Label(self.main, text="Enter seconds to wait before shutdown.", font=('digital-7',12), background='black', foreground='green')
        self.cancel_shutdown_button = Button(self.main, text="Cancel Shutdown",width=18, padding=2, command=self.cancel_shutdown)

        self.mainLabel.pack(anchor='center', pady=20)
        self.label_time.pack(anchor='center', pady=0)
        self.clock_label.pack(anchor='center',pady=15)
        self.label_stopwatch.pack(anchor='center', pady=0)
        self.timer_label.pack(anchor='center',pady =15)
        self.savedtime_label.pack(anchor='center', pady=0)
        self.label_savedtime.pack(anchor='center', pady= 15)
        self.shutdown_label.pack(anchor='center', pady=0)
        self.shutdown_timelabel.pack(anchor='center', pady=0)
        self.shutdown_entry.pack(anchor='center', pady=8)
        self.shutdown_button.pack(anchor='center', pady=10)
        self.cancel_shutdown_button.pack(anchor='center', pady=2)
        self.brand_label.pack(anchor='center', pady=10)
        self.exit_button.pack(anchor='center',side=RIGHT)
        self.reset_savedtime_button.pack(anchor='center', side=RIGHT)
        self.save_button.pack(anchor = 'center',side=RIGHT)
        self.reset_button.pack(anchor='center', side=RIGHT)
        self.stop_button.pack(anchor='center', side=RIGHT)
        self.start_button.pack(anchor='center', side=RIGHT)
        self.main.configure(background = 'black')
        self.clock()
        self.main.mainloop()


if __name__=='__main__':
    stopwatch = StopWatch()
        