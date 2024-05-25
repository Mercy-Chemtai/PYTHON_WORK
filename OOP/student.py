class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code

    def greet_student(self):
        greeting = f"Hello {self.first_name},welcome to {self.school}. Your code is {self.code}"
        return greeting

    def greet_with_age(self):
        greeting = f"Hello {self.first_name},you were born in {2024 - self.age}"
        return greeting

    def Student_initials(self):
        initials = f"Your initials are {self.first_name[0]} for first name and {self.last_name[0]} for your last name"
        return initials

    def Student_full_name(self):
        full_name = f"Your full name is {self.first_name} {self.last_name}"
        return full_name

    def enroll_student(self):
        enrollment = f"Input name: {self.first_name} {self.last_name} Age:{self.age} Country:{self.country} Student code:{self.code}" 
        return enrollment





    