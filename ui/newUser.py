# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dougall\Python_Workspace\Interview_Questions_GUI\scripts\..\ui\newUser.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewUser(object):
    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(560, 154)
        self.lineEdit = QtWidgets.QLineEdit(NewUser)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(NewUser)
        self.label.setGeometry(QtCore.QRect(76, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.user_create = QtWidgets.QPushButton(NewUser)
        self.user_create.setGeometry(QtCore.QRect(190, 120, 75, 23))
        self.user_create.setObjectName("user_create")
        self.user_cancel = QtWidgets.QPushButton(NewUser)
        self.user_cancel.setGeometry(QtCore.QRect(270, 120, 75, 23))
        self.user_cancel.setObjectName("user_cancel")

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)

    def retranslateUi(self, NewUser):
        _translate = QtCore.QCoreApplication.translate
        NewUser.setWindowTitle(_translate("NewUser", "Form"))
        self.label.setText(_translate("NewUser", "Username"))
        self.user_create.setText(_translate("NewUser", "Create"))
        self.user_cancel.setText(_translate("NewUser", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewUser = QtWidgets.QWidget()
    ui = Ui_NewUser()
    ui.setupUi(NewUser)
    NewUser.show()
    sys.exit(app.exec_())
