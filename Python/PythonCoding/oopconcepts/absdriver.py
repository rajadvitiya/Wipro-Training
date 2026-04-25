from oopconcepts.rectangle import Rectangle
from oopconcepts.square import Square

sqobj = Square(10)

print(f'sq area {sqobj.calculate_area()} \t sq peri : {sqobj.calculate_perimeter()}')

recobj = Rectangle(10, 5)
print(f'rec area {sqobj.calculate_area()} \t rec peri : {sqobj.calculate_perimeter()}')


