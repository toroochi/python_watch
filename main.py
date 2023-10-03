import openpyxl

book = openpyxl.load_workbook('/Users/yamaokana/Desktop/project_2/excel_data/Book1.xlsx')
print(len(book.sheetnames))

for name in book.get_sheet_names():
    print(name)