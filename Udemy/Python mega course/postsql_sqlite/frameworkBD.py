import psycopg2
import json

with open('config.json') as data:
    d = json.load(data)
    data.close()

def create_table():
    conn = psycopg2.connect("dbname='"+d["database"]+"' user='"+d["user"]+"' password='"+d["password"]+"' host='"+d["host"]+"' port='"+d["port"]+"'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(tabela, valores):
    conn = psycopg2.connect("dbname='"+d["database"]+"' user='"+d["user"]+"' password='"+d["password"]+"' host='"+d["host"]+"' port='"+d["port"]+"'")
    cur = conn.cursor()

    cur.execute("INSERT INTO %s VALUES(%s)", (tabela, valores))
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='"+d["database"]+"' user='"+d["user"]+"' password='"+d["password"]+"' host='"+d["host"]+"' port='"+d["port"]+"'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='"+d["database"]+"' user='"+d["user"]+"' password='"+d["password"]+"' host='"+d["host"]+"' port='"+d["port"]+"'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='"+d["database"]+"' user='"+d["user"]+"' password='"+d["password"]+"' host='"+d["host"]+"' port='"+d["port"]+"'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows
