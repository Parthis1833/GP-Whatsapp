from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 708)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QToolTip {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"    border: 1px solid darkkhaki;\n"
"    border-radius: 2px;\n"
"    opacity: 0.5;\n"
"color:  rgb(0, 255, 0);\n"
"}")
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setStyleSheet("QWidget {\n"
"background-color: rgb(44, 171, 37);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QTableView {\n"
"background-color: rgb(253, 255, 197);\n"
"}")
        self.Main.setObjectName("Main")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.Main)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.frame_msg = QtWidgets.QFrame(self.Main)
        self.frame_msg.setMinimumSize(QtCore.QSize(335, 0))
        self.frame_msg.setStyleSheet("QFrame {\n"
"background-color: rgb(63, 78, 64) ;\n"
"}")
        self.frame_msg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_msg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_msg.setObjectName("frame_msg")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_msg)
        self.gridLayout_8.setContentsMargins(4, 6, 4, 5)
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_numLebel = QtWidgets.QFrame(self.frame_msg)
        self.frame_numLebel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_numLebel.setStyleSheet("QFrame {\n"
"background-color: rgb(207, 223, 162);\n"
"}")
        self.frame_numLebel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_numLebel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_numLebel.setObjectName("frame_numLebel")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_numLebel)
        self.gridLayout_10.setContentsMargins(7, 0, -1, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.whatsAppNumbers = QtWidgets.QLabel(self.frame_numLebel)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.whatsAppNumbers.setFont(font)
        self.whatsAppNumbers.setObjectName("whatsAppNumbers")
        self.horizontalLayout_4.addWidget(self.whatsAppNumbers)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_10.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_numLebel, 0, 0, 1, 1)
        self.tableview_numbers = QtWidgets.QTableView(self.frame_msg)
        self.tableview_numbers.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableview_numbers.setFont(font)
        self.tableview_numbers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableview_numbers.setStyleSheet("QTableView {\n"
"background-color: rgb(63, 78, 64) ;\n"
"color: rgb(0, 174, 255) ;\n"
"}")
        self.tableview_numbers.setAutoScrollMargin(16)
        self.tableview_numbers.setObjectName("tableview_numbers")
        self.gridLayout_8.addWidget(self.tableview_numbers, 1, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frame_msg, 1, 0, 1, 1)
        self.frame_btn = QtWidgets.QFrame(self.Main)
        self.frame_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_btn.setStyleSheet("QFrame {\n"
"background-color: rgb(63, 78, 64) ;\n"
"}")
        self.frame_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn.setObjectName("frame_btn")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_btn)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_import = QtWidgets.QPushButton(self.frame_btn)
        self.btn_import.setEnabled(True)
        self.btn_import.setMinimumSize(QtCore.QSize(25, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_import.setFont(font)
        self.btn_import.setMouseTracking(False)
        self.btn_import.setStatusTip("")
        self.btn_import.setWhatsThis("")
        self.btn_import.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(16, 255, 196);\n"
"border-radius: 10px;\n"
"}")
        self.btn_import.setObjectName("btn_import")
        self.horizontalLayout.addWidget(self.btn_import)
        self.btn_gnarate = QtWidgets.QPushButton(self.frame_btn)
        self.btn_gnarate.setEnabled(True)
        self.btn_gnarate.setMinimumSize(QtCore.QSize(25, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_gnarate.setFont(font)
        self.btn_gnarate.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(16, 255, 196);\n"
"border-radius: 10px;\n"
"}")
        self.btn_gnarate.setObjectName("btn_gnarate")
        self.horizontalLayout.addWidget(self.btn_gnarate)
        self.btn_export = QtWidgets.QPushButton(self.frame_btn)
        self.btn_export.setEnabled(False)
        self.btn_export.setMinimumSize(QtCore.QSize(25, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_export.setFont(font)
        self.btn_export.setStatusTip("")
        self.btn_export.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(16, 255, 196);\n"
"border-radius: 10px;\n"
"}")
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout.addWidget(self.btn_export)
        self.btn_clear = QtWidgets.QPushButton(self.frame_btn)
        self.btn_clear.setEnabled(False)
        self.btn_clear.setMinimumSize(QtCore.QSize(25, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(16, 255, 196);\n"
"border-radius: 10px;\n"
"}")
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.btn_acclist = QtWidgets.QPushButton(self.frame_btn)
        self.btn_acclist.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_acclist.setFont(font)
        self.btn_acclist.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(129, 125, 255);\n"
"    color: #FF0000;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(16, 255, 196);\n"
"border-radius: 10px;\n"
"}")
        self.btn_acclist.setObjectName("btn_acclist")
        self.gridLayout_3.addWidget(self.btn_acclist, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_tab = QtWidgets.QTabWidget(self.frame_btn)
        self.start_tab.setEnabled(True)
        self.start_tab.setToolTip("")
        self.start_tab.setAccessibleName("")
        self.start_tab.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.start_tab.setStyleSheet("QTabWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.start_tab.setObjectName("start_tab")
        self.tab_Analyz = QtWidgets.QWidget()
        self.tab_Analyz.setStyleSheet("QWidget {\n"
"background-color: rgb(234, 255, 201);\n"
"border-radius: 5px;\n"
"}\n"
"QPlainTextEdit {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 255, 29);\n"
"}")
        self.tab_Analyz.setObjectName("tab_Analyz")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_Analyz)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_Analyz)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_16.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.start_tab.addTab(self.tab_Analyz, "")
        self.tab_msg = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_msg.setFont(font)
        self.tab_msg.setStyleSheet("QWidget {\n"
"background-color:rgb(234, 255, 201);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(234, 255, 201);\n"
"color:rgb(0, 0, 255);\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-color: rgb(255, 136, 0);\n"
"   border-radius: 10px;\n"
"}")
        self.tab_msg.setObjectName("tab_msg")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_msg)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.tab_msg)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color:  rgb(170, 0, 255);\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.frame_sleep = QtWidgets.QFrame(self.tab_msg)
        self.frame_sleep.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_sleep.setStyleSheet("QFrame {\n"
"background-color: rgb(247, 212, 255)  ;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(74, 78, 31) ;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(247, 212, 255)  ;\n"
"}")
        self.frame_sleep.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sleep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sleep.setObjectName("frame_sleep")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_sleep)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_sleep)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)
        self.sleepMax = QtWidgets.QLineEdit(self.frame_sleep)
        self.sleepMax.setMinimumSize(QtCore.QSize(30, 0))
        self.sleepMax.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sleepMax.setFont(font)
        self.sleepMax.setStyleSheet("")
        self.sleepMax.setAlignment(QtCore.Qt.AlignCenter)
        self.sleepMax.setObjectName("sleepMax")
        self.gridLayout_2.addWidget(self.sleepMax, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_sleep)
        self.label_3.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.sleepMin = QtWidgets.QLineEdit(self.frame_sleep)
        self.sleepMin.setMinimumSize(QtCore.QSize(30, 0))
        self.sleepMin.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sleepMin.setFont(font)
        self.sleepMin.setStyleSheet("")
        self.sleepMin.setAlignment(QtCore.Qt.AlignCenter)
        self.sleepMin.setObjectName("sleepMin")
        self.gridLayout_2.addWidget(self.sleepMin, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_sleep)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 3)
        self.gridLayout_4.addWidget(self.frame_sleep, 2, 0, 1, 1)
        self.textMSG = QtWidgets.QTextEdit(self.tab_msg)
        self.textMSG.setMinimumSize(QtCore.QSize(200, 0))
        self.textMSG.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textMSG.setFont(font)
        self.textMSG.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textMSG.setStyleSheet("QTextEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.textMSG.setObjectName("textMSG")
        self.gridLayout_4.addWidget(self.textMSG, 1, 0, 1, 1)
        self.start_tab.addTab(self.tab_msg, "")
        self.tab_img = QtWidgets.QWidget()
        self.tab_img.setStyleSheet("QWidget {\n"
"background-color: rgb(234, 255, 201);\n"
"border-radius: 5px;\n"
"}\n"
"QPlainTextEdit {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 255, 29);\n"
"}")
        self.tab_img.setObjectName("tab_img")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_img)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_img = QtWidgets.QFrame(self.tab_img)
        self.frame_img.setStyleSheet("QFrame  {\n"
"background-color: rgb(234, 255, 201);\n"
"border-radius: 5px;\n"
"}")
        self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_img.setObjectName("frame_img")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_img)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(5)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_img_2 = QtWidgets.QFrame(self.frame_img)
        self.frame_img_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_img_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_img_2.setObjectName("frame_img_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_img_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_img = QtWidgets.QPushButton(self.frame_img_2)
        self.btn_img.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_img.setFont(font)
        self.btn_img.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_img.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px dashed rgb(255, 85, 0);\n"
"    background-color: rgb(182, 182, 182);\n"
"    color: rgb(7, 255, 77);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 170, 127);\n"
"border-radius: 10px;\n"
"color: rgb(51, 0, 255)  ;\n"
"}")
        self.btn_img.setObjectName("btn_img")
        self.horizontalLayout_3.addWidget(self.btn_img)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.caption = QtWidgets.QTextEdit(self.frame_img_2)
        self.caption.setMaximumSize(QtCore.QSize(16777215, 30))
        self.caption.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.caption.setStyleSheet("QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.caption.setPlaceholderText("")
        self.caption.setObjectName("caption")
        self.gridLayout_9.addWidget(self.caption, 2, 0, 1, 2)
        self.imgShow = QtWidgets.QLabel(self.frame_img_2)
        self.imgShow.setMinimumSize(QtCore.QSize(0, 120))
        self.imgShow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imgShow.setText("")
        self.imgShow.setAlignment(QtCore.Qt.AlignCenter)
        self.imgShow.setObjectName("imgShow")
        self.gridLayout_9.addWidget(self.imgShow, 3, 0, 1, 1)
        self.imgName = QtWidgets.QLabel(self.frame_img_2)
        self.imgName.setStyleSheet("QLabel {\n"
"color:  rgb(158, 2, 255)  ;\n"
"}")
        self.imgName.setText("")
        self.imgName.setAlignment(QtCore.Qt.AlignCenter)
        self.imgName.setObjectName("imgName")
        self.gridLayout_9.addWidget(self.imgName, 3, 1, 1, 1)
        self.label_caption = QtWidgets.QLabel(self.frame_img_2)
        self.label_caption.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_caption.setObjectName("label_caption")
        self.gridLayout_9.addWidget(self.label_caption, 1, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_img_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.frame_img)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setStyleSheet("QLineEdit{\n"
"background-color: rgb(234, 255, 201);\n"
"color:rgb(0, 0, 255);\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-bottom-color: rgb(255, 136, 0);\n"
"   border-radius: 10px;\n"
"}\n"
"\n"
"QFrame {\n"
"background-color: rgb(247, 212, 255)  ;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(74, 78, 31) ;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(247, 212, 255)  ;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 3)
        self.sleepMax_I = QtWidgets.QLineEdit(self.frame)
        self.sleepMax_I.setMinimumSize(QtCore.QSize(30, 0))
        self.sleepMax_I.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sleepMax_I.setFont(font)
        self.sleepMax_I.setStyleSheet("")
        self.sleepMax_I.setAlignment(QtCore.Qt.AlignCenter)
        self.sleepMax_I.setObjectName("sleepMax_I")
        self.gridLayout_5.addWidget(self.sleepMax_I, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setMaximumSize(QtCore.QSize(20, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 1, 1, 1)
        self.sleepMin_I = QtWidgets.QLineEdit(self.frame)
        self.sleepMin_I.setMinimumSize(QtCore.QSize(30, 0))
        self.sleepMin_I.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sleepMin_I.setFont(font)
        self.sleepMin_I.setStyleSheet("")
        self.sleepMin_I.setAlignment(QtCore.Qt.AlignCenter)
        self.sleepMin_I.setObjectName("sleepMin_I")
        self.gridLayout_5.addWidget(self.sleepMin_I, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 3)
        self.gridLayout_14.addWidget(self.frame, 1, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_img, 0, 0, 1, 1)
        self.start_tab.addTab(self.tab_img, "")
        self.horizontalLayout_2.addWidget(self.start_tab)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frame_btn, 1, 1, 1, 1)
        self.frame_botton_controller = QtWidgets.QFrame(self.Main)
        self.frame_botton_controller.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_botton_controller.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_botton_controller.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_botton_controller.setStyleSheet("QFrame {\n"
"background-color: rgb(63, 78, 64) ;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(46, 255, 0);\n"
"}")
        self.frame_botton_controller.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botton_controller.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botton_controller.setObjectName("frame_botton_controller")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_botton_controller)
        self.gridLayout_7.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_7.setSpacing(4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.btn_start = QtWidgets.QPushButton(self.frame_botton_controller)
        self.btn_start.setMinimumSize(QtCore.QSize(250, 80))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 4px dashed rgb(0, 85, 255);\n"
"    background-color: rgb(198, 253, 200);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"QPushButton{\n"
"  border: 2px solid  rgb(226, 157, 255);\n"
"    background-color: rgb(105, 210, 76);\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.btn_start.setAutoDefault(True)
        self.btn_start.setDefault(True)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout_7.addWidget(self.btn_start, 0, 0, 1, 1)
        self.LogBox = QtWidgets.QPlainTextEdit(self.frame_botton_controller)
        self.LogBox.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.LogBox.setFont(font)
        self.LogBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LogBox.setStyleSheet("")
        self.LogBox.setObjectName("LogBox")
        self.gridLayout_7.addWidget(self.LogBox, 0, 1, 2, 1)
        self.frame_LCD = QtWidgets.QFrame(self.frame_botton_controller)
        self.frame_LCD.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_LCD.setStyleSheet("QFrame{\n"
"background-color: rgb(191, 191, 0) ;\n"
"}")
        self.frame_LCD.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LCD.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LCD.setObjectName("frame_LCD")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_LCD)
        self.gridLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lcdNumber_reviewed = QtWidgets.QLCDNumber(self.frame_LCD)
        self.lcdNumber_reviewed.setStyleSheet("QLCDNumber{\n"
"color: rgb(0, 0, 0) ;\n"
"}")
        self.lcdNumber_reviewed.setObjectName("lcdNumber_reviewed")
        self.gridLayout_11.addWidget(self.lcdNumber_reviewed, 1, 0, 1, 1)
        self.lcdNumber_wa = QtWidgets.QLCDNumber(self.frame_LCD)
        self.lcdNumber_wa.setStyleSheet("QLCDNumber {\n"
"color:rgb(0, 255, 0);\n"
"}")
        self.lcdNumber_wa.setObjectName("lcdNumber_wa")
        self.gridLayout_11.addWidget(self.lcdNumber_wa, 2, 0, 1, 1)
        self.lcdNumber_nwa = QtWidgets.QLCDNumber(self.frame_LCD)
        self.lcdNumber_nwa.setStyleSheet("QLCDNumber{\n"
"color: rgb(255, 2, 18) ;\n"
"}")
        self.lcdNumber_nwa.setObjectName("lcdNumber_nwa")
        self.gridLayout_11.addWidget(self.lcdNumber_nwa, 3, 0, 1, 1)
        self.lcdNumber_allCount = QtWidgets.QLCDNumber(self.frame_LCD)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber_allCount.setFont(font)
        self.lcdNumber_allCount.setStyleSheet("QLCDNumber{\n"
"color: rgb(0, 0, 255) ;\n"
"}")
        self.lcdNumber_allCount.setObjectName("lcdNumber_allCount")
        self.gridLayout_11.addWidget(self.lcdNumber_allCount, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_LCD, 0, 2, 2, 1)
        self.frame_LCD_label = QtWidgets.QFrame(self.frame_botton_controller)
        self.frame_LCD_label.setStyleSheet("QFrame{\n"
"background-color: rgb(191, 191, 0);\n"
"border-radius: 10px;\n"
"}")
        self.frame_LCD_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_LCD_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_LCD_label.setObjectName("frame_LCD_label")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_LCD_label)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_count_txt_5 = QtWidgets.QLabel(self.frame_LCD_label)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_count_txt_5.setFont(font)
        self.label_count_txt_5.setObjectName("label_count_txt_5")
        self.gridLayout.addWidget(self.label_count_txt_5, 4, 0, 1, 1)
        self.label_count_txt_3 = QtWidgets.QLabel(self.frame_LCD_label)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_count_txt_3.setFont(font)
        self.label_count_txt_3.setObjectName("label_count_txt_3")
        self.gridLayout.addWidget(self.label_count_txt_3, 2, 0, 1, 1)
        self.label_count_txt_4 = QtWidgets.QLabel(self.frame_LCD_label)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_count_txt_4.setFont(font)
        self.label_count_txt_4.setObjectName("label_count_txt_4")
        self.gridLayout.addWidget(self.label_count_txt_4, 3, 0, 1, 1)
        self.label_count_txt = QtWidgets.QLabel(self.frame_LCD_label)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_count_txt.setFont(font)
        self.label_count_txt.setStyleSheet("")
        self.label_count_txt.setObjectName("label_count_txt")
        self.gridLayout.addWidget(self.label_count_txt, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_LCD_label, 0, 3, 2, 1)
        self.btn_stop = QtWidgets.QPushButton(self.frame_botton_controller)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setMinimumSize(QtCore.QSize(120, 20))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"  border: 4px dashed rgb(255, 0, 0);\n"
"    background-color: rgb(251, 255, 211);\n"
"    color: rgb(255, 5, 5);\n"
"}\n"
"QPushButton{\n"
"  border: 3px double rgb(255, 227, 112);\n"
"    background-color: rgb(255, 170, 0);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.btn_stop.setObjectName("btn_stop")
        self.gridLayout_7.addWidget(self.btn_stop, 1, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frame_botton_controller, 2, 0, 1, 2)
        self.frame_TabBar = QtWidgets.QFrame(self.Main)
        self.frame_TabBar.setStyleSheet("QFrame{\n"
"    background-color: rgb(44, 171, 37);\n"
"}\n"
"\n"
"QLabel{\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.frame_TabBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TabBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TabBar.setObjectName("frame_TabBar")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_TabBar)
        self.gridLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lb_version = QtWidgets.QLabel(self.frame_TabBar)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.lb_version.setFont(font)
        self.lb_version.setText("")
        self.lb_version.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lb_version.setObjectName("lb_version")
        self.gridLayout_12.addWidget(self.lb_version, 0, 1, 1, 1)
        self.btn_maxmin = QtWidgets.QPushButton(self.frame_TabBar)
        self.btn_maxmin.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_maxmin.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setFamily("MesloLGS NF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_maxmin.setFont(font)
        self.btn_maxmin.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(3, 255, 74);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.btn_maxmin.setObjectName("btn_maxmin")
        self.gridLayout_12.addWidget(self.btn_maxmin, 0, 6, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.frame_TabBar)
        self.btn_close.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_close.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setFamily("MesloLGS NF")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(255, 12, 16);\n"
"    color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.btn_close.setObjectName("btn_close")
        self.gridLayout_12.addWidget(self.btn_close, 0, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem4, 0, 2, 1, 1)
        self.lang = QtWidgets.QComboBox(self.frame_TabBar)
        self.lang.setMinimumSize(QtCore.QSize(40, 0))
        self.lang.setStyleSheet("QComboBox{\n"
"background-color: #eee1c5   ;\n"
"color:rgb(30, 0, 255);\n"
"border: 1px solid #096578  ;\n"
"border-radius: 2px;\n"
"}")
        self.lang.setObjectName("lang")
        self.lang.addItem("")
        self.lang.addItem("")
        self.gridLayout_12.addWidget(self.lang, 0, 4, 1, 1)
        self.btn_min = QtWidgets.QPushButton(self.frame_TabBar)
        self.btn_min.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_min.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setFamily("MesloLGS NF")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(100, 50, 0);\n"
"    color: rgb(248, 44, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.btn_min.setObjectName("btn_min")
        self.gridLayout_12.addWidget(self.btn_min, 0, 5, 1, 1)
        self.label_appName = QtWidgets.QLabel(self.frame_TabBar)
        font = QtGui.QFont()
        font.setFamily("African")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_appName.setFont(font)
        self.label_appName.setStyleSheet("QLabel:hover:!pressed\n"
"{\n"
"    color: rgb(255, 213, 0);\n"
"}\n"
"")
        self.label_appName.setObjectName("label_appName")
        self.gridLayout_12.addWidget(self.label_appName, 0, 0, 1, 1)
        self.areaCode = QtWidgets.QLineEdit(self.frame_TabBar)
        self.areaCode.setMinimumSize(QtCore.QSize(20, 0))
        self.areaCode.setMaximumSize(QtCore.QSize(30, 16777215))
        self.areaCode.setStyleSheet("QLineEdit{\n"
"background-color: #eee1c5   ;\n"
"color:rgb(30, 0, 255);\n"
"border: 1px solid #096578  ;\n"
"border-radius: 3px;\n"
"}")
        self.areaCode.setObjectName("areaCode")
        self.gridLayout_12.addWidget(self.areaCode, 0, 3, 1, 1)
        self.gridLayout_13.addWidget(self.frame_TabBar, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        self.start_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_import, self.btn_gnarate)
        MainWindow.setTabOrder(self.btn_gnarate, self.btn_export)
        MainWindow.setTabOrder(self.btn_export, self.btn_clear)
        MainWindow.setTabOrder(self.btn_clear, self.start_tab)
        MainWindow.setTabOrder(self.start_tab, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.btn_start)
        MainWindow.setTabOrder(self.btn_start, self.btn_stop)
        MainWindow.setTabOrder(self.btn_stop, self.textMSG)
        MainWindow.setTabOrder(self.textMSG, self.sleepMin)
        MainWindow.setTabOrder(self.sleepMin, self.sleepMax)
        MainWindow.setTabOrder(self.sleepMax, self.btn_img)
        MainWindow.setTabOrder(self.btn_img, self.caption)
        MainWindow.setTabOrder(self.caption, self.sleepMin_I)
        MainWindow.setTabOrder(self.sleepMin_I, self.sleepMax_I)
        MainWindow.setTabOrder(self.sleepMax_I, self.tableview_numbers)
        MainWindow.setTabOrder(self.tableview_numbers, self.LogBox)
        MainWindow.setTabOrder(self.LogBox, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.btn_maxmin)
        MainWindow.setTabOrder(self.btn_maxmin, self.btn_min)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WhatsApp Sender"))
        self.frame_msg.setToolTip(_translate("MainWindow", "لیست شماره های که در برنامه بررسی می شوند"))
        self.whatsAppNumbers.setText(_translate("MainWindow", " لیست شماره ها "))
        self.btn_import.setToolTip(_translate("MainWindow", "بارگذاری لیست شماره ها"))
        self.btn_import.setText(_translate("MainWindow", "بارگذاری"))
        self.btn_gnarate.setToolTip(_translate("MainWindow", "ایجاد از یک رنج شماره "))
        self.btn_gnarate.setText(_translate("MainWindow", "ایجاد لیست"))
        self.btn_export.setToolTip(_translate("MainWindow", "خروجی گرفتن از نتایج برنامه"))
        self.btn_export.setText(_translate("MainWindow", "استخراج"))
        self.btn_clear.setToolTip(_translate("MainWindow", "پاک کردن لیست شماره ها"))
        self.btn_clear.setText(_translate("MainWindow", "پاک کردن"))
        self.btn_acclist.setText(_translate("MainWindow", "لیست اکانت ها"))
        self.tab_Analyz.setToolTip(_translate("MainWindow", "تحلیل لیست شماره ها"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#000000;\">شما با استفاده از امکان آنالیز شماره ها می تونید لیست شماره های خود را مورد بررسی قرار دهید تا برنامه شماره های که دارای حساب کاربری واتساپ می باشند را شناسایی کند</span></p></body></html>"))
        self.start_tab.setTabText(self.start_tab.indexOf(self.tab_Analyz), _translate("MainWindow", "آنالیز شماره ها"))
        self.tab_msg.setToolTip(_translate("MainWindow", "ارسال پیام متنی"))
        self.label.setText(_translate("MainWindow", "متن پیام"))
        self.label_2.setText(_translate("MainWindow", "زمان وقفه هر ارسال بین"))
        self.sleepMax.setToolTip(_translate("MainWindow", "بیشترین زمان وقفه "))
        self.sleepMax.setPlaceholderText(_translate("MainWindow", "6"))
        self.label_3.setText(_translate("MainWindow", " و"))
        self.sleepMin.setToolTip(_translate("MainWindow", "کمترین زمان وقفه"))
        self.sleepMin.setPlaceholderText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "ثانیه تنظیم می شود"))
        self.textMSG.setToolTip(_translate("MainWindow", "متن پیام شما برای ارسال"))
        self.start_tab.setTabText(self.start_tab.indexOf(self.tab_msg), _translate("MainWindow", "پیام متنی"))
        self.tab_img.setToolTip(_translate("MainWindow", "ارسال تصویر"))
        self.btn_img.setToolTip(_translate("MainWindow", "انتخاب تصویر برای ارسال"))
        self.btn_img.setText(_translate("MainWindow", "انتخاب تصویر"))
        self.caption.setToolTip(_translate("MainWindow", "کپشن تصویر مورد نظر شما"))
        self.label_caption.setText(_translate("MainWindow", "درصورت نیاز کپشن خود را وارد کنید:"))
        self.label_11.setText(_translate("MainWindow", "زمان وقفه هر ارسال بین"))
        self.sleepMax_I.setToolTip(_translate("MainWindow", "بیشترین زمان وقفه "))
        self.sleepMax_I.setPlaceholderText(_translate("MainWindow", "6"))
        self.label_10.setText(_translate("MainWindow", " و"))
        self.sleepMin_I.setToolTip(_translate("MainWindow", "کمترین زمان وقفه"))
        self.sleepMin_I.setPlaceholderText(_translate("MainWindow", "3"))
        self.label_12.setText(_translate("MainWindow", "ثانیه تنظیم می شود"))
        self.start_tab.setTabText(self.start_tab.indexOf(self.tab_img), _translate("MainWindow", "تصویر"))
        self.btn_start.setToolTip(_translate("MainWindow", "شروع فعالیت برنامه"))
        self.btn_start.setText(_translate("MainWindow", "شروع"))
        self.LogBox.setToolTip(_translate("MainWindow", "گزارش فعالیت برنامه"))
        self.LogBox.setPlaceholderText(_translate("MainWindow", "     *** Program Log ***"))
        self.frame_LCD.setToolTip(_translate("MainWindow", "آمار لحظه ای بررسی برنامه"))
        self.frame_LCD_label.setToolTip(_translate("MainWindow", "آمار لحظه ای بررسی برنامه"))
        self.label_count_txt_5.setText(_translate("MainWindow", "عملیات ناموفق:"))
        self.label_count_txt_3.setText(_translate("MainWindow", "بررسی شده:"))
        self.label_count_txt_4.setText(_translate("MainWindow", "عملیات موفق:"))
        self.label_count_txt.setText(_translate("MainWindow", "تعداد کل :"))
        self.btn_stop.setToolTip(_translate("MainWindow", "توقف برنامه"))
        self.btn_stop.setText(_translate("MainWindow", "توقف"))
        self.btn_maxmin.setToolTip(_translate("MainWindow", "حالت پنجره برنامه"))
        self.btn_maxmin.setText(_translate("MainWindow", "类"))
        self.btn_close.setToolTip(_translate("MainWindow", "بستن برنامه"))
        self.btn_close.setText(_translate("MainWindow", "窱"))
        self.lang.setToolTip(_translate("MainWindow", "تنظیم زبان برنامه"))
        self.lang.setItemText(0, _translate("MainWindow", "EN"))
        self.lang.setItemText(1, _translate("MainWindow", "FA"))
        self.btn_min.setToolTip(_translate("MainWindow", "به حداقل رساندن"))
        self.btn_min.setText(_translate("MainWindow", "-"))
        self.label_appName.setText(_translate("MainWindow", "Advanced WhatsApp"))
        self.areaCode.setToolTip(_translate("MainWindow", "پیش شماره کد کشور شما"))
        self.areaCode.setText(_translate("MainWindow", "98"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
