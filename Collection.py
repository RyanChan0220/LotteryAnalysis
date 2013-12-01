__author__ = 'Ryan'

import MySQLdb as mdb
from xlrd import open_workbook, cellname


def read_excel():
    datas = []
    book = open_workbook('20020101-20130501.xls')
    sheet = book.sheet_by_index(0)
    print sheet.name
    print sheet.nrows
    print sheet.ncols
    for row_index in range(4022):
        if(row_index >= 1):
            print "ths row is: %d", row_index
            award_string = sheet.cell(row_index, 3).value
            try_string = sheet.cell(row_index, 11).value
            award_num = int(award_string)
            try_num = int(try_string)
            datas.append((sheet.cell(row_index, 2).value, sheet.cell(row_index, 1).value,
                          award_string,
                          str(award_num / 100), str((award_num % 100) / 10), str(award_num % 10),
                          try_string,
                          str(try_num / 100), str((try_num % 100) / 10), str(try_num % 10)))
    return datas


def connect_to_db(db_name):
    try:
        con = mdb.connect(host='localhost', user='root', passwd='7758258', db=db_name, port=3306)
        return con
    except mdb.Error, e:
        print "Mysql connect error %d: %s" % (e.args[0], e.args[1])


def close_db(conn):
    conn.close()


def write_many_to_db(conn, datas):
    with conn:
        cur = conn.cursor()
        cur.executemany("INSERT INTO award(DATE, NO, AWARD_NUM, AWARD_HUNDREDS, AWARD_DECADE, AWARD_UNIT, \
        TRY_NUM, TRY_HUNDREDS, TRY_DECADE, TRY_UNIT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", datas)
        conn.commit()
        cur.close()


if __name__ == '__main__':
    data = read_excel()
    connection = connect_to_db("3dlottery")
    #data = []
    #data.append(('20120101', '20120101', '123', '1', '2', '3', '321', '3', '2', '1'))
    #data.append(('20130101', '20120101', '123', '1', '2', '3', '321', '3', '2', '1'))
    write_many_to_db(connection, data)
    close_db(connection)