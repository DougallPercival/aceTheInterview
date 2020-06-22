import os
import sys
from random import shuffle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from src import DataConnector

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

uipath = r"{}\ui\stats.ui".format(os.path.dirname(os.path.realpath(__file__)))
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
		
		self.user_stats.clicked.connect(self.show_stats)
		
		self.question_write.clicked.connect(self.write_question)
		#self.question_edit.clicked.connect(self.new_user) #TODO:
		#self.questions_download.clicked.connect(self.new_user) #TODO:
		
		self.start_quiz.clicked.connect(self.quiz_start)
	

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
		# set up categories list
		self.setCategories()
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
		# reset categories
		self.categories_list.clear()
				
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
		
	def quiz_start(self):
		"""
		Start the quiz
		Loads UserID, QBID, number of questions, and specified categories to the quiz window
		Quiz Window handles generation of quiz
		"""
		
		
		try:
			num_qs = int(self.numquestions.text())
		except:
			num_qs = -1
		
		# get selected categories
		cats = []
		if len(self.categories_list.selectedItems()) > 0:
			for item in self.categories_list.selectedItems():
				cats.append(item.text())
		quizWindow = QuizWindow(self.current_qb['ID'], self.current_user['ID'], num_qs, cats)
		quizWindow.exec_()
		
		#reload user profile
		self.load_user()
		return
		
	def show_stats(self):
		"""
		Show a user's stats
		"""
		statsWindow = StatsWindow(self.current_user['ID'], self.current_qb['ID'])
		statsWindow.exec_()
		
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
			
		# add questions - if deleted, keep them in list in case someone wants to bring them back
		question = {"QUESTION":q_text, "ANSWER":a_text, "CATEGORIES":categories, "DELETED":False} 
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
	def __init__(self, questionBaseID, userID, num_questions, categories):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)				
		self.qbConnector = DataConnector.QuestionBaseConnector(r"data")
		self.userConnector = DataConnector.UserProfileConnector(r"data")
		self.questionBaseID = questionBaseID
		self.userID = userID
		self.num_questions = num_questions
		self.categories = categories

		# define question
		self.quiz, self.quiz_index = self.createQuiz()
		# if there are no questions, end early
		if len(self.quiz) == 0:
			self.show_answer.setEnabled(False)
			self.next_question.setEnabled(False)
			self.correctRadio.setEnabled(False)
			self.incorrectRadio.setEnabled(False)
			self.questionText.setText("No questions found for this quiz")
		else:
			self.incorrectRadio.setChecked(True)
			self._displayQuestion()
		# display first question
		
		# button setup
		self.show_answer.clicked.connect(self.showAnswer)
		self.next_question.clicked.connect(self.nextQuestion)
		self.end_quiz.clicked.connect(self.endQuiz)
	

	def createQuiz(self):
		"""
		Get questions for the quiz, random ordering.
		"""
		if len(self.categories) > 0:
			if self.categories[0] == "<ALL>":
				questions = self.qbConnector.loadQuestions(self.questionBaseID)
				return
			else:
				questions = self.qbConnector.loadQuestions(self.questionBaseID, categories=self.categories)
		else:
			questions = self.qbConnector.loadQuestions(self.questionBaseID)
		
		# shuffle questions
		shuffle(questions)
		return questions, 0
	
	def _displayQuestion(self):
		"""
		Display question on the question text line.
		"""
		current_question = self.quiz[self.quiz_index]
		self.questionText.setText(current_question['QUESTION'])
		return
	
	def showAnswer(self):
		"""
		Show the answer of the current question
		"""
		current_question = self.quiz[self.quiz_index]
		self.answerText.setText(current_question['ANSWER'])
		return
		
	def nextQuestion(self):
		"""
		Proceed to the next question
		Update self.quiz_index to be 1 higher
		Update user profile with Question ID answered, correct/incorrect values
		Reset correct/incorrect radio buttons
		"""
		self.questionText.clear()
		self.answerText.clear()
		
		# get id
		questionID = self.quiz[self.quiz_index]['ID']
		# get correct/incorrect
		if self.correctRadio.isChecked():
			correct = True
		elif self.incorrectRadio.isChecked():
			correct = False
		
		self.userConnector.userAnswer(self.userID, self.questionBaseID, questionID, correct)
		
		
		self.quiz_index += 1
		self.incorrectRadio.setChecked(True)
		
		# display next question if exists
		if self.quiz_index == len(self.quiz):
			self.endQuiz()
			return
			
		self._displayQuestion()
		return
	
	def endQuiz(self):
		"""
		Finish quiz, close window
		"""
		self.close()
		return
		
		
class StatsWindow(QtWidgets.QDialog,ui[5]):
	def __init__(self, questionBaseID, userID):
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)	
		self.qbConnector = DataConnector.QuestionBaseConnector(r"data")
		self.userConnector = DataConnector.UserProfileConnector(r"data")
		self.questionBaseID = questionBaseID
		self.userID = userID
		
		self.__loadQuestions()
		
		#setup stat holding variables
		self.__setupStatVariables()
		
		# query stats for ALL categories to start
		self.queryStats()
		self.__displayStats()
		self.__loadCategories()
		
		# button connectors
		self.closeButton.clicked.connect(self.exitDialog)
		self.applyButton.clicked.connect(self.apply)
		
		
		
	def __loadQuestions(self):
		"""
		Load questions and user profile stats for querying
		"""
		self.questionbase = self.qbConnector.questionStatsQuery(self.questionBaseID)
		self.userstats = self.userConnector.userStatsQuery(self.userID)
		return
		
	def __setupStatVariables(self):
		"""
		Setup stat variables to defaults of 0
		"""
		self.attempts = 0
		self.correct = 0
		self.incorrect = 0
		self.percentCorrect = 0.0
		return
		
	def __loadCategories(self):
		"""
		Load categories to the list widget
		"""
		# reset categories
		self.categories_list.clear()
				
		# get categories
		self.categories_list.addItem("<ALL>")
		
		categories = self.qbConnector.getCategories(self.questionBaseID)
		for cat in categories:
			self.categories_list.addItem(cat)
			
		return
		
		
	def queryStats(self, category=None):
		"""
		Return the statistics for the given categories. None represents ALL categories.
		"""
		# for all cats
		if category is None:
			for q in self.userstats:
				self.attempts += q['ATTEMPTS']
				self.correct += q['CORRECT']
				self.incorrect += q['INCORRECT']
			# get percentage correct
			self.percentCorrect = round((self.correct / self.attempts) * 100, 2)
			
		else:
			possible_questions = []
			# identify question ids in category
			for question in self.questionbase:
				if not question['DELETED']:
					if category in question['CATEGORIES']:
						possible_questions.append(question['ID'])
			
			for q in self.userstats:
				# QID, QBID are part of q
				if q['QID'] in possible_questions:
					self.attempts += q['ATTEMPTS']
					self.correct += q['CORRECT']
					self.incorrect += q['INCORRECT']
			# get percentage correct
			if self.attempts > 0:
				self.percentCorrect = round((self.correct / self.attempts) * 100, 2)
			
		return
		
	def __displayStats(self):
		"""
		Display current stats to the dialog window
		"""
		self.line_attempted.setText(str(self.attempts))
		self.line_correct.setText(str(self.correct))
		self.line_incorrect.setText(str(self.incorrect))
		self.line_pct.setText("{}%".format(self.percentCorrect))
		return
		
	def apply(self):
		"""
		Apply the selected category 
		"""
		self.__setupStatVariables()
		# get selected category
		category = ""
		if len(self.categories_list.selectedItems()) > 0:
			for item in self.categories_list.selectedItems():
				category = item.text()
		else:
			category = "<ALL>"
		
		if category == "<ALL>":
			category = None
		
	
		self.queryStats(category=category)
		self.__displayStats()

		return
		
	def exitDialog(self):
		"""
		close window
		"""
		self.close()
		return
		
		
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT5()
    myapp.show()
    sys.exit(app.exec_())