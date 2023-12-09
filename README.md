# INST326_Final_Project
Final Project Repository

# Purpose:
* QA.txt - A sample text file with questions and answers to them, the format specifically is necessary for the program to run
* QuizGame.py - The python file on which the program is stored and is run through a command line argument
* README.md - This file, which has the credits, and explanation about the program


# Instructions:
* Run the file from the command line, the only two arguments needed are QuizGame.py and the text file you plan on using for the quiz
* This program is a quiz game, we reccomend using it as a study guide by writing your own questions into the text file
* Think of it like Kahoot/Quizlet where you can test yourself on your knowledge, this project is also open source so you may tweak your version as you wish 


# Rules
* Do not use '.' for abbreviations, (i.e, use DC/dc instead of D.C/d.c)
* The answers are not case-senstive



# Attribution:

| Method/Function                     | Primary Author | Techniques Demonstrated|
| ----------------------------------- | -------------- | -----------------------|
| Score.__lt__()                      | Ahmed Elhag    | Magic methods other than __init__
| TriviaGame.__init__()               | Ahmed Elhag    | Regular expression
| parse_args                          | Amaar Amir     | ArgumentParaser class
|ScoreKeeper.display_score_plot()     | Amaar Amir     | Data Visualization
|run_game (with open)                 | Adam Blum      | With statement
|TriviaGame & Timer                   | Adam Blum      | Composition of 2 custom classes
|ScoreKeeper.__init__                 | Kaiya Pankey   | Optional Parameters/Keyword arguments
|run_game (for question,answer)       | Kaiya Pankey   | Sequence Unpacking
|ScoreKeeper.determine_winner()       | David Mariona  | F-strings containing expressions
|Score.__init__                       | David Mariona  | Conditional Expression

# Clarification and Apology
The reason our commit history is slightly different from our attribution table 
is due to a mixture of technological issues and migration of code across 
different files. While working on this project, our group had split ourselves 
between the “original” file and a “test” file. Throughout the process, we had 
been soft-merging these versions. To elaborate, we would migrate code between 
the versions until we had a “true” file in which the QuizGame ran perfectly. 
This ended up being the “test2” file. However, these migrations had caused our 
commit history to display a different image of accreditation than is fact. 

Going back to the technical issues, there were times where we worked in person 
where we acted as drivers and navigators for certain aspects of our code. 
So the commit containing the code for someones work would come from someone else. 

We deeply apologize for the confusion and misunderstanding. 
As this is our first long-term coding project using GitHub, 
we will strive to ensure that these mistakes never happen again. 

