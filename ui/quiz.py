# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dougall\Python_Workspace\Interview_Questions_GUI\scripts\..\ui\quiz.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(684, 472)
        self.questionText = QtWidgets.QTextEdit(Form)
        self.questionText.setGeometry(QtCore.QRect(110, 40, 481, 71))
        self.questionText.setObjectName("questionText")
        self.answerText = QtWidgets.QTextEdit(Form)
        self.answerText.setGeometry(QtCore.QRect(110, 190, 481, 221))
        self.answerText.setObjectName("answerText")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 160, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.show_answer = QtWidgets.QPushButton(Form)
        self.show_answer.setGeometry(QtCore.QRect(240, 120, 171, 23))
        self.show_answer.setObjectName("show_answer")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(154, 440, 171, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 440, 171, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Question"))
        self.label_2.setText(_translate("Form", "Answer"))
        self.show_answer.setText(_translate("Form", "Show Answer"))
        self.pushButton.setText(_translate("Form", "Next Question"))
        self.pushButton_2.setText(_translate("Form", "End Quiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
