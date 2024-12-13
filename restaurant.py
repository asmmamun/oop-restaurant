from menu import Menu
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print(f'***Employee List***')
        for emp in self.employee:
            print(f"{emp.name}\t{emp.phone}\t{emp.email}\t{emp.address}\t{emp.designation}\t{emp.salary}")
