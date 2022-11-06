class Student(object):
    
    __default_number = 0

    def __init__(self, score, name=None):
        if name is None:
            self.__name = f"UnnamedStudent{Student.__default_number}"
            Student.__default_number += 1
        else:
            self.__name = name
        self.__score = score
        self.__percentage = self.calculatePercentage()
        self.__grade = self.calculateGrade()
        
    def calculatePercentage(self):
        self.__percentage = self.__score*10/6
        return self.__percentage

    def calculateGrade(self):
        if self.__score >= 50:
            self.__grade = "A"
        else:
            self.__grade = "B"
        return self.__grade
    
    def showStudentData(self):
        print(f"Student {self.__name} got {self.__score} ({round(self.__percentage, 2)}%) and achieved a grade {self.__grade}.")