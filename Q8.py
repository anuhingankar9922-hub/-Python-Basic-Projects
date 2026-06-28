class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   # Tuple

    def show_details(self):
        print()
        print("Employee ID :", self.emp_id)
        print("Name :", self.name)
        print("Department :", self.details[0])
        print("Salary :", self.details[1])


employees = {}

for i in range(3):
    print(f"\nEnter Details of Employee {i+1}")
    emp_id = input("\nEnter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, salary)

    employees[emp_id] = emp

print("\n:---:---: Employee Details :---:---:")

for emp in employees.values():
    emp.show_details()