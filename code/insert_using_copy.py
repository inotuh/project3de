import psycopg2
import csv

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")
cur = conn.cursor()

#create table
cur.execute("""
        CREATE TABLE IF NOT EXISTS users_using_copy(
            id serial PRIMARY KEY
            , email text
            , name text
            , phone text
            , postal_code text)
            """)

with open("/home/informatics/de15_project3/source/users_w_postal_code.csv",'r') as f:
    next(f)
    cur.copy_from(f,'users_using_copy', sep=',', columns=('email','name','phone','postal_code'))

conn.commit()

try:
   cur.execute("""SELECT * FROM users_using_copy""")
   rows = cur.fetchall()
   print(rows)
except:
    print ("Data not found!")