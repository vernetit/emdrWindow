#pyinstaller.exe --onefile .\emdr.py

import win32gui
import time
import sys
import os, random
import subprocess
import psutil
import os, random

import pywinauto

from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()

import tkinter as tk
import threading
import sys

exit=0

velocity=0.4
variable = ""
variable1 = ""
volumen=0.4
root=""

def update_status():
    global velocity
    global variable
    print("menos")
    velocity+=0.05
    variable.set(velocity)
    pass

def update_status1():
    global velocity
    global variable
    print("mas")
    velocity-=0.05
    variable.set(velocity)
    pass

def update_status2():
    global volumen
    global variable1
    print("mas")
    if volumen<=0.15 : return;
    volumen-=0.1

    variable1.set(volumen)
    pass

def update_status3():
    global volumen
    global variable1
    print("mas")
    volumen+=0.1
    variable1.set(volumen)
    pass

def run_gui():

    global root

    root = tk.Tk()
    button1 = tk.Button(root, text="mas", command=update_status1)
    button = tk.Button(root, text="menos", command=update_status)

    button2 = tk.Button(root, text="menos volumen", command=update_status2)
    button3 = tk.Button(root, text="mas volumen", command=update_status3)
    global velocity
    global volumen
    global variable
    global variable1
    button.pack()
    button1.pack()
    
    variable = tk.StringVar()
    variable.set(velocity)
    entry = tk.Entry(root, textvariable=variable)
    entry.pack()

    button2.pack()
    button3.pack()
    variable1 = tk.StringVar()
    variable1.set(volumen)
    entry1= tk.Entry(root, textvariable=variable1)
    entry1.pack()
    root.mainloop()
    #print("exit")  

    global exit
    exit=1
    global bSalir
    bSalir=1

    sys.exit(1)

gui_thread = threading.Thread(target=run_gui)
gui_thread.start()



bPan=0



import signal
import atexit

def handle_exit():

    volume.SetChannelVolumeLevelScalar(0, 0.4, None)
    volume.SetChannelVolumeLevelScalar(1, 0.4, None)

    

#atexit.register(handle_exit)
#signal.signal(signal.SIGTERM, handle_exit)
#signal.signal(signal.SIGINT, handle_exit)

# Obtener el objeto IAudioEndpointVolume
#volume = pywinauto.IAudioEndpointVolume()

# Establecer el nivel de pan a -1

#bPan=1;
'''
def loadwindowslist (hwnd, topwindows):
    topwindows.append ( (hwnd, win32gui.GetWindowText (hwnd)))

def showwindowslist ():
    topwindows = []
    win32gui.EnumWindows (loadwindowslist, topwindows)
    for hwin in topwindows:
        sappname=str (hwin [1])
        nhwnd=hwin [0]
        print (str (nhwnd) + " " + sappname)
showwindowslist ()




def findwindow (classname, windowname):
    return win32gui.FindWindow (classname, windowname)

def movewindow (hwnd, x, y):
    win32gui.MoveWindow (hwnd, x, y, 640, 480, True)

hwnd = findwindow (None, "SumatraPDF.exe")
if hwnd:
    movewindow (hwnd, 100, 100)

'''
'''
from multiprocessing import Process
from pynput import keyboard

tecla=""

def on_press(key):
    try:
        tecla=key
        print('Tecla presionada: {0}'.format(key.char))
    except AttributeError:
        pass
        #print('Tecla especial presionada: {0}'.format(key))

def on_release(key):
    return
    print('{0} liberada'.format(key))
    tecla=key 
    if key == keyboard.Key.esc:
        return False

def my_function():
    print('Hello from a parallel process!')
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    p = Process(target=my_function)
    p.start()
    p.join()



'''

#from multiprocessing import Process
from pynput import keyboard
import threading

tecla = 2

#velocity = 0.5

def on_press(key):
    try:
        global tecla 
        tecla = key.char
        #print('Tecla presionada: {0}'.format(key.char))
    except AttributeError:
        print('Tecla especial presionada: {0}'.format(str(key)))
        tecla = str(key)
        print(tecla)
        if tecla == "Key.esc" :

            volume.SetChannelVolumeLevelScalar(0, 0.4, None)
            volume.SetChannelVolumeLevelScalar(1, 0.4, None)

            print("salir")
            sys.exit()
            #quit()
            

def on_release(key):
    return
    print('{0} liberada'.format(key))
    if key == keyboard.Key.esc:
        return False

def detect_last_key():
    print("hola gato")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    t1 = threading.Thread(target=detect_last_key)
    #p = Process(target=detect_last_key)
    t1.start()
    #p.join()



a =  random.choice(os.listdir("C:\\Users\\User\\t4"))


#print(a)

r=random.randint(80,60*20)

print(sys.argv)



try:
    file = sys.argv[1]
except Exception:
    file="C:\\Users\\User\\t4\\"+a



#subprocess.Popen('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', 'C:\\Users\\User\\t4\\'+a)
subprocess.Popen('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe --start-time='+str(r)+' "'+file+'"')

time.sleep(2)



window = win32gui.FindWindow(None, "emdr7")
win32gui.ShowWindow(window, 6)

b=1

bSel=1;
bSalir=0
bNoSalir=0;



for i in range(1000):
    print(i)

    if i == 100 : 
        if bNoSalir :
            continue;
        bSalir = 1

    if tecla == "Key.esc" or bSalir :

        volume.SetChannelVolumeLevelScalar(0, 0.4, None)
        volume.SetChannelVolumeLevelScalar(1, 0.4, None)

        print("salir")
        
        PROCNAME = "vlc.exe"

        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()

        PROCNAME = "emdr.exe"

        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
        
        root.destroy()    
        
          

        sys.exit(1)
        quit()

        break 


    if tecla == "Key.up" :
        velocity -= 0.1
        tecla=2

    if tecla == "Key.left" :
        bNoSalir = 1
        print("no salir")
        tecla=2

       
    if tecla == "Key.down" :
        velocity += 0.1
        tecla=2


   #bPan= not bPan

    #if bPan :
    #    volume.setPan(-1, 0)
    #else :
    #    volume.setPan(1, 0)


    try:
        b= not b

        x=0

        if b :
            x=1360
            
        if bSel :
            hwnd = win32gui.GetForegroundWindow()
            bSel=0
        win32gui.MoveWindow(hwnd, x, 0, 640, 1080, True)

        title = win32gui.GetWindowText(hwnd)

        #print(tecla)

        #print(title)

    except Exception:
        duration_ms=3000
        pass

    bPan = not bPan

    try:
        if bPan :
            volume.SetChannelVolumeLevelScalar(0, 0, None)
            volume.SetChannelVolumeLevelScalar(1, volumen, None)
        else :
            volume.SetChannelVolumeLevelScalar(0, volumen, None)
            volume.SetChannelVolumeLevelScalar(1, 0, None)
    except AttributeError:
        pass

    #if exit:
    #    break

    time.sleep(velocity)

   
