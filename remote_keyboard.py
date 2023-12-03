import kivy
kivy.require("1.11.1")
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.gridlayout import GridLayout

import socket, threading
from  threading import Thread
import json



SERVER = None
PORT  = 8000
IP_ADDRESS  = "192.168.0.111"

BUFFER_SIZE = 4096




class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        keyboard =VKeyboard(on_key_up = self.key_up)
        self.label=Label(text ="Selected key : ",font_size ="50sp")

        layout.add_widget(self.label)
        layout.add_widget(keyboard)
        return layout
    def key_up(self, keyboard, keycode, *args):
        global SERVER
        if isinstance(keycode,tuple):
            keycode = keycode[1]
        self.label.text = "Selected key : "+str(keycode)
        print(str(keycode))
        SERVER.send((str(keycode)).encode('ascii'))
    
    def setup():
        global SERVER
        global PORT
        global IP_ADDRESS
        global remote_mouse
        PORT  = 8000
        IP_ADDRESS  = "192.168.0.111"
    
        try:
            SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            SERVER.connect((IP_ADDRESS, PORT))
            #start_write()
            SERVER.listen(10)
            print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")
            getDeviceSize()
            acceptConnections()
            return True
        except:
            return False

    setup_thread = threading.Thread(target=setup)                   #sending messages 
    setup_thread.start()        

def getDeviceSize():
    global screen_width
    global screen_height
    for m in get_monitors():
        screen_width - int(str(m).split(",")[2].strip()("width=")[1])
        screen_height - int(str(m).split(",")[3].strip()("width=")[1])

def recvMessage(client_socket):
    global keyboard

    while True:
        try:
            message = client_socket.recv(2048),decode()
            if(message):
                keyboard.press(message)
                keyboard.release(message)
                print(message)
        except Exception error:
            pass

def acceptConnections():
    global SERVER
    while True:
        client_socket,addr = SERVER.accpet()
        print(f"Connection established with {client_socket} : {addr}")
        thread1 = Thread(target = recvMessage,args={client_socket,})
        thread1.start()

        
if __name__== '__main__':
    MyApp().run()
    

#def write():
#    global SERVER    
#    while True:                                                 #message layout
#        if msvcrt.kbhit():
#            key_stroke = msvcrt.getch()
#            print(key_stroke)
#            #SERVER.send(message.encode('ascii'))    
       
#def start_write():
#    write_thread = threading.Thread(target=write)                   #sending messages 
#    write_thread.start()
    
