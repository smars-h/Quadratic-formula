import math


a = int(input('Input number: '))
b = int(input('Input number: '))
c = int(input('Input number: '))


x = (b**2) - (4*a*c)


def first_solution(a: int, b: int, c: int) -> int:
    if x < 0: 
        return 'Math error'
    return (-b-math.sqrt(x))/(2*a)

def second_solution(a: int, b: int, c: int) -> int:
    if x < 0: 
        return 'Math error'
    return (-b+math.sqrt(x))/(2*a) 


print(f'First Solution: {first_solution(a,b,c)}. Druga solucija: {second_solution(a,b,c)}')

