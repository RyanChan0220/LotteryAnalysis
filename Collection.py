__author__ = 'Ryan'

import MySQLdb as mdb
import sys
from xlrd import open_workbook, cellname

#con = mdb.connect(host='localhost', user='root', passwd='7758258', db='lottery')
#with con:
#    cur = con.cursor()
#    cur.execute("INSERT INTO test VALUES(1,2)")
#    cur.close()
#con.close()
    #cur.execute("CREATE TABLE IF NOT EXISTS \
    #            Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
    #cur.execute("INSERT INTO Writers(Name) VALUES('abc')")
    #cur.execute("INSERT INTO Writers(Name) VALUES('def')")


#mydb = mdb.connect(host='localhost', user='root', passwd='7758258', db='lottery')
#cur = mydb.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS test6(ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(45))")
#statement = "INSERT INTO test6(Name) VALUES('abc')"
#cur.execute(statement)
#cur.execute("SELECT VERSION()")
#print "The version is: %s" % cur.fetchone()
#cur.close()
#mydb.close()

#book = open_workbook('20020101-20130501.xls')
#sheet = book.sheet_by_index(0)
#print sheet.name
#
#print sheet.nrows
#print sheet.ncols
#
#for row_index in range(sheet.nrows):
#    for col_index in range(sheet.ncols):
#        print sheet.cell(row_index, col_index).value


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
    connection = connect_to_db("3dlottery")
    data = []
    data.append(('20120101', '20120101', '123', '1', '2', '3', '321', '3', '2', '1'))
    data.append(('20130101', '20120101', '123', '1', '2', '3', '321', '3', '2', '1'))
    write_many_to_db(connection, data)
    close_db(connection)