import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

def Check(list1, list2):
    for i in list1:
        if i in list2 and not(list2[-1] in list1):
            return 1
    return 0

class Calc(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.is_equal = False
    
    def init_UI(self):
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon("Calculator_30001.png"))
        
        self.ui.btn_1.clicked.connect(lambda: self.write_number(self.ui.btn_1.text()))
        self.ui.btn_2.clicked.connect(lambda: self.write_number(self.ui.btn_2.text()))
        self.ui.btn_3.clicked.connect(lambda: self.write_number(self.ui.btn_3.text()))
        self.ui.btn_4.clicked.connect(lambda: self.write_number(self.ui.btn_4.text()))
        self.ui.btn_5.clicked.connect(lambda: self.write_number(self.ui.btn_5.text()))
        self.ui.btn_6.clicked.connect(lambda: self.write_number(self.ui.btn_6.text()))
        self.ui.btn_7.clicked.connect(lambda: self.write_number(self.ui.btn_7.text()))
        self.ui.btn_8.clicked.connect(lambda: self.write_number(self.ui.btn_8.text()))
        self.ui.btn_9.clicked.connect(lambda: self.write_number(self.ui.btn_9.text()))
        self.ui.btn_zero.clicked.connect(lambda: self.write_number(self.ui.btn_zero.text()))
        self.ui.btn_del.clicked.connect(lambda: self.write_number(self.ui.btn_del.text()))
        self.ui.btn_multi.clicked.connect(lambda: self.write_number(self.ui.btn_multi.text()))
        self.ui.btn_plus.clicked.connect(lambda: self.write_number(self.ui.btn_plus.text()))
        self.ui.btn_minus.clicked.connect(lambda: self.write_number(self.ui.btn_minus.text()))
        
        self.ui.btn_C.clicked.connect(lambda: self.write_number(self.ui.btn_C.text()))
        self.ui.btn_back.clicked.connect(lambda: self.write_number("Backspace"))
        
        self.ui.btn_equal.clicked.connect(self.results)
    
    def write_number(self, number):
        a = ["-", "+", "*", "/"]
        if number == "C":
            self.ui.label.setText("0")
        elif number == "Backspace":
            self.ui.label.setText(self.ui.label.text()[0:-1])
        elif self.ui.label.text() == "0" or self.is_equal:
            if not number in a[1:]:
                self.ui.label.setText(number)
                self.is_equal = False
        else:
            if not (self.ui.label.text()[-1] in a and number in a[1:]):
                self.ui.label.setText(self.ui.label.text() + str(number))
          
        if Check(a, self.ui.label.text().lstrip("-")):
            self.ui.label_2.setText(str(eval(self.ui.label.text())))
        else:
            self.ui.label_2.setText(" ")
        
    def results(self):
        try:
            res = eval(self.ui.label.text())
            self.ui.label.setText(str(res))
            self.ui.label_2.setText(" ")
            self.is_equal = True
        except SyntaxError:
            pass
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Calc()
    application.show()
    sys.exit(app.exec())