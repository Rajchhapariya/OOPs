class Employee:
    number_of_employees = 0
    raise_amount = 1.09
    
    def __init__(self,fname,lname,pay,email):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@' + 'gmail' + '.' + 'com'
        Employee.number_of_employees += 1
    
    def fullname(self):
        return  '{} {}'.format(self.fname, self.lname)   
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def inc_emp(cls, new_emp):
        cls.number_of_employees = new_emp
        print(new_emp)    
                
print(Employee.number_of_employees)
emp1 = Employee('Raj', 'Chhapariya', 50000 , 'raj.chhapariya@gmail.com')
emp2 = Employee('Raunak', 'Chhapariya',60000, 'raunak.chhapariya@gmail.com')
print(Employee.number_of_employees)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
Employee.inc_emp(5)