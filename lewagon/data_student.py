from lewagon.student import Student


# lewagon/data_student.py

# the import will only work if executed from lewagon-project directory
# unless you have set up the PYTHONPATH

class DataStudent(Student):
    cursus = 'datascience'
    def __init__(self, name, age, batch):
        super().__init__(name, age)
        self.batch = batch


# boris = DataStudent('boris', 30, 1767)
# boris.batch

# print(boris.name)
# print(boris.age)
# boris.says(f"he is new to batch: {boris.batch}")
