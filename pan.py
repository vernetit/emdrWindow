#pyinstaller.exe --onefile .\pan.py
import time
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(-0.20, None)
#volume_level = 0.1
#volume.SetChannelVolumeLevelScalar(0, volume_level, None)
#volume.SetChannelVolumeLevelScalar(1, volume_level, None)

import tkinter as tk
import threading
import sys

exit=0

velocity=0.4
variable = ""
variable1 = ""
volumen=0.4

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
	print("exit")

	

	global exit
	exit=1

gui_thread = threading.Thread(target=run_gui)
gui_thread.start()



bPan=0



import signal
import atexit

def handle_exit():

	volume.SetChannelVolumeLevelScalar(0, 0.4, None)
	volume.SetChannelVolumeLevelScalar(1, 0.4, None)

    

atexit.register(handle_exit)
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)
	
for i in range(10000):
	#variable.set(velocity)
	#print(velocity)
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

	if exit:
		break

	time.sleep(velocity)