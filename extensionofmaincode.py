import sys
from restaurants import Restaurant
from dbclass import data_base
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
import sqlite3



"""In this class we have defined all the details of customer like name,phone,address,email. Basically Customer_details class is the subclass of data_base(parent class).
"""
class Customer_Details(data_base,QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

    def init_ui(self,QtWidgets,QtGui):
        self.w = QtWidgets.QWidget()

        
        #LineEdits defined
        self.name=QtWidgets.QLineEdit(self.w)
        self.phone=QtWidgets.QLineEdit(self.w)
        self.address=QtWidgets.QLineEdit(self.w)
        self.email=QtWidgets.QLineEdit(self.w)
        self.area_btn=QtWidgets.QPushButton(self.w)
        self.area_btn.setText("Proceed Further")

        #Labels defined
        self.customerdetails=QtWidgets.QLabel(self.w)
        self.L1=QtWidgets.QLabel(self.w)
        self.L2=QtWidgets.QLabel(self.w)
        self.L3=QtWidgets.QLabel(self.w)
        self.L4=QtWidgets.QLabel(self.w)

        #Labels set TEXT
        self.L1.setText('Customer Name:')
        self.L2.setText('Customer Mobile No: ')
        self.L3.setText('Customer Email: ')
        self.L4.setText('Customer Address: ')
        
                

        
        #setting fontsize 
        textfont=QFont("Calibiri", 16)
        self.L1.setFont(textfont)
        self.L2.setFont(textfont)
        self.L3.setFont(textfont)
        self.L4.setFont(textfont)
        self.pic1=QtWidgets.QLabel(self.w)
        self.pic1.setPixmap(QtGui.QPixmap('icon'))
        self.pic1.move(0,0)

        #allignment of labels
        self.L1.move(10,250)
        self.L2.move(400,250)
        self.L3.move(415,295)
        self.L4.move(10,295)
        self.area_btn.setGeometry(220,330,400,20)
        self.area_btn.clicked.connect(self.btn_click)
        self.name.setGeometry(190,255,200,20)
        self.phone.setGeometry(600,255,200,20)
        self.address.setGeometry(600,300,200,20)
        self.email.setGeometry(190,300,200,20)
        self.w.setGeometry(240,150,820,360)

        self.w.setWindowTitle('FOOD ORDERING SYSTEM')

        self.w.show()


        
    
    def btn_click(self):
            try:
                a = self.name.text()
                b = self.phone.text()
                c = self.address.text()
                d = self.email.text()
                if a.isdigit() or b=='' or c=='' or d=='':
                    raise Exception('INVALID INPUT')
                else:
                    self.database(self.name.text(), self.phone.text(), self.address.text(), self.email.text())
                    self.w=QtWidgets.QWidget()
                    self.w.setWindowTitle('Restaurant Selection')
                    

                    #Buttons defined
                    self.b1=QtWidgets.QPushButton(self.w)
                    self.b2=QtWidgets.QPushButton(self.w)
                    self.b3=QtWidgets.QPushButton(self.w)
                    self.b4=QtWidgets.QPushButton(self.w)
                    self.b5=QtWidgets.QPushButton(self.w)
                    self.b6=QtWidgets.QPushButton(self.w)
                    self.b1.clicked.connect(self.btn_clicked1)
                    self.b2.clicked.connect(self.btn_clicked2)
                    self.b3.clicked.connect(self.btn_clicked3)
                    self.b4.clicked.connect(self.btn_clicked4)
                    self.b5.clicked.connect(self.btn_clicked5)
                    self.b6.clicked.connect(self.btn_clicked6)

                    #setting text for buttons
                    self.b1.setText("Student Biryani")
                    self.b2.setText("McDonald's")
                    self.b3.setText("Burger Lab")
                    self.b4.setText("Pizza Max")
                    self.b5.setText("Del Frio")
                    self.b6.setText("Shaheen Shinwari")
                    
                    #allignment of buttons
                    self.b1.setGeometry(0,10,200,100)
                    self.b2.setGeometry(200,10,200,100)
                    self.b3.setGeometry(400,10,200,100)
                    self.b4.setGeometry(0,110,200,100)
                    self.b5.setGeometry(200,110,200,100)
                    self.b6.setGeometry(400,110,200,100)

                    self.w.setGeometry(390,210,600,220)
                    self.w.show()
            except Exception:
                    QMessageBox.question(self, 'Error', "Either Wrong Input Is Given Or Fields Are Empty ", QMessageBox.Yes | QMessageBox.Yes, QMessageBox.Yes)
                    print("Exception Raised")

    
    #button clicks for all restaurants        
    def btn_clicked1(self):
        self.det=Restaurant()
        self.det.Student_Biryani(QtWidgets,QtGui)
    def btn_clicked2(self):
        self.det=Restaurant()
        self.det.McDonalds(QtWidgets,QtGui)
    def btn_clicked3(self):
        self.det=Restaurant()
        self.det.burgerlab(QtWidgets,QtGui)
    def btn_clicked4(self):
        self.det=Restaurant()
        self.det.pizzamax(QtWidgets,QtGui)
    def btn_clicked5(self):
        self.det=Restaurant()
        self.det.del_frio(QtWidgets,QtGui)
    def btn_clicked6(self):
        self.det=Restaurant()
        self.det.shaheen_shinwari(QtWidgets,QtGui)





app=QtWidgets.QApplication(sys.argv)
det=Customer_Details()
det.init_ui(QtWidgets,QtGui)
sys.exit(app.exec_())
