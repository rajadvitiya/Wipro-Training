from symtable import Class


class Calc():
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def fdiv(self,a, b):
        return a / b


calobj = Calc()
# print(calobj.add(10,5))
# print(calobj.sub(10,5))
# print(calobj.mul(10,5))
numbers = [10,20,30]


try:
    res = calobj.fdiv(10,5)
    for i in range(len(numbers)+1):
        print(numbers[i])


except ZeroDivisionError,IndexError:
    print('Do not give in denominator')
    print('check the index')

else:
    print('result ',res)

finally:
    print('Done')
