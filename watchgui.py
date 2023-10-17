import PySimpleGUI as sg
import datetime
import openpyxl

book = openpyxl.load_workbook('excel_data/Book1.xlsx')
ws = book["Sheet1"]
i = 1
j = 1
p = 1
q = 1

a = False
b = False
c = False 
d = False

while True:
     if ws.cell(row=i,column=1).value != None:
          i += 1
     else:
          a = True
     if ws.cell(row=j,column=2).value != None:
          j += 1
     else:
          b = True
     if ws.cell(row=p,column=3).value != None:
          p += 1
     else:
          c = True
     if ws.cell(row=q,column=4).value != None:
          q += 1
     else:
          d = True
     if a == True and b == True and c == True and d == True:
          break

sg.theme('DarkPurple1')
wstart = 0 #workstart
wend = 0
bstart = 0 #breakstart
bend = 0

wsbool = False
webool = False
bsbool = False
bebool = False
count = 0

def getTime():
     return datetime.datetime.now().strftime('%-m/%-d %H:%M:%S')

layout = [[sg.Text('', size=(20, 2), key='_time_',font=(40))],[sg.Text('Command'),sg.InputText(size=(20,3),key='-command-'),sg.Button('OK', key='-btn-')]]
window = sg.Window('Clock', layout, grab_anywhere=True)

def Record():
     global i,j,p,q,count,wsbool,webool,bsbool,bebool
     if wsbool == True and count == 1:
          ws.cell(row=i,column=1).value = wstart
          i += 1
          wsbool = False
          book.save('excel_data/Book1.xlsx')
          print(wsbool)
          print("aaa")
          count = 0
     if webool == True and count == 1:
          ws.cell(row=j,column=2).value = wend
          j += 1
          webool = False
          book.save('excel_data/Book1.xlsx')
          count = 0
     if bsbool == True and count == 1:
          ws.cell(row=p,column=3).value = bstart
          p += 1
          bsbool = False
          book.save('excel_data/Book1.xlsx')
          count = 0
     if bebool == True and count == 1:
          ws.cell(row=q,column=4).value = bend
          q += 1
          bebool = False
          book.save('excel_data/Book1.xlsx')
          count = 0
     
while True:
     Record()
     event, values = window.Read(timeout=1000)
     if event == '-btn-':
          if values['-command-'] == 'wstart' and count == 0:
               wstart = datetime.datetime.now()
               window['-command-'].update('')
               wsbool = True
               count += 1
               print(count)
          elif values['-command-'] == 'wend' and count == 0:
               wend = datetime.datetime.now()
               window['-command-'].update('')
               webool = True
               count += 1
          elif values['-command-'] == 'bstart' and count == 0:
               bstart = datetime.datetime.now()
               window['-command-'].update('')
               bsbool = True
               count += 1
          elif values['-command-'] == 'bend' and count == 0:
               bend = datetime.datetime.now()    
               window['-command-'].update('')
               bebool = True
               count += 1
     if event == sg.WINDOW_CLOSED:
         break
     window.find_element('_time_').Update(getTime())


window.Close()
