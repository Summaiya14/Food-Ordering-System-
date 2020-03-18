import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
import sqlite3


"""data_base is a parent class and class of customer_details is inherited from this class. In this class we have created a database table for all the records and
details of customer. It will fetch all the data in the form of list on our IDLE shell."""

class data_base:
     def __init__(self):
         super().__init__()

     #creating table for details
     def init_ui(self):
         self.conn = sqlite3.connect("Details.db")
         self.c = self.conn.cursor()
         self.c.execute("CREATE TABLE IF NOT EXISTS details(name TEXT,phone INTEGER,address TEXT,email TEXT)")


     #data fetching
     def database(self, name, phone, address, email):
         self.conn = sqlite3.connect("Details.db")
         self.c = self.conn.cursor()
         self.c.execute("INSERT INTO details(name,phone,address,email) VALUES (?,?,?,?)", (name, phone, address, email))
         self.conn.commit()
         self.c.execute('SELECT * FROM details')
         data = self.c.fetchall()
         print(data)
         for row in data:
             print(row)
         self.c.close()
         self.conn.close()





