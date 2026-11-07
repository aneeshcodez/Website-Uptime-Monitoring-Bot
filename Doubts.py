class Employee:
    # Constructor
    def __init__(self,first,last,pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + "gmail.com"

    # Method
    def emp_full_name(self):
        return self.first + " " + self.last


emp_1 = Employee("Lucy",500)
emp_2 = Employee("Luky","Eoritz",600)

print(emp_1)
print(emp_2)