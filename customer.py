# this class inherits from Person

from person import Person


class Customer(Person):

    def __init__(self, name, age, gender, interest):
        super().__init__(name, age, gender)
        self.interest = interest
