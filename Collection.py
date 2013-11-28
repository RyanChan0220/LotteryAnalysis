__author__ = 'Ryan'


from xlrd import open_workbook, cellname

book = open_workbook('20020101-20130501.xls')
sheet = book.sheet_by_index(0)
print sheet.name

print sheet.nrows
print sheet.ncols

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        print sheet.cell(row_index, col_index).value



#print open_workbook('20020101-20130501.xls')
#
#with open('20020101-20130501.xls', 'rb') as f:
#    print open_workbook(file_contents=mmap(f.fileno(), 0, access=ACCESS_READ))
#
#aString = open('20020101-20130501.xls', 'rb').read()
#print open_workbook(file_contents=aString)