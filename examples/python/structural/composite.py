class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.subordinates = []

    def add(self, employee):
        self.subordinates.append(employee)

    def get_details(self):
        return (self.name, self.salary, [item.get_details() for item in self.subordinates])


manager = Employee("John", 100000)
manager.add(Employee("Jane", 80000))
