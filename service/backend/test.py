import package_table
import sqlite3

def connect_db():
  conn = sqlite3.connect('shopping.db')
  c = conn.cursor()
  return c

def insert_goods(name, price, description):
  conn = sqlite3.connect('shopping.db')
  c = conn.cursor()
  c.execute("INSERT INTO Goods (name, price, description) VALUES (?, ?, ?)", (name, price, description))
  conn.commit()
  conn.close()

def insert_package(place, status_time, status, goods_id):
  conn = sqlite3.connect('shopping.db')
  c = conn.cursor()
  c.execute("INSERT INTO Package (place, status_time, status, goods_id) VALUES (?, ?, ?, ?)", (place, status_time, status, goods_id))
  conn.commit()
  conn.close()
  return c.lastrowid

#package_table.create_db()
insert_goods('apple', 10, 'red')
insert_goods('banana', 20, 'yellow')
insert_goods('orange', 30, 'orange')


