from oopconcepts.agecalc import AgeCalculation
from oopconcepts.myexception import AgeException

age = int(input('Enter your age '))

aobj = AgeCalculation()

try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)



except AgeException as ae:

    print(ae)

else:
    print('Eligible to vote contact next step... ')