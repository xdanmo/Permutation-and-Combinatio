import math

a = input("[1] for Permutation\n[2] for Combination\n[3] for both\nEnter: ")

while True:
    
    if a=='1':
        n = int(input('Enter the value of "n": '))
        r = int(input('Enter the value of "r": '))
        nr = n-r

        NPR = math.factorial(n)/(math.factorial(nr))
        print('NPR = ',NPR)
        break

    elif a=='2':
        n = int(input('Enter the value of "n": '))
        r = int(input('Enter the value of "r": '))
        nr = n-r

        NCR = math.factorial(n)/(math.factorial(r)*math.factorial(nr))
        print('NCR = ',NCR)
        break

    elif a=='3':
        n = int(input('Enter the value of "n": '))
        r = int(input('Enter the value of "r": '))
        nr = n-r
        
        NPR = math.factorial(n)/(math.factorial(nr))
        print('NPR = ',NPR)
        NCR = math.factorial(n)/(math.factorial(r)*math.factorial(nr))
        print('NCR = ',NCR)
        break
        
    else:
        print('Invalid input, please try again.')

    a = input('Enter: ')
        

        
        
