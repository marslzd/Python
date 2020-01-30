# Pyhon3
# randomQuizGenerator.py - Creates quizzes with questions and 
# answers in random order, along with the answer key.

import random
import os
Filepath = os.path.join(os.getcwd(),'8_Project/Quiz_folder')
print(Filepath)
# The quiz data. Keys are states and values are their capitals.
# 以美国州名为keys，以州首府为values
capitals = { 'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':'Phoneix',
             'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
             'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
             'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
             'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
             'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
             'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
             'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
             'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
             'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
             'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleign',
             'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':'Oklahoma City',
             'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
             'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
             'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Monpelier', 
             'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charletson',
             'Wisconsin': 'Madison', 'Wyoming': 'cheyenne'}
# print(len(capitals))

# Generate 35 quiz files
for quizNum in range(35):
    # Create the quize and answer key files
    quizFile = open('/home/linux/Documents/Python_test/Automate_the_Boring_Stuff_with_Python/8_Project/Quiz_folder/capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('/home/linux/Documents/Python_test/Automate_the_Boring_Stuff_with_Python/8_Project/Quiz_folder/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):

        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]    # delete correct answer
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
