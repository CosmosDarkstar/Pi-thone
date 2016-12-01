'''
Created on Sep 21, 2016

@author: Gab

Implement a class Student. For the purpose of this exercise, a student has a name
and a total quiz score. Supply an appropriate constructor and methods getName(),
addQuiz(int score), getTotalScore(), and getAverageScore(). To compute the average,
you also need to store the number of quizzes that the student took.
Supply a StudentTester class that tests all methods. 
'''

class Student(object):
    score = 0
    name = ""
    counter = 0
    '''
    classdocs
    '''


    def __init__(self, nameIn):
        self.name = nameIn
        
           
    
    def addQuiz(self, scoreAdd):
        self.score += scoreAdd  
        self.counter += 1  
        
    def getTotalScore(self):
        return self.score 

    def getAvgScore(self):
        return self.score / self.counter  

    def makeStudent(self, name):
        student = Student(name)
        return student
