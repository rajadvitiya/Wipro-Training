# radius = int(input('enter radius '))
#
# print('Area : ',areaofcircle(radius))
# print('Peri  : ',cicumofcircle(radius))

from mypack.basicsshapes import areaofsquare,perimeterofsquare

side = int(input('enter side of square'))

print('Area of square : ',areaofsquare((side)))
print('Perimeter : ',perimeterofsquare(side))

