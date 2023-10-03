import PySimpleGUI as sg
import datetime

sg.theme('DarkPurple1')
def getTime():
     return datetime.datetime.now().strftime('%-m/%-d %H:%M:%S')

layout = [[sg.Text('', size=(20, 2), key='_time_',font=(40))],[sg.Text('Command'),sg.InputText(size=(20,1))]]
window = sg.Window('Clock', layout, grab_anywhere=True)

while True:
     event, values = window.Read(timeout=1000)
     if event == sg.WINDOW_CLOSED:
         break
     window.FindElement('_time_').Update(getTime())

window.Close()
