"""Student class blueprint"""

class Student:
    def __init__(self, name, age, major, university, city, country):
        self.name = name
        self.age = age
        self.major = major
        self.university = university
        self.city = city
        self.country = country

    def student_details(self):
        print(f"Student name: {self.name}, Age: {self.age}, Major: {self.major}, University: {self.university}, City: {self.city}, Country: {self.country}")


student = Student("Anowar", 24, "CSE", "Dong-Eui", "Busan", "South Korea")

student.student_details()
