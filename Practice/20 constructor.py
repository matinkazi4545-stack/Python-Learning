class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    student1 = Student("Rahul", 20)
    print("Name:", student1.name)
    print("Age:", student1.age)
