'''
Created on Sep 21, 2016
 
@author: Gab
'''
from School.Ch3.Student import Student
if __name__ == '__main__':
    joey = Student.makeStudent('jim')
#    joey = Student('Joey')
    joey.addQuizz(99)
    joey.addQuizz(11)
    joey.addQuizz(94)
    joey.addQuizz(87)
    joey.addQuizz(39)
    joey.addQuizz(50)
    joey.addQuizz(67)   
    joey.addQuizz(72)
    joey.addQuizz(48)
    joey.addQuizz(84)
    joey.addQuizz(23)
    print(joey.getTotalScore())
    print(joey.getAvgScore())
