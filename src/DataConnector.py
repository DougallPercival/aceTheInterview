import json
import os

class DataConnector():
	"""
	The Data Connector links to the Data Store and imports / exports data from the GUI to the store.
	
	"""
	
	def __init__(self, dataStore):
		"""
		Initialize the data connector. Point to a datastore path
		"""
		if os.path.exists(dataStore):
			self.dataStore = dataStore
		else:
			raise ValueError("No data store found")
			
	



class QuestionBaseConnector(DataConnector):
	"""
	Questions have 3 keys - QUESTION, ANSWER, and CATEGORIES
	"""
	
	
	def __init__(self, dataStore):
		DataConnector.__init__(self, dataStore)
		self.database = r"{}\QuestionBase".format(self.dataStore)
		
	
	def getQuestionBases(self):
		"""
		Load all question base names and ids
		"""
		bases = os.listdir("{}".format(self.database))
		# ID and name
		qbs = []
		for qb in bases:
			id = qb.split('_')[0]
			with open("{}\{}".format(self.database, qb), 'r') as f:
				data = json.load(f)
			f.close()
			if not data['DELETED']:
				name = data['NAME']
				qbs.append((name, id))

		return qbs
	
	def newQB(self, name):
		"""
		Generate a new question base
		Only required input is the name of the question base
		"""
		# get number of existing question bases to set ID
		id = len(os.listdir("{}".format(self.database))) + 1
		new_base = "{}_QuestionBase.json".format(id)
		
		base_setup = {}
		base_setup['ID'] = id
		base_setup['NAME'] = name
		base_setup['DELETED'] = False
		base_setup['QUESTIONS'] = []
		
		with open("{}\{}".format(self.database, new_base), 'w') as f:
			json.dump(base_setup, f, ensure_ascii=True, indent=4)
		f.close()	
		return
		
	def loadQB(self, qbid):
		"""
		Load an existing Question Base
		"""
		try:
			with open("{}\{}_QuestionBase.json".format(self.database,str(qbid)), 'r') as f:
				qb = json.load(f)
			f.close()
		except:
			raise ValueError("No question base by that ID found in the Data Store")
		
		return qb
		
	def setDeleted(self, qbid):
		"""
		Toggle the deleted switch on the user profile to True. Will no longer show up, but data can still be manually accessed.
		"""
		qb = self.loadQB(qbid)
		
		qb['DELETED'] = True
		
		# overwrite qb
		with open("{}\{}_QuestionBase.json".format(self.database,qbid), 'w') as f:
			json.dump(qb, f, ensure_ascii=True, indent=4)	
		f.close()
		
		return	
		
	def writeQuestion(self, qbid, question):
		"""
		Write a question to a question base
		"""
		qb = self.loadQB(qbid)
		qb['QUESTIONS'].append(question)
		
		# overwrite qb
		with open("{}\{}_QuestionBase.json".format(self.database,qbid), 'w') as f:
			json.dump(qb, f, ensure_ascii=True, indent=4)	
		f.close()
		return
		
	def deleteQuestion(self, qbid, questionID):
		"""
		Remove a question from the QuestionBase
		"""
		qb = self.loadQB(qbid)
		del qb['QUESTIONS'][questionID]
		
		# overwrite qb
		with open("{}\{}_QuestionBase.json".format(self.database,qbid), 'w') as f:
			json.dump(qb, f, ensure_ascii=True, indent=4)	
		f.close()	
		return
		
	def loadQuestions(self, qbid, categories=None):
		"""
		Load all questions from the QB.
		Can subset by passing a list of categories
		"""
		qb = self.loadQB(qbid)
		if categories is None:
			return qb['QUESTIONS']

		questions = []
		for q in qb['QUESTIONS']:
			to_append=False
			for cat in q['CATEGORIES']:
				if cat in categories:
					to_append=True
			if to_append:
				questions.append(q)
		return questions
		
	def getCategories(self, qbid):
		qb = self.loadQuestions(qbid)
		cats = []
		for q in qb:
			for cat in q['CATEGORIES']:
				if cat not in cats:
					cats.append(cat)
		
		return cats
		
		

class UserProfileConnector(DataConnector):
	def __init__(self, dataStore):
		DataConnector.__init__(self, dataStore)
		self.database = r"{}\UserBase".format(self.dataStore)
	

	def getUsers(self):
		"""
		Load all user profile names and ids
		"""
		profiles = os.listdir("{}".format(self.database))
		# ID and name
		users = []
		for profile in profiles:
			id = profile.split('_')[0]
			with open("{}\{}".format(self.database, profile), 'r') as f:
				data = json.load(f)
			f.close()
			if not data['DELETED']:
				name = data['NAME']
				users.append((name, id))
		
		return users
		
	def newUser(self, name):
		"""
		Add a new user to the User Base, with a username and unique ID.
		"""
		# get number of existing user profiles to set ID
		id = len(os.listdir("{}".format(self.database))) + 1
		new_base = "{}_UserProfile.json".format(id)
		
		base_setup = {}
		base_setup['ID'] = id
		base_setup['NAME'] = name
		base_setup['DELETED'] = False
		base_setup['QUESTIONS'] = []
		
		with open("{}\{}".format(self.database, new_base), 'w') as f:
			json.dump(base_setup, f, ensure_ascii=True, indent=4)
		f.close()	
		return
		
	def loadUser(self, uid):
		"""
		Load the User Profile
		"""
		try:
			with open("{}\{}_UserProfile.json".format(self.database,str(uid)), 'r') as f:
				up = json.load(f)
			f.close()
		except:
			raise ValueError("No question base by that ID found in the Data Store")
		
		return up
		
	def overwriteUser(self, uid, up):
		"""
		Overwrite the user profile
		"""
		# overwrite user profile
		with open("{}\{}_UserProfile.json".format(self.database, uid), 'w') as f:
			json.dump(up, f, ensure_ascii=True, indent=4)
		f.close()	
		return
		
	def setDeleted(self, uid):
		"""
		Toggle the deleted switch on the user profile to True. Will no longer show up, but data can still be manually accessed.
		"""
		up = self.loadUser(uid)
		
		up['DELETED'] = True
		
		self.overwriteUser(uid, up)
		
		return	

	def userAnswer(self, userid, qbid, qid, correct):
		"""
		When the user answers a question, the question they answeres is added or updated in their file
		Question contains QuestionBaseID, QuestionID, NumAttempts, NumCorrect, NumIncorrect
		Overwrites the user profile at this time
		"""
		up = self.loadUser(userid)
		for question in up['QUESTIONS']:
			if question['QBID'] == qbid and question['QID'] == qid:
				question['ATTEMPTS'] += 1
				if correct:
					question['CORRECT'] += 1
				else:
					question['INCORRECT'] += 1
				# overwrite user profile
				with open("{}\{}_UserProfile.json".format(self.database, userid), 'w') as f:
					json.dump(up, f, ensure_ascii=True, indent=4)
				f.close()	
				return
				
		new_question = {}
		new_question['QBID'] = qbid
		new_question['QID'] = qid
		new_question['ATTEMPTS'] = 1
		if correct:
			new_question['CORRECT'] = 1
			new_question['INCORRECT'] = 0
		else:
			new_question['CORRECT'] = 0
			new_question['INCORRECT'] = 1
		up['QUESTIONS'].append(new_question)
		
		# overwrite user profile
		self.overwriteUser(userid, up)
		return
				
			
		
			
			
			
			
		
	
		