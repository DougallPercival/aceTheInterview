A basic GUI system for Machine Learning Interview Questions

The system has 4 windows: the main window, the write question window, and the question window, and the new user window.

Question Window:
Like a cue card, the window puts a question on the screen. User must decide the answer, then click See Answer. There is a checkbox for Correct/Incorrect, and a button to go Next Question or Close Window.

Write Question Window:
Allows user to write Question, Answer, and add Categories to the question.
Can have multiple categories. Will provide a list of existing categories.

New User Window:
Generates new user profile.

Main window:
Load Question Base: User can load a specific question base.
Load User Profile: User can save multiple profiles, which will help identify questions they are doing well on / questions they are not doing well on, catgories etc.

Write question - open the write question window.
Get Questions - Starts the questions. User can select a subset of categories for this.



DATA STORAGE
Just store JSONs

QUESTION BASE
Question Unit - questionID, question, answer, categories

USER PROFILES
User Unit - userID, username
User_Base - userID, QuestionBaseID, questionID, attempts, correct, incorrect







