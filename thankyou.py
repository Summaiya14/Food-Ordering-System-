import sys
from abc import ABC,abstractmethod
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
import sqlite3

"""We have used concept of abstraction here and also we have overriden the method 'thanks' in the next class. Here __str__ method is used for overloading."""

class abstract_ThankYou(ABC):
    @abstractmethod
    def thanks(self):
        pass

class Thank_you(abstract_ThankYou):
    def thanks(self,QtWidgets,QtGuin):
        self.w = QtWidgets.QWidget()

        #Label defined
        self.thankyou=QtWidgets.QLabel(self.w)
        self.L=QtWidgets.QLabel(self.w)

        #Label set Text
        self.L.setText('THANKYOU FOR ORDERING!')

        #fontsize of label
        textfont=QFont("Times", 35)
        self.L.setFont(textfont)

        #allignment of label
        self.L.move(100,100)
        self.w.setGeometry(300,200,800,300)
        self.w.setWindowTitle('FOOD ORDERING SYSTEM')

        self.w.show()
        
    #Overloading    
    def __str__(self):
        print("Executed")

        


