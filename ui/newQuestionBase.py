# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dougall\Python_Workspace\Interview_Questions_GUI\scripts\..\ui\newQuestionBase.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewUser(object):
    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(360, 154)
        self.lineEdit = QtWidgets.QLineEdit(NewUser)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(NewUser)
        self.label.setGeometry(QtCore.QRect(40, 40, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.qb_create = QtWidgets.QPushButton(NewUser)
        self.qb_create.setGeometry(QtCore.QRect(70, 110, 75, 23))
        self.qb_create.setObjectName("qb_create")
        self.qb_cancel = QtWidgets.QPushButton(NewUser)
        self.qb_cancel.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.qb_cancel.setObjectName("qb_cancel")

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)

    def retranslateUi(self, NewUser):
        _translate = QtCore.QCoreApplication.translate
        NewUser.setWindowTitle(_translate("NewUser", "Form"))
        self.label.setText(_translate("NewUser", "Question Base Name"))
        self.qb_create.setText(_translate("NewUser", "Create"))
        self.qb_cancel.setText(_translate("NewUser", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewUser = QtWidgets.QWidget()
    ui = Ui_NewUser()
    ui.setupUi(NewUser)
    NewUser.show()
    sys.exit(app.exec_())
