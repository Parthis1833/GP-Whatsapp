from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(308, 392)
        Form.setStyleSheet("QLabel {\n"
"color:    rgb(255, 255, 0)  ;\n"
"}\n"
"\n"
"QToolTip {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"    border: 1px solid darkkhaki;\n"
"    border-radius: 5px;\n"
"    opacity: 0.5;\n"
"color:  rgb(0, 255, 0);\n"
"}")
        self.frame_import = QtWidgets.QFrame(Form)
        self.frame_import.setGeometry(QtCore.QRect(9, 9, 296, 378))
        self.frame_import.setStyleSheet("QFrame {\n"
"    background-color: #2b2b2b;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"border-color:#a9a9a9;\n"
"   border-radius: 10px;\n"
"   height: 25px;\n"
"}")
        self.frame_import.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_import.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_import.setObjectName("frame_import")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_import)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_import_cancel = QtWidgets.QPushButton(self.frame_import)
        self.btn_import_cancel.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.btn_import_cancel.setFont(font)
        self.btn_import_cancel.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid rgb(255, 85, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(205, 68, 102);\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid  #55ffff;;\n"
"border-radius: 10px;\n"
"}")
        self.btn_import_cancel.setAutoDefault(True)
        self.btn_import_cancel.setDefault(True)
        self.btn_import_cancel.setObjectName("btn_import_cancel")
        self.gridLayout_3.addWidget(self.btn_import_cancel, 3, 0, 1, 1)
        self.frame_manul = QtWidgets.QFrame(self.frame_import)
        self.frame_manul.setStyleSheet("QFrame {\n"
"    background-color: #3b3b3b;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"border-color:#a9a9a9;\n"
"   border-radius: 15px;\n"
"   height: 25px;\n"
"}\n"
"QTableView {\n"
"    background-color: #c5c5c5;\n"
"        border-style: no;\n"
"border-radius:5px;\n"
"color: rgb(121, 2, 180) ; \n"
"}\n"
"\n"
"QLabel {\n"
"  border-style: no;\n"
"border-radius:5px;\n"
"}")
        self.frame_manul.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_manul.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_manul.setObjectName("frame_manul")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_manul)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.accountsTable = QtWidgets.QTableView(self.frame_manul)
        self.accountsTable.setObjectName("accountsTable")
        self.gridLayout_2.addWidget(self.accountsTable, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_manul)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_manul, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_import)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_addnewtel = QtWidgets.QLineEdit(self.frame)
        self.btn_addnewtel.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_addnewtel.setFont(font)
        self.btn_addnewtel.setStyleSheet("QLineEdit{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-color: rgb(255, 136, 0);\n"
"   border-radius: 7px;\n"
"}")
        self.btn_addnewtel.setObjectName("btn_addnewtel")
        self.gridLayout.addWidget(self.btn_addnewtel, 0, 0, 1, 1)
        self.btn_importaccount = QtWidgets.QPushButton(self.frame)
        self.btn_importaccount.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_importaccount.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_importaccount.setFont(font)
        self.btn_importaccount.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid rgb(0, 209, 255);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 92, 67);\n"
"color: rgb(255, 204, 0);\n"
"border: 1px solid  rgb(234, 0, 255);;\n"
"border-radius: 10px;\n"
"}")
        self.btn_importaccount.setObjectName("btn_importaccount")
        self.gridLayout.addWidget(self.btn_importaccount, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "فرم ایجاد لیست شماره"))
        self.btn_import_cancel.setToolTip(_translate("Form", "لغو عملیات بارگذاری شماره"))
        self.btn_import_cancel.setText(_translate("Form", "بستن"))
        self.label_2.setText(_translate("Form", "لیست اکانت های ذخیره شده:"))
        self.btn_addnewtel.setPlaceholderText(_translate("Form", "شماره اکانت جدید"))
        self.btn_importaccount.setToolTip(_translate("Form", "انتخاب فایل برای بارگذاری"))
        self.btn_importaccount.setText(_translate("Form", "افزودن اکانت جدید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
