__author__ = 'Ryan'

import mysql_db
import excel
import calculator


def input_to_db():
    excel_file = excel.Excel()
    excel_file.open_book("20020101-20130501.xls")
    excel_file.open_sheet_by_index(0)
    data = excel_file.read_cols(1, 4022, (2, 1, 3, 11))
    for row in range(len(data)):
        award_num = int(data[row][2])
        try_num = int(data[row][3])
        data[row].insert(len(data[row]) - 1, str(award_num / 100))
        data[row].insert(len(data[row]) - 1, str((award_num % 100) / 10))
        data[row].insert(len(data[row]) - 1, str(award_num % 10))
        data[row].append(str(try_num / 100))
        data[row].append(str((try_num % 100) / 10))
        data[row].append(str(try_num % 10))
    mdb = mysql_db.MySQLDB()
    mdb.connect("3dlottery")
    mdb.insert_many("award", "DATE, NO, AWARD_NUM, AWARD_HUNDREDS, AWARD_DECADE,\
    AWARD_UNIT, TRY_NUM, TRY_HUNDREDS, TRY_DECADE, TRY_UNIT", data)
    mdb.close_connect()


if __name__ == '__main__':
    calculator.caculator()
