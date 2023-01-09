class student:
    def __init__(self, rollNo, name, semester, cgpa):
        self.rollNo = rollNo
        self.name = name
        self.semester = semester
        self.cgpa = cgpa
    def print(self):
        print(self.__name)
        print(self.__rollNo)
        print(self.__semester)
        print(self.__cgpa)


