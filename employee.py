# this class inherits from Person

from person import Person


class Employee(Person):

    def __init__(self, name, age, gender, store, department, position):
        super().__init__(name, age, gender)
        self.store = store
        self.department = department
        self.position = position

