import math

if __name__ == "__main__":
    print('Welcome to Math Module')

def factorial():

    num = int(input('Enter number to find factorial:- '))
    print(f'\nFactorial of {num} is {math.factorial(num)}.\n\n')


def compund_interest():

    money = int(input('Enter principal amount:- '))
    rate = float(input('Enter annual interest rate:- '))
    cop_year = int(input('How many time compund your money in 1 year:- '))
    time = int(input('Enter the years of investment:- '))


    final_amount = money * math.pow((1+((rate/100)/cop_year)),(cop_year*time))

    print(f'\nCompund interest is {final_amount-money}\n')



def main():

    print('\nMathematical Operations:\n')

    while True: 

        print('1. Calculate Factorial')
        print('2. Compund Interest')
        print('3. Trigonometic Calculations')
        print('4. Are of Geometric Shapes')
        print('5. Back to Main Menu')

        choice = int(input('Enter your choice:- '))

        print('')

        match choice:
            case 1: 
                factorial()
            case 2: 
                compund_interest()
            case 3: 
                print('Coming soon')
            case 4:
                print('Coming soon')
            case 5:
                break
            case _:
                print('\nInvalid choice!\n')