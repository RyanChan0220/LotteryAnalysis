__author__ = 'Ryan'

from mmap import mmap, ACCESS_READ
from xlrd import open_workbook

book = open_workbook('20020101-20130501.xls')

print book.nsheets

for sheet_index in range(book.nsheets):
    print book.sheet_by_index(sheet_index)

print book.sheet_names()

for sheet_name in book.sheet_names():
    print book.sheet_by_name(sheet_name)

for sheet in book.sheets():
    print sheet


#print open_workbook('20020101-20130501.xls')
#
#with open('20020101-20130501.xls', 'rb') as f:
#    print open_workbook(file_contents=mmap(f.fileno(), 0, access=ACCESS_READ))
#
#aString = open('20020101-20130501.xls', 'rb').read()
#print open_workbook(file_contents=aString)