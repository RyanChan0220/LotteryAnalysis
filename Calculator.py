__author__ = 'Ryan'

import mysql_db


def caculator():
    mdb = mysql_db.MySQLDB()
    mdb.connect("3dlottery")
    award_h = mdb.query("award", "AWARD_HUNDREDS")
    award_d = mdb.query("award", "AWARD_DECADE")
    award_u = mdb.query("award", "AWARD_UNIT")
    times_h = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    times_d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    times_u = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in award_h:
        times_h[int(i[0])] += 1
    for i in award_d:
        times_d[int(i[0])] += 1
    for i in award_u:
        times_u[int(i[0])] += 1
    print "\n-------------------AWARD HUNDREDS--------------------------"
    for i in range(len(times_h)):
        print "%d: %.2f %%\t\t" % (i, 100 * (float(times_h[i])/sum(times_h))),
        if i == 4:
            print
    print "\n-------------------AWARD DECADE--------------------------"
    for i in range(len(times_d)):
        print "%d: %.2f %%\t\t" % (i, 100 * (float(times_d[i])/sum(times_d))),
        if i == 4:
            print
    print "\n-------------------AWARD UNIT--------------------------"
    for i in range(len(times_u)):
        print "%d: %.2f %%\t\t" % (i, 100 * (float(times_u[i])/sum(times_u))),
        if i == 4:
            print
    try_h = mdb.query("award", "TRY_HUNDREDS")
    try_d = mdb.query("award", "TRY_DECADE")
    try_u = mdb.query("award", "TRY_UNIT")
    for i in try_h:
        times_h[int(i[0])] += 1
    for i in try_d:
        times_d[int(i[0])] += 1
    for i in try_u:
        times_u[int(i[0])] += 1
    print "\n\n-------------------TRY HUNDREDS--------------------------"
    for i in range(len(times_h)):
        print "%d: %.2f %%\t\t" % (i, 100 * (float(times_h[i])/sum(times_h))),
        if i == 4:
            print
    print "\n-------------------TRY DECADE--------------------------"
    for i in range(len(times_d)):
        print "%d: %.2f %%\t\t" % (i, 100 * (float(times_d[i])/sum(times_d))),
        if i == 4:
            print
    print "\n-------------------TRY UNIT--------------------------"
    for i in range(len(times_u)):
        print "%d: %.2f %%\t\t" % (i, 100 * (float(times_u[i])/sum(times_u))),
        if i == 4:
            print
    mdb.close_connect()