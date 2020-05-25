import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from src import DataConnector


newconn1 = DataConnector.QuestionBaseConnector(r"data")
newconn2 = DataConnector.UserProfileConnector(r"data")


def test_questionbase(newconn):
	newconn.newQB("Test")
	newconn.writeQuestion(1, "What are pants?")

	newconn.writeQuestion(1, "What aren't pants?")

	newconn.writeQuestion(1, "Why are pants?")

	print(newconn.loadQB(1))
	print('\n\n')

	newconn.deleteQuestion(1, 2)

	print(newconn.loadQB(1))
	return
	
def test_userbase(newconn):

	newconn.newUser('percido')
	
	newconn.userAnswer(1, 1, 0, True)
	print(newconn.loadUser(1))
	
	return

#test_questionbase(newconn1)
#test_userbase(newconn2)



ui = []
uipath = r"{}\ui\Main.ui".format(os.path.dirname(os.path.realpath(__file__)))
ui.append(uic.loadUiType(uipath)[0])

uipath = r"{}\ui\newUser.ui".format(os.path.dirname(os.path.realpath(__file__)))
ui.append(uic.loadUiType(uipath)[0])

uipath = r"{}\ui\newQuestionBase.ui".format(os.path.dirname(os.path.realpath(__file__)))
ui.append(uic.loadUiType(uipath)[0])

uipath = r"{}\ui\write_question.ui".format(os.path.dirname(os.path.realpath(__file__)))
ui.append(uic.loadUiType(uipath)[0])

uipath = r"{}\ui\quiz.ui".format(os.path.dirname(os.path.realpath(__file__)))
ui.append(uic.loadUiType(uipath)[0])

# Main Window
class StartQT5(QtWidgets.QMainWindow,ui[0]):
	"""
	Main Window of the GUI.
	"""
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)
		self.userConnector = DataConnector.UserProfileConnector(r"data")
		self.qbConnector = DataConnector.QuestionBaseConnector(r"data")
		
		self.load_users()
		self.load_qbs()
		
		# set button actions
		self.actionExit.triggered.connect(self.click_exit) #Exit button in menu
		
		self.userProfile_load.clicked.connect(self.load_user)
		self.userProfile_delete.clicked.connect(self.delete_user)
		self.userProfile_new.clicked.connect(self.new_user)
		
		self.questionBase_load.clicked.connect(self.load_qb)
		self.questionBase_delete.clicked.connect(self.delete_qb)
		self.questionBase_new.clicked.connect(self.new_qb)		
		
		self.user_stats.clicked.connect(self.new_user)
		self.question_write.clicked.connect(self.write_question)
		self.question_delete.clicked.connect(self.new_user)
		self.start_quiz.clicked.connect(self.new_user)
	

	def load_users(self):
		"""
		Load all user profiles and add to the user combo box
		"""
		# get count
		cnt = self.userProfile_box.count()
		# remove all items
		if cnt > 0:
			for i in range(cnt, -1, -1):
				self.userProfile_box.removeItem(i)
		
		self.userProfile_box.addItem("<NAME>, <ID>")
		users = self.userConnector.getUsers()
		for user in users:
			self.userProfile_box.addItem("{}, {}".format(user[0], user[1]))
		return
		

	
	def new_user(self):
		"""
		Define a new user profile
		"""
		new_user_window = NewUserWindow()
		new_user_window.exec_()
		
		# reload users 
		self.load_users()
		
		return
		
	def load_user(self):
		"""
		Load a user profile
		"""
		# verify current index in userProfile_box
		curind = str(self.userProfile_box.currentIndex())
		if int(curind) == 0:
			return
		else:
			user = str(self.userProfile_box.currentText()).split(',')[-1]
			self.current_user = self.userConnector.loadUser(uid=int(user.strip()))
		# set labels to current user profile
		self.user_label.setText("User: {}".format(self.current_user['NAME']))
		return
		
	def delete_user(self):
		"""
		Delete a user profile
		Deletions are not final
		"""
		# verify current index in userProfile_box
		_
		curind = str(self.userProfile_box.currentIndex())
		if int(curind) == 0:
			return
		else:
			user = str(self.userProfile_box.currentText()).split(',')[-1]
			self.userConnector.setDeleted(uid=int(user.strip()))
			# reload the user list
			self.load_users()
		return
	
	
	def load_qbs(self):
		"""
		Load all Question Bases and add to the combo box
		"""
		# get count
		cnt = self.questionBase_box.count()
		# remove all items
		if cnt > 0:
			for i in range(cnt, -1, -1):
				self.questionBase_box.removeItem(i)
		
		self.questionBase_box.addItem("<NAME>, <ID>")
		qbs = self.qbConnector.getQuestionBases()
		for qb in qbs:
			self.questionBase_box.addItem("{}, {}".format(qb[0], qb[1]))
		return
	
	def new_qb(self):
		"""
		Create new question base
		"""
		new_qb_window = NewQBWindow()
		new_qb_window.exec_()
		
		# reload bases 
		self.load_qbs()
		
		return

	def load_qb(self):
		"""
		Load question base
		"""
		# verify current index in questionBase_box
		curind = str(self.questionBase_box.currentIndex())
		if int(curind) == 0:
			return
		else:
			qb = str(self.questionBase_box.currentText()).split(',')[-1]
			self.current_qb = self.qbConnector.loadQB(qbid=int(qb.strip()))
		# set labels to current user profile
		self.questionbase_label.setText("Question Base: {}".format(self.current_qb['NAME']))
		return
		
	def delete_qb(self):
		"""
		Delete question base
		"""
		# verify current index in questionBase_box
		_
		curind = str(self.questionBase_box.currentIndex())
		if int(curind) == 0:
			return
		else:
			qb = str(self.questionBase_box.currentText()).split(',')[-1]
			self.qbConnector.setDeleted(qbid=int(qb.strip()))
			# reload the user list
			self.load_qbs()
		return
		
	def setCategories(self):
		"""
		Once a question base is loaded, or a new question is added, establish the categories box.
		"""
		# get count
		cnt = self.categories_list.count()
		# remove all items
		if cnt > 0:
			for i in range(cnt, -1, -1):
				self.categories_list.removeItem(i)
				
		# get categories
		self.categories_list.addItem("<ALL>")
		
		categories = self.qbConnector.getCategories(self.current_qb['ID'])
		for cat in categories:
			self.categories_list.addItem(cat)
			
		return
		
	def write_question(self):
		"""
		Allow user to write a new question
		"""
		window = NewQuestionWindow(self.current_qb['ID'])
		window.exec_()
		
		# reload question base 
		self.load_qb()
		return
		
		
		
	def click_exit(self):
		"""
		Method: click_exit
		When user clicks QuitButton, terminate GUI
		"""
		sys.exit()
		
		


class NewUserWindow(QtWidgets.QDialog,ui[1]):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)
		self.userConnector = DataConnector.UserProfileConnector(r"data")
		
		# set button functions
		self.user_cancel.clicked.connect(self.cancel)
		self.user_create.clicked.connect(self.create)
	
	def create(self):
		"""
		Generate new user if text is entered
		"""
		if len(self.user_lineEdit.text().strip()) == 0:
			return
		else:
			self.userConnector.newUser(self.user_lineEdit.text())
			self.close()
		return

	def cancel(self):
		"""
		Cancel the window
		"""
		self.close()
		return
		
class NewQBWindow(QtWidgets.QDialog,ui[2]):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)
		self.qbConnector = DataConnector.QuestionBaseConnector(r"data")
		
		# set button functions
		self.qb_cancel.clicked.connect(self.cancel)
		self.qb_create.clicked.connect(self.create)
	
	def create(self):
		"""
		Generate new user if text is entered
		"""
		if len(self.qb_lineEdit.text().strip()) == 0:
			return
		else:
			self.qbConnector.newQB(self.qb_lineEdit.text())
			self.close()
		return

	def cancel(self):
		"""
		Cancel the window
		"""
		self.close()
		return
		
class NewQuestionWindow(QtWidgets.QDialog,ui[3]):
	def __init__(self, questionBaseID):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)		
		self.qbConnector = DataConnector.QuestionBaseConnector(r"data")
		self.questionBaseID = questionBaseID
		print(self.questionBaseID )
		
		# set button functions
		self.anotherButton.clicked.connect(self.another)	
		self.doneButton.clicked.connect(self.complete)	
		self.cancelButton.clicked.connect(self.cancel)
		
	def __validateAnswer(self):
		"""
		Check that all of the answer pieces are properly filled out
		Write an error message out if something is missing
		"""
		if len(self.questionText.toPlainText().strip()) == 0:
			self.messageLabel.setText("Error: Question must have text")
			return False
			
		if len(self.answerText.toPlainText().strip()) == 0:
			self.messageLabel.setText("Error: Answer must have text")
			return False
			
		if len(self.category1.text().strip()) == 0 and len(self.category2.text().strip()) == 0 and len(self.category3.text().strip()) == 0:
			self.messageLabel.setText("Error: Must specify at least 1 question category")
			return False
		
		return True
		
	def __addQuestion(self):
		"""
		Add the question to the question base
		"""
		q_text = self.questionText.toPlainText()
		a_text = self.answerText.toPlainText()
		categories = []
		if len(self.category1.text().strip()) > 0:
			categories.append(self.category1.text().strip())
		if len(self.category2.text().strip()) > 0:
			categories.append(self.category2.text().strip())
		if len(self.category3.text().strip()) > 0:
			categories.append(self.category3.text().strip())
			
		# add questions
		question = {"QUESTION":q_text, "ANSWER":a_text, "CATEGORIES":categories}
		self.qbConnector.writeQuestion(self.questionBaseID, question)
		
		return
	
	def another(self):
		"""
		Complete current question and reset to blank
		"""
		if self.__validateAnswer():
			self.__addQuestion()
		# clear contents
		self.questionText.clear()
		self.answerText.clear()
		self.category1.setText("")
		self.category2.setText("")
		self.category3.setText("")
		return
	
	def complete(self):
		"""
		Complete current question and add to QB
		"""
		if self.__validateAnswer():
			self.__addQuestion()
		# return to main window
		self.close()
		return
	
	def cancel(self):
		"""
		Cancel the window, clear all info
		"""
		self.close()
		return		
		
		
class QuizWindow(QtWidgets.QDialog,ui[4]):
	def __init__(self, questionBaseID, userID):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)				
		self.qbConnector = DataConnector.QuestionBaseConnector(r"data")
		self.userConnector = DataConnector.UserProfileConnector(r"data")
		self.questionBaseID = questionBaseID
		self.userID = userID
		
		
		
		
		
		
		
		
		
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT5()
    myapp.show()
    sys.exit(app.exec_())