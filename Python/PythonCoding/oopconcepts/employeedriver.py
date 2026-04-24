#driver code
from oopconcepts.employeedetails import EmployeeDetails

eno = int(input('Emp no : '))
name = input('Emp name : ')
bp = int(input('basic pay : '))


emp1 = EmployeeDetails(empno=eno, ename=name, basicpay=bp)
print('Employee no : ',emp1.empno)
print('Employee name : ',emp1.ename)

print('net salary : ',emp1.calculate_netsal())
