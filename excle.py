import openpyxl

book = openpyxl.load_workbook('excel_data/Book1.xlsx')
ws = book["Sheet1"]
cell = ws.cell(row=1,column=1)
cell.value = "データA1"
book.save('excel_data/Book1.xlsx')

book.close()
