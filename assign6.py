a = int(input('enter the first number'))
b = int(input('enter the second number'))
def larger_number(a,b):
    if a>b:
        print(f'{a}is the largest')
    else:
        print(f'{b}is the largest')
        
larger_number(a,b)