import math


a = int(input('Input number: '))
b = int(input('Input number: '))
c = int(input('Input number: '))


x = (b**2) - (4*a*c)


def prva_solucija(a, b, c):
    if x < 0: 
        return 'Math error'
    return (-b-math.sqrt(x))/(2*a)

def druga_solucija(a, b, c):
    if x < 0: 
        return 'Math error'
    return (-b+math.sqrt(x))/(2*a) 


print(f'Prva solucija: {prva_solucija(a,b,c)}. Druga solucija: {druga_solucija(a,b,c)}')

