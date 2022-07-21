from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(265, 325)
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
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_import = QtWidgets.QFrame(Form)
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
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_file = QtWidgets.QFrame(self.frame_import)
        self.frame_file.setStyleSheet("QFrame {\n"
"    background-color: #3b3b3b;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"border-color:#a9a9a9;\n"
"   border-radius: 15px;\n"
"   height: 25px;\n"
"}\n"
"QPlainTextEdit {\n"
"    background-color: #c5c5c5;\n"
"        border-style: no;\n"
"border-radius:5px;\n"
"}\n"
"QLabel {\n"
"    border-style: no;\n"
"}")
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_file)
        self.gridLayout.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_importFile = QtWidgets.QPushButton(self.frame_file)
        self.btn_importFile.setMinimumSize(QtCore.QSize(180, 25))
        self.btn_importFile.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_importFile.setFont(font)
        self.btn_importFile.setStyleSheet("QPushButton:hover:!pressed\n"
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
        self.btn_importFile.setObjectName("btn_importFile")
        self.gridLayout.addWidget(self.btn_importFile, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_file)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"color:    rgb(255, 255, 0)  ;\n"
"  border-style: no;\n"
"border-radius:5px;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_file, 0, 0, 1, 1)
        self.frame_manul = QtWidgets.QFrame(self.frame_import)
        self.frame_manul.setStyleSheet("QFrame {\n"
"    background-color: #3b3b3b;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"border-color:#a9a9a9;\n"
"   border-radius: 15px;\n"
"   height: 25px;\n"
"}\n"
"QPlainTextEdit {\n"
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
        self.label_2 = QtWidgets.QLabel(self.frame_manul)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.btn_importManual = QtWidgets.QPushButton(self.frame_manul)
        self.btn_importManual.setMinimumSize(QtCore.QSize(180, 25))
        self.btn_importManual.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.btn_importManual.setFont(font)
        self.btn_importManual.setStyleSheet("QPushButton:hover:!pressed\n"
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
        self.btn_importManual.setObjectName("btn_importManual")
        self.gridLayout_2.addWidget(self.btn_importManual, 2, 1, 1, 1)
        self.manualNumber = QtWidgets.QPlainTextEdit(self.frame_manul)
        self.manualNumber.setObjectName("manualNumber")
        self.gridLayout_2.addWidget(self.manualNumber, 1, 0, 1, 3)
        self.gridLayout_3.addWidget(self.frame_manul, 1, 0, 1, 1)
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
        self.gridLayout_3.addWidget(self.btn_import_cancel, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_import, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.btn_importFile, self.manualNumber)
        Form.setTabOrder(self.manualNumber, self.btn_importManual)
        Form.setTabOrder(self.btn_importManual, self.btn_import_cancel)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "فرم ایجاد لیست شماره"))
        self.btn_importFile.setToolTip(_translate("Form", "انتخاب فایل برای بارگذاری"))
        self.btn_importFile.setText(_translate("Form", "انتخاب فایل"))
        self.label.setText(_translate("Form", "بارگزاری شماره تلفن از فایل :"))
        self.label_2.setText(_translate("Form", "ورود دستی شماره تلفن:"))
        self.btn_importManual.setToolTip(_translate("Form", "بارگذاری شماره های وارد شده"))
        self.btn_importManual.setText(_translate("Form", "بارگذاری"))
        self.manualNumber.setToolTip(_translate("Form", "شماره تلفن ها خود را وارد کنید و با فاصله خطی (Enter) از هم جدا کنید"))
        self.btn_import_cancel.setToolTip(_translate("Form", "لغو عملیات بارگذاری شماره"))
        self.btn_import_cancel.setText(_translate("Form", "لغو"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
