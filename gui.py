import PySimpleGUI as sg
import datetime

def getTime():
     return datetime.datetime.now().strftime('%-m/%-d %H:%M:%S')

layout = [[sg.Text('', size=(19, 0), key='_time_',font=(30))]]
window = sg.Window('Clock', layout, grab_anywhere=True)

while True:
     event, values = window.Read(timeout=1000)
     if event == sg.WINDOW_CLOSED:
         break
     window.FindElement('_time_').Update(getTime())

window.Close()
