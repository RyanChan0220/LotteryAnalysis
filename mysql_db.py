__author__ = 'Ryan'

import MySQLdb


class MySQLDB:
    __db_name = ""
    __con = None

    def __init__(self, db_name):
        self.__db_name = db_name

    def connect(self):
        try:
            self.__con = MySQLdb.connect(host='localhost', user='root', passwd='7758258', db=self.__db_name, port=3306)
        except MySQLdb.Error, e:
            print "Mysql connect error %d: %s" % (e.args[0], e.args[1])

    def close_connect(self):
        self.__con.close()

    def write_many(self, table, columns, values):
        with self.__con:
            cur = self.__con.cursor()
            column_values = "\%s" + ", %s"*len(columns)
            statement = """INSERT INTO %s(%s) VALUES(%s)""" % (table, columns, column_values)
            print statement
            cur.executemany(statement, values)
            self.__con.commit()
            cur.close()

    def write(self, table, column, value):
        with self.__con:
            cur = self.__con.cursor()
            statement = """INSERT INTO %s(%s) VALUES(%s)""" % (table, column, value)
            print statement
            cur.execute(statement)
            cur.close()





