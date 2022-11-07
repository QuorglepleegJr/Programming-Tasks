from People import Person
class Group:
    def __init__(self, size=5):
        self.__group_size = size
        self.__people = []

    def getSize(self):
        return self.__group_size

    def addPeople(self):
        for index in range(self.__group_size):
            self.__people.append(Person())
            self.__people[index].addDetails()

    def showPeople(self):
        for person in self.__people:
            person.showDetails()
    
    def showPerson(self, index):
        self.__people[index].showDetails()

    def findPerson(self, name):
        for index, person in enumerate(self.__people):
            if person.getName() == name:
                return index
        return -1
    
    def editPerson(self, locator):
        if isinstance(locator, string):
            index = findPerson(locator)
        else:
            index = locator
        if index >= 0:
            self.__people[index].editDetail()

# UNTESTED