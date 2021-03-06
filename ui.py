# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 640)
        MainWindow.setMinimumSize(QtCore.QSize(459, 640))
        MainWindow.setMaximumSize(QtCore.QSize(459, 640))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: rgb(39, 39, 39);\n"
"    font-family: Rubik;\n"
"    font-size: 18px;\n"
"    font-weight: 600\n"
"}\n"
"QLabel#label {\n"
"    font-size: 20px;\n"
"}\n"
"QLabel#label_2 {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(29, 29, 29);\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}\n"
"\n"
"QPushButton#btn_equal {\n"
"    background-color: rgb(0, 35, 107);\n"
"}\n"
"QPushButton#btn_equal:hover {\n"
"    background-color: rgb(0, 48, 145);\n"
"}\n"
"\n"
"QPushButton#btn_multi, #btn_del, #btn_plus, #btn_minus, #btn_C, #btn_back{\n"
"    background-color: rgb(54, 54, 54);\n"
"}\n"
"QPushButton#btn_multi:hover, #btn_del:hover, #btn_plus:hover, #btn_minus:hover, #btn_C:hover, #btn_back:hover {\n"
"    background-color: #666;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 421, 41))
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(39, 39, 39);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 421, 21))
        self.label_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(205, 205, 205);\n"
"background-color: rgb(39, 39, 39);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 190, 440, 446))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_C = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_C.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_C.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_C.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_C.setStyleSheet("")
        self.btn_C.setObjectName("btn_C")
        self.gridLayout.addWidget(self.btn_C, 0, 0, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_del.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_del.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_del.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_del.setStyleSheet("")
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.btn_del, 0, 1, 1, 1)
        self.btn_multi = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_multi.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_multi.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_multi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_multi.setStyleSheet("")
        self.btn_multi.setObjectName("btn_multi")
        self.gridLayout.addWidget(self.btn_multi, 0, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_back.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_back.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("")
        self.btn_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/backspace_FILL0_wght400_GRAD0_opsz48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(32, 32))
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 0, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_7.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setStyleSheet("")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_8.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setStyleSheet("")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_9.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_9.setStyleSheet("")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_minus.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_minus.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minus.setStyleSheet("")
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_4.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setStyleSheet("")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_5.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setStyleSheet("")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_6.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setStyleSheet("")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_plus.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_plus.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_plus.setStyleSheet("")
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 2, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_1.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet("")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_2.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet("")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_3.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setStyleSheet("")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_equal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setMinimumSize(QtCore.QSize(105, 171))
        self.btn_equal.setMaximumSize(QtCore.QSize(105, 171))
        self.btn_equal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_equal.setStyleSheet("")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 3, 3, 2, 1)
        self.btn_Heh = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Heh.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Heh.sizePolicy().hasHeightForWidth())
        self.btn_Heh.setSizePolicy(sizePolicy)
        self.btn_Heh.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_Heh.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_Heh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Heh.setStyleSheet("")
        self.btn_Heh.setObjectName("btn_Heh")
        self.gridLayout.addWidget(self.btn_Heh, 4, 0, 1, 1)
        self.btn_zero = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_zero.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_zero.sizePolicy().hasHeightForWidth())
        self.btn_zero.setSizePolicy(sizePolicy)
        self.btn_zero.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_zero.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_zero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_zero.setStyleSheet("")
        self.btn_zero.setObjectName("btn_zero")
        self.gridLayout.addWidget(self.btn_zero, 4, 1, 1, 1)
        self.btn_drob = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_drob.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_drob.sizePolicy().hasHeightForWidth())
        self.btn_drob.setSizePolicy(sizePolicy)
        self.btn_drob.setMinimumSize(QtCore.QSize(105, 84))
        self.btn_drob.setMaximumSize(QtCore.QSize(105, 84))
        self.btn_drob.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_drob.setStyleSheet("")
        self.btn_drob.setObjectName("btn_drob")
        self.gridLayout.addWidget(self.btn_drob, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", " "))
        self.btn_C.setText(_translate("MainWindow", "C"))
        self.btn_del.setText(_translate("MainWindow", "/"))
        self.btn_multi.setText(_translate("MainWindow", "*"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_Heh.setText(_translate("MainWindow", "Heh"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_drob.setText(_translate("MainWindow", ","))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
