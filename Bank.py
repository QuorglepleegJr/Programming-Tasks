class Address(object):
    def __init__(self, *lines):
        self.lines = []
        for line in lines:
            self.lines.append(line)

    def __str__(self):
        string = ""
        for line in self.lines:
            string += line + "\n"
        return string

class Date(object):
    def __init__(self, d=1, m=1, y=1970):
        self.d = d
        self.m = m
        self.y = y

    def __str__(self):
        return f"{self.d}/{self.m}/{self.y}"

class Account(object): # Shouldn't be instantiated

    BASE_INTEREST_RATE = 3
    __default_number = 0

    def __init__(*useless_args):
        raise NotImplementedError("Account is a factory class and therefore shouldn't be instantiated")

    def new(address, name=None, initial_deposit=0):
        if name is None:
            name = f"UnnamedAccount{Account.__default_number}"
            Account.__default_number += 1
        else:
            name = str(name)

        try:
            initial_deposit = float(initial_deposit)
            assert initial_deposit >= 0

        except (ValueError, AssertionError):
            raise ValueError("Invalid initial deposit for Account, must be a non-negative number")
        
        if not isinstance(address, Address):
            raise ValueError("Invalid address for Account, must be of type Address")

        if initial_deposit > 500:
            return GoldAccount(address, name, initial_deposit, Account.BASE_INTEREST_RATE)
        else:
            return BasicAccount(address, name, initial_deposit)

class BasicAccount(object):
    def __init__(self, address, name, initial_deposit):
        self._address = address
        self._name = str(name)
        self._balance = initial_deposit

    def setName(self, name):
        self._name = str(name)

    def getBalance(self):
        return self._balance

    def credit(self, amount):
        try:
            amount = float(amount)
            assert amount > 0
        except (ValueError, AssertionError):
            raise ValueError("Invalid amount to credit, must be a positive number")
        else:
            self._balance += amount

    def showDetails(self):
        print(f"Account holder name:\n{self._name}")
        print(f"Account holder address:\n{self._address}", end="")
        print(f"Account balance:\n{round(self._balance, 2)}")

class GoldAccount(BasicAccount):
    def __init__(self, address, name, initial_deposit, interest_rate):
        super().__init__(address, name, initial_deposit)
        self.__interest_rate = interest_rate
        self.__date_of_interest = Date()

    def addInterest(self, date=None):
        self.credit(self._balance * self.__interest_rate / 100)
        if date is None:
            date = Date()
        self.__date_of_interest = date

    def withdraw(self, amount):
        try:
            amount = float(amount)
            assert amount > 0
            assert amount <= self._balance
        except (ValueError, AssertionError):
            raise ValueError("Invalid amount to withdraw, must be a positive number less than the balance")
        else:
            self._balance -= amount

    def showDetails(self):
        super().showDetails()
        print(f"Account Interest rate:\n{self.__interest_rate}%")
        print(f"Date of last Interest:\n{self.__date_of_interest}")
