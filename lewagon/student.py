from datetime import date

class Student:
    # class attribute
    '''A class attribute in Python is a variable that is defined directly within
    a class (outside any methods) and is shared across all instances of that
    class. Class attributes are commonly used for data that should be the same
    for all instances or for defining constants.'''
    school = 'lewagon'

    # initializer of instance attributes
    def __init__(self, name, age): # Note the `self` parameter
        self.name = name.capitalize()
        self.age = age

    # instance method
    def says(self, something): # x.f(y) equivalent to Class.f(x,y)
        print(f'{self.name} says {something}')


    @classmethod
    def from_birth_year(cls, name, birth_year): # Note the `cls` parameter
        return cls(name, date.today().year - birth_year)




# felipe = Student("Felipe", 31)
# print(f"Hi my name is {felipe.name}!")
# print(f"And I am {felipe.age}, and I am taking th Data Science BC in {felipe.school}")


# sofia = Student.from_birth_year("Sofia", 1999)
# print(sofia.name)
# sofia.says("she likes medicine")
