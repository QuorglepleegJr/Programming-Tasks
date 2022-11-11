from Bank import Address
class Person:

    def addDetails(self):
        self._name = input("Enter Name: ")
        address_lines = []
        print("Enter Address lines (leave blank to finish):")
        line = input()
        while line:
            address_lines.append(line)
            line = input()
        self.__address = Address(*address_lines)
        self.__age = int(input("Enter Age: "))

    def editDetail(self):
        detail = input("Enter Detail to edit: ").lower()
        while detail not in ("name", "address", "age"):
            print("Invalid detail, must be name, address, or age")
            detail = input("Enter Detail to edit: ").lower()
        if detail == "name":
            self._name = input(f"Enter new name (old: {self._name}): ")
        elif detail == "address":
            print("Old address:")
            print(self.__address)
            print("Enter new Address lines (leave blank to finish):")
            address_lines = []
            line = input()
            while line:
                address_lines.append(line)
                line = input()
            self.__address = Address(*address_lines)
        else:
            self.__age = int(input(f"Enter new age (old: {self.__age})"))

    def showDetails(self):
        print(f"Name: {self._name}")
        print("Address:")
        print(self.__address)
        print(f"Age: {self.__age}")

    def getName(self):
        return self._name # Used in Group.py

class SpecialPerson(Person):

    def __init__(self):
        super().__init__()

    def addTitle(self):
        title = input("Enter title to add: ")
        self._name = title + " " + self._name

def main():
    person1 = Person()
    person1.addDetails()
    person2 = SpecialPerson()
    person2.addDetails()
    person1.editDetail()
    person2.addTitle()
    person1.showDetails()
    person2.showDetails()

if __name__ == "__main__":
    main()
