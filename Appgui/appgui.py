# hello_psg.py

import PySimpleGUI as sg
import time
import tkinter

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")],[sg.Button("not OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        tkinter.messagebox.showwarning(title=None, message="Hello")
        time.sleep(2)
        break

window.close()