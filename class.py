class Employee:
    def __init__(self,fname,lname,pay,email):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@' + 'gmail' + '.' + 'com'
    
    def fullname(self):
        return  '{} {}'.format(self.fname, self.lname)   
    
emp1 = Employee('Raj', 'Chhapariya', 50000 , 'raj.chhapariya@gmail.com')
emp2 = Employee('Raunak', 'Chhapariya', ' 60000', 'raunak.chhapariya@gmail.com')

print(emp2.email)
print(emp2.fullname())
print(Employee.fullname(emp1))
print(emp1.fullname())