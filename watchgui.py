import PySimpleGUI as sg
import datetime
import openpyxl

book = openpyxl.load_workbook('excel_data/Book1.xlsx')
ws = book["Sheet1"]
i = 1

sg.theme('DarkPurple1')
wstart = 0 #workstart
wend = 0
bstart = 0 #breakstart
bend = 0

wsbool = False
webool = False
bsbool = False
bebool = False

def getTime():
     return datetime.datetime.now().strftime('%-m/%-d %H:%M:%S')

layout = [[sg.Text('', size=(20, 2), key='_time_',font=(40))],[sg.Text('Command'),sg.InputText(size=(20,3),key='-command-'),sg.Button('OK', key='-btn-')]]
window = sg.Window('Clock', layout, grab_anywhere=True)

def Record():
    if wsbool == True:
        cell = cell(row=i,column=1)
        cell.value = wstart
        i += 1
        wsbool == False
        book.save('excel_data/Book1.xlsx')
    book.close()

while True:
     Record()
     event, values = window.Read(timeout=1000)
     if event == '-btn-':
          if values['-command-'] == 'wstart':
               wstart = datetime.datetime.now()
               window['-command-'].update('')
               wsbool = True
               print(wsbool)
          elif values['-command-'] == 'wend':
               wend = datetime.datetime.now()
               window['-command-'].update('')
               webool = True
          elif values['-command-'] == 'bstart':
               bstart = datetime.datetime.now()
               window['-command-'].update('')
               bsbool = True
          elif values['-command-'] == 'bend':
               bend = datetime.datetime.now()    
               window['-command-'].update('')
               bebool = True
     if event == sg.WINDOW_CLOSED:
         break
     window.FindElement('_time_').Update(getTime())




window.Close()
