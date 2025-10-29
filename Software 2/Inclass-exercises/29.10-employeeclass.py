class Employee:
    total = 0
    def __init__(self, name, last_name):
        Employee.total += 1
        self.employee_number = Employee.total
        self.name = name
        self.last_name = last_name

    def print_information(self):
        print(f"Employee number {self.employee_number}: {self.name} {self.last_name}")

class HourlyPaid(Employee):

    def __init__(self, name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(name, last_name) #super calls the upper class

    def print_information(self):
        super().print_information()
        print(f"Hourly pay: {self.hourly_pay}")

class MonthlyPaid(Employee):

    def __init__(self, name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(name, last_name) #super calls the upper class

    def print_information(self):
        super().print_information()
        print(f"Monthly pay: {self.monthly_pay}")

employees = []
emp1 = Employee("Viivi", "Virta")
emp2 = Employee("Ahmed", "Habib")
emp3 = HourlyPaid("Pekka", "Puro", 14.50)
emp4 = MonthlyPaid("Timo", "Salin", 1500.70)

employees.append(emp1)
employees.append(emp2)
employees.append(emp3)
employees.append(emp4)

for e in employees:
    e.print_information()

#subclasses inherited from the base class


