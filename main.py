import math

while True:
    a = input('Enter "P" for Permutation and "C" for Combination: ').lower()
        
    if a == 'p':
        n = int(input('Enter the value of n: '))
        r = int(input('Enter the value of r: '))
        npr = math.factorial(n)/math.factorial(n-r)
        print(npr)
        break
    
    if a == 'c':
        n = int(input('Enter the value of n: '))
        r = int(input('Enter the value of r: '))
        ncr = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
        print(ncr)
        break

    else:
        print('Invalid input')
    
