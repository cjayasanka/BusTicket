import MySQLdb


def dbConnection():

    conn = MySQLdb.connect(host="sql12.freesqldatabase.com", user="sql12245338", passwd="jKTYhdgkdF", db="sql12245338")
    cursor = conn.cursor()
    return cursor;

dbConnection()








