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
test_userbase(newconn2)