# pyrus = python + virus

import time
from tkinter.ttk import Label

import pyautogui as pg # elegxei keyboard + mouse
import winsound # paizei mono .wav hxous
import os, sys # gia na exoume prosbasei se lutourgeies tou upologisti
import tkinter as tk # gia dhmiourgeia parathirou me eikones , koumpia kai alla
from PIL import Image, ImageTk # gia thn isagogei eikonwn sto programma

run = 0

def resource_path(relative_path): # prosarmozei to path pou tha valei tis eikones kai tous hxous
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def updateImg(imgNum, duration): # updateImg(3,5) -> tha fortwsei to bsod1.ppng
    img = 'bsod' + str(imgNum) + '.png'
    i = Image.open(resource_path(img)).resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.LANCZOS) #Image.LANCZOS einai o tropos me ton opoio tha ginei resize h eikona
    bg2 = ImageTk.PhotoImage(i)
    bglbl.configure(image=bg2)
    bglbl.image = bg2
    win.update()
    time.sleep(duration)

def virus(event):
    global run
    if run == 0:
      run = 1
      time.sleep(3)
      updateImg(1, 3)
      updateImg(2, 6)
      updateImg(3, 4)
      updateImg(4, 5)
      updateImg(5, 9)
      updateImg(6, 3)
      updateImg(7, 12)
      updateImg(8, 8)
      winsound.PlaySound(resource_path('sound.wav'),winsound.SND_ASYNC)  # den perimenei na teleivsei o hxos gia na allaksei eikona
      updateImg(9,9)



def disable():
    pass # auti h def den kanei akoma tipota

time.sleep(5)

pg.hotkey('win','d')

dir = os.path.dirname(os.path.abspath(sys.argv[0]))# mas dinei to path pou briskete auto to script
print(dir)
time.sleep(1)

im = pg.screenshot('desktop.png')

win = tk.Tk() # dimiourgia extra paratyrou
win.geometry('{}x{}+0+0'. format(win.winfo_screenwidth(), win.winfo_screenheight())) # rythmizoume tis diastsaseis tou parathurou
bg = tk.PhotoImage(file= 'desktop.png')
bglbl = tk.Label(win, image=bg, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
bglbl.place(x=0, y=0, width=win.winfo_screenwidth(), height =win.winfo_screenheight())


bglbl.bind('<Button-1>', virus)
win.attributes('-fullscreen', True) # gia na piasei to parathuro oli thn othonh
win.attributes('-topmost',True) # gia na einai mprosta apoola ta upoloipa parathyra
#win.bind('<Escape>', disable)# lew sto ESC na min kanei tipota
#win.protocol('WM_DELETE_WINDOW', disable) # lew sto alt f4 na min kanei tipota
win.update()








win.mainloop()#panata sto telos otan xrhsimopoioume thn bibliothykh tkinter