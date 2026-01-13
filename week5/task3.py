class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        return f"I am {self._name}, {self._age} years old."

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        return f"I am {self._name}, {self._age}, studying {self.major}."

p = Person("Alina", 30)
s = Student("Nurkhan", 20, "Cybersecurity")

print(p.introduce())
print(s.introduce())
