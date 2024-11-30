import os
import tkinter as tki
import openpyoxl
from tkinter import messagebox
import threading
import time

#رقم قفل التطبيق

password = '123456'


#رسالة إدخال رقم خاطئ

def on_close():
   messagebox.showerror('security','enter a correct password')
   

def check_pass():
   
   psd = enter.get() 
   if psd == password:
      tk.destroy()
      global run
      run = False
      
   
   else:
      messagebox.showerror('security','password is wrong')
      os.system('taskkill /im DrawNote.exe')
      tk.destroy()
#الكود الأساسي للتشغيل


def prot():
   global tk
   global enter
   
   
   tk = tki.Tk()
   tk.attributes('-fullscreen',True)
   tk.resizable(False,False)
   tk.attributes('-topmost',True)
   tk.protocol('WM_DELETE_WINDOW',on_close)
   labe = tki.Label(tk,text='أدخل كلمة المرور')
   labe.pack()
   enter = tki.Entry(tk,show='•')
   enter.place(x=155,y=255)
   butt = Button(tk,text = 'دخول',command = check_pass)
   butt.pack()
   
   tk.mainloop()
def run_script():
   global run
   run = True
   
   while run:
#التطبيق الذي يتم قفله
      if 'DrawNote.exe' in os.popen('tasklist').read():
         prot()
      time.sleep(1)
#كود مراقبة التطبيقات
def mainlo():
   thrd = threading.Thread(target= run_script)
   thrd.daemon = True
   thrd.start()
   while True:
      pass
if __name__ == '__main__':
   mainlo()









