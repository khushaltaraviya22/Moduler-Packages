import random

if __name__ == "__main__":
    print('Welcome to Random Module')


def rand_num():

    stNum = int(input('Enter Start Range number to generate random numbe:- '))
    enNum = int(input('Enter End Range number to generate random numbe:- '))

    print(f'\nRandom number is:- {random.randint(stNum,enNum)}\n')


def rand_list():

    list = []
    ele = int(input('Enter lenght of the random list:- '))

    for i in range(0,ele):

        temp = random.randint(1, 1000)

        list.append(temp)

    print(f'\nRandom List is {list}\n')


def rand_pass():

    char_li = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    sym_li = ['%','*','#','@','!','$','&']

    password = f'{random.randint(1,100)}{random.choice(char_li)}{random.choice(sym_li)}{random.randint(1,100)}{random.choice(char_li)}{random.choice(sym_li)}{random.choice(char_li)}{random.choice(sym_li)}\n'


    print(f'Random Password is {password}')

def rand_otp():

    otp = random.randint(100000,999999)

    print(f'Random OTP is {otp}\n')



def main():

    print('\nRandom Data Generation:\n')

    while True: 

        print('1. Generate Random Number')
        print('2. Generate Random List')
        print('3. Create Random Password')
        print('4. Generate Random OTP')
        print('5. Back to Main Menu')

        choice = int(input('Enter your choice:- '))

        print('')

        match choice:
            case 1: 
                rand_num()
            case 2: 
                rand_list()
            case 3: 
                rand_pass()
            case 4:
                rand_otp()
            case 5:
                break
            case _:
                print('\nInvalid choice!\n')