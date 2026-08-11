class emplyoee:
    language="py"  #this is a class atribute
    salary=1400000


    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

        
    def info(self):
        print(f" the langugage is{self.language} and the salary is {self.salary}")
    
pavan=emplyoee("pavan",12000000,"java")
print(pavan.name,pavan.salary,pavan.language)