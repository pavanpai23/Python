class employee:
    company="itc"
    def show(self):
        print(f"the name of the employeee id {self.company} and the salary is {self.salary}")


class progemmer(employee):
    company="info itc"
    def showlang(self):
        print(f"the name of the employeee id {self.company} and the salary is {self.language}")

a=employee()
b=progemmer()

print(a.company,b.company)