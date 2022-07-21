from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 154)
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(9, 68, 3);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"color:    rgb(255, 255, 0)  ;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgb(4, 255, 0);\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-color: rgb(255, 136, 0);\n"
"   border-radius: 10px;\n"
"\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QToolTip {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"    border: 1px solid darkkhaki;\n"
"    border-radius: 5px;\n"
"    opacity: 0.5;\n"
"color:  rgb(0, 255, 0);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.generate_num = QtWidgets.QLineEdit(self.frame)
        self.generate_num.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.generate_num.setFont(font)
        self.generate_num.setStyleSheet("")
        self.generate_num.setAlignment(QtCore.Qt.AlignCenter)
        self.generate_num.setObjectName("generate_num")
        self.gridLayout.addWidget(self.generate_num, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"color:    rgb(255, 255, 0)  ;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.generate_count = QtWidgets.QLineEdit(self.frame)
        self.generate_count.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.generate_count.setFont(font)
        self.generate_count.setAlignment(QtCore.Qt.AlignCenter)
        self.generate_count.setObjectName("generate_count")
        self.gridLayout.addWidget(self.generate_count, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_g_cancel = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_g_cancel.setFont(font)
        self.btn_g_cancel.setStyleSheet("QPushButton:hover:!pressed\n"
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
        self.btn_g_cancel.setObjectName("btn_g_cancel")
        self.gridLayout_3.addWidget(self.btn_g_cancel, 0, 0, 1, 1)
        self.btn_g_ok = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_g_ok.setFont(font)
        self.btn_g_ok.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(0, 92, 67);\n"
"color: rgb(255, 255, 127);\n"
"border: 1px solid  #55ffff;;\n"
"border-radius: 10px;\n"
"}")
        self.btn_g_ok.setAutoDefault(True)
        self.btn_g_ok.setDefault(True)
        self.btn_g_ok.setObjectName("btn_g_ok")
        self.gridLayout_3.addWidget(self.btn_g_ok, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.generate_num, self.generate_count)
        Form.setTabOrder(self.generate_count, self.btn_g_ok)
        Form.setTabOrder(self.btn_g_ok, self.btn_g_cancel)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "فرم ایجاد لیست شماره"))
        self.generate_num.setToolTip(_translate("Form", "اولین شماره مورد نظر خود را بدون 0 وارد کنید"))
        self.generate_num.setPlaceholderText(_translate("Form", "9123456789"))
        self.label.setText(_translate("Form", "اولین شماره :"))
        self.generate_count.setToolTip(_translate("Form", "تعداد مورد نظر خود برای ایجاد لیست شماره ها وارد کنید"))
        self.generate_count.setPlaceholderText(_translate("Form", "10"))
        self.label_2.setText(_translate("Form", "تعداد ایجاد    :"))
        self.btn_g_cancel.setToolTip(_translate("Form", "لغو عملیات"))
        self.btn_g_cancel.setText(_translate("Form", "لغو"))
        self.btn_g_ok.setToolTip(_translate("Form", "ایجاد لیست"))
        self.btn_g_ok.setText(_translate("Form", "تایید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
