"""
👉 Day 64 Challenge
In today's project, create classes to represent jobs.

Your program should

Create a generic 'job' class.
The init method will store the details for name, salary and hours worked.
'job' will have another method that prints those details nicely.
Create two sub-classes from job: 'doctor' and 'teacher'
The 'doctor' subclass should also include 'speciality' and 'years of experience'.
The 'teacher' subclass should also include 'subject' and 'position'.
The print functions for each sub-class should print this extra data.
Instantiate a lawyer, a computer science teacher, and a pediatric doctor (this is a doctor for children) with 7 years of experience.
Output the information for each job.
Example:

🌟Jobs Jobs Jobs!🌟
Job type: Lawyer
Salary: $ Squillions
Hours worked: 60
Job type: Teacher
Salary: $ Nowhere near enough
Hours worked: All of them
Subject: Computer Science
Position: Classroom Teacher
Job type: Doctor
Salary: $ Doing very nicely thank you
Hours worked: 50
Speciality: Pediatric Consultant
Years of Experience: 7

Hints:
* Copy the print method to each of your sub-classes and customize it for each one.
* Don't worry about keeping the same method name. The one in the sub-class will override the one in the 'job' main class.

"""


class Job:
    name: str = None
    salary: float = None
    hoursWorked: int = None

    def __init__(self, name, hoursWorked, salary):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def print(self):
        print("== JOB ==")
        print(
            f"Job name: {self.name}\nHours worked: {self.hoursWorked}\nSalary: ${self.salary}"
        )


class Doctor(Job):
    experience: str = None
    speciality: str = None

    def __init__(self, specialty, experience, hoursWorked, salary):
        super().__init__(self, hoursWorked, salary)
        self.name = "Doctor"
        self.experience = experience
        self.speciality = specialty

    def print(self):
        print("== JOB ==")
        print(
            f"Job name: {self.name}\nSpeciality: {self.speciality}\nExperience: {self.experience}\nHours worked: {self.hoursWorked}\nSalary: ${self.salary}"
        )


class Teacher(Job):
    subject: str = None
    position: str = None

    def __init__(self, subject, position, hoursWorked, salary):
        super().__init__(self, hoursWorked, salary)
        self.name = "Teacher"
        self.position = position
        self.subject = subject

    def print(self):
        print("== JOB ==")
        print(
            f"Job name: {self.name}\nSubject: {self.subject}\nPosition: {self.position}\nHours worked: {self.hoursWorked}\nSalary: ${self.salary}"
        )


lawyer = Job("Lawyer", 40, 4000)
doctor = Doctor("Pediatric Consultant", 7, 60, 5000)
teacher = Teacher("Computer Science", "Teacher", 40, 1000)

lawyer.print()
print()
doctor.print()
print()
teacher.print()


# -------------------------------------------------------------------------------
class Animal:
    species = None
    name = None
    sound = None

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def talk(self):
        print(f"{self.name} says {self.sound}")


class Bird(Animal):
    color = None

    def __init__(self, color):
        self.name = "bird"
        self.species = "avian"
        self.sound = "tweet"
        self.color = color


dog = Animal("dog", "canine", "woof")
cow = Animal("cow", "bo taurus", "moo")
polly = Bird("green")

# dog.talk()
# cow.talk()
# polly.talk()
# print(polly.color)
