class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_role(self):
        return "Employee"

    def get_salary(self):
        return self._salary

class Manager(Employee):
    def __init__(self, salary, bonus_rate):
        super().__init__(salary)
        self.bonus_rate = bonus_rate

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * self.bonus_rate

employees = [
    Employee(200000),
    Manager(350000, 0.15),
    Employee(180000)
]

for e in employees:
    print(e.get_role(), "-", e.get_salary())
