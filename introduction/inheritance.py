# Python Inheritance


# Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Amir", "Hamidi")
x.printname()


# Create a Child Class
class Student(Person):
    pass


x = Student("Mobina", "Tajik")
x.printname()


# Add the __init__() Function
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Camellia", "Hamidi")
x.printname()


# Use the super() Function
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("Kaveh", "Hamidi")
x.printname()


# Add Properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


# Add Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )
