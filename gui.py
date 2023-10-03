import PySimpleGUI as sg
import tkinter as tk
import datetime

dt_now = datetime.datetime.now()
today = dt_now.strftime('%Y年%m月%d日')
today_time = dt_now.hour,"時",dt_now.minute,"分"
layout = [[sg.Text(today)], [sg.Text(today_time)],[sg.Button("OK")]]
window = sg.Window("watch", layout, size=(200, 100))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break  

window.close()