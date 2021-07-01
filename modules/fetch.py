from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def fetch():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cur = conn.cursor()
        cur.execute("SELECT * FROM intelligence.malware")

        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

    except Error as e:
        print(e)

    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    fetch()

