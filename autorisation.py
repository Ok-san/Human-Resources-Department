from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 414)
        Form.setMinimumSize(QtCore.QSize(446, 414))
        Form.setMaximumSize(QtCore.QSize(446, 414))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
                           "background: #333;\n"
                           "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "D:/Учеба/Методы и средства проектирования ИСиТ/Human-Resources-Department/icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 70, 401, 321))

        self.frame.setStyleSheet("*{\n"
                                 "font-famaly: century gothic;\n"
                                 "font-size: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QFrame{\n"
                                 "background: #333;\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 "#pushButton{\n"
                                 "background: #d80ff7;\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "color:  #f0acfa;\n"
                                 "font-size: 19px;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "background:transparent;\n"
                                 "border:none;\n"
                                 "border-bottom: 2px solid #f0acfa;\n"
                                 "color:white;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 260, 401, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 180, 261, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEditUsername")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 110, 261, 41))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEditPassword")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 161, 41))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 10, 121, 121))
        self.pushButton_2.setStyleSheet("*{\n"
                                        "background: #d80ff7;\n"
                                        "border-radius: 60px;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "D:/Учеба/Методы и средства проектирования ИСиТ/Human-Resources-Department/icon/person-icon-1671.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.pushButton.setText(_translate("Form", "Авторизироваться"))
        self.label.setText(_translate("Form", "Имя пользователя"))
        self.label_2.setText(_translate("Form", "Пароль"))
