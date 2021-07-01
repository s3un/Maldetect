import mysql.connector
import sys

def search():
    rec = sys.argv[1]

    if rec is not "":
        try:
            con = mysql.connector.connect(host='localhost', user='root', password='Postgres@1', database='intelligence')
            if con.is_connected():
                print("Successfully connected to database\nQuery database for hash")
                cur = con.cursor()
                cur.execute("SELECT * FROM intelligence.malware")