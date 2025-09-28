class Employee:
    def __init__(self):
        self.id = 52562
        self.salary = 500000
        self.designation = "Soul Society"

    def travel(self,destination):
        print("Employee is not travelling to the "+ destination)


# creating an object 
raj = Employee()

print(raj.id)
raj.travel("Hyogaku")

print(type(raj))