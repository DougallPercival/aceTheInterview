# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dougall\Python_Workspace\Interview_Questions_GUI\scripts\..\ui\Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questionBase_load = QtWidgets.QPushButton(self.centralwidget)
        self.questionBase_load.setGeometry(QtCore.QRect(510, 30, 121, 23))
        self.questionBase_load.setObjectName("questionBase_load")
        self.userProfile_load = QtWidgets.QPushButton(self.centralwidget)
        self.userProfile_load.setGeometry(QtCore.QRect(180, 30, 111, 23))
        self.userProfile_load.setObjectName("userProfile_load")
        self.questionBase_box = QtWidgets.QComboBox(self.centralwidget)
        self.questionBase_box.setGeometry(QtCore.QRect(360, 30, 141, 22))
        self.questionBase_box.setObjectName("questionBase_box")
        self.userProfile_box = QtWidgets.QComboBox(self.centralwidget)
        self.userProfile_box.setGeometry(QtCore.QRect(10, 30, 161, 22))
        self.userProfile_box.setObjectName("userProfile_box")
        self.userProfile_new = QtWidgets.QPushButton(self.centralwidget)
        self.userProfile_new.setGeometry(QtCore.QRect(180, 90, 111, 23))
        self.userProfile_new.setObjectName("userProfile_new")
        self.userProfile_delete = QtWidgets.QPushButton(self.centralwidget)
        self.userProfile_delete.setGeometry(QtCore.QRect(180, 60, 111, 23))
        self.userProfile_delete.setObjectName("userProfile_delete")
        self.questionBase_new = QtWidgets.QPushButton(self.centralwidget)
        self.questionBase_new.setGeometry(QtCore.QRect(510, 90, 121, 23))
        self.questionBase_new.setObjectName("questionBase_new")
        self.questionBase_delete = QtWidgets.QPushButton(self.centralwidget)
        self.questionBase_delete.setGeometry(QtCore.QRect(510, 60, 121, 23))
        self.questionBase_delete.setObjectName("questionBase_delete")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 761, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(40, 150, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.questionbase_label = QtWidgets.QLabel(self.centralwidget)
        self.questionbase_label.setGeometry(QtCore.QRect(40, 180, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.questionbase_label.setFont(font)
        self.questionbase_label.setObjectName("questionbase_label")
        self.question_write = QtWidgets.QPushButton(self.centralwidget)
        self.question_write.setGeometry(QtCore.QRect(40, 270, 121, 23))
        self.question_write.setObjectName("question_write")
        self.question_delete = QtWidgets.QPushButton(self.centralwidget)
        self.question_delete.setGeometry(QtCore.QRect(40, 300, 121, 23))
        self.question_delete.setObjectName("question_delete")
        self.categories_list = QtWidgets.QListWidget(self.centralwidget)
        self.categories_list.setGeometry(QtCore.QRect(320, 220, 256, 192))
        self.categories_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.categories_list.setObjectName("categories_list")
        self.categories_label = QtWidgets.QLabel(self.centralwidget)
        self.categories_label.setGeometry(QtCore.QRect(350, 200, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.categories_label.setFont(font)
        self.categories_label.setObjectName("categories_label")
        self.start_quiz = QtWidgets.QPushButton(self.centralwidget)
        self.start_quiz.setGeometry(QtCore.QRect(320, 440, 261, 23))
        self.start_quiz.setObjectName("start_quiz")
        self.user_stats = QtWidgets.QPushButton(self.centralwidget)
        self.user_stats.setGeometry(QtCore.QRect(40, 210, 121, 23))
        self.user_stats.setObjectName("user_stats")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 420, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 420, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionGet_Stats = QtWidgets.QAction(MainWindow)
        self.actionGet_Stats.setObjectName("actionGet_Stats")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.questionBase_load.setText(_translate("MainWindow", "Load Question Base"))
        self.userProfile_load.setText(_translate("MainWindow", "Load User Profile"))
        self.userProfile_new.setText(_translate("MainWindow", "New User"))
        self.userProfile_delete.setText(_translate("MainWindow", "Delete User"))
        self.questionBase_new.setText(_translate("MainWindow", "New Question Base"))
        self.questionBase_delete.setText(_translate("MainWindow", "Delete Question Base"))
        self.user_label.setText(_translate("MainWindow", "User:"))
        self.questionbase_label.setText(_translate("MainWindow", "Question Base:"))
        self.question_write.setText(_translate("MainWindow", "Write New Question"))
        self.question_delete.setText(_translate("MainWindow", "Delete Question"))
        self.categories_label.setToolTip(_translate("MainWindow", "To only quiz yourself on specific categories, make selections here."))
        self.categories_label.setText(_translate("MainWindow", "Select Question Categories"))
        self.start_quiz.setText(_translate("MainWindow", "Start Quiz"))
        self.user_stats.setText(_translate("MainWindow", "See User Stats"))
        self.label.setText(_translate("MainWindow", "Specify number of questions"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionGet_Stats.setText(_translate("MainWindow", "Get Stats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
