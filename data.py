import openpyxl
import watchgui

book = openpyxl.load_workbook('excel_data/Book1.xlsx')
ws = book["Sheet1"]
i = 1

def Record():
    if watchgui.wstart == True:
        cell = ws.cell(row=i,column=1)
        cell.value = watchgui.wstart
        i += 1
        watchgui.wstart == False
        book.save('excel_data/Book1.xlsx')
    book.close()
