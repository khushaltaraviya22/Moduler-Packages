from datetime import datetime
import time

if __name__ == "__main__":
    print('Welcome to DateTime Module')

now = datetime.now()


def current_dateTime():
    print(f'Current Date and Time {now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}\n')


def difference():
    
    diffChoice = input('Date or Time(1 or 2): ')

    if diffChoice in ['Date', 'date', '1']:

        stDate = input('Enter start date(YYYY-MM-DD):- ')
        enDate = input('Enter end date(YYYY-MM-DD):- ')
        diff = datetime.strptime(enDate,'%d-%m-%Y') - datetime.strptime(stDate,'%d-%m-%Y')
        print(f'\nDifference of {diff.days} days.\n')

    elif diffChoice in ['Time', 'time', '2']:

        stTime = input('Enter start time(hh-mm-ss):- ')
        enTime = input('Enter end time(hh-mm-ss):- ')

        stTime = datetime.strptime(stTime,'%H:%M:%S')
        enTime = datetime.strptime(enTime,'%H:%M:%S')

        diff = enTime - stTime

        total_seconds = int(diff.total_seconds())

        hours = total_seconds
        minutes = (total_seconds % 3600)
        seconds = total_seconds % 60

        print(f"\nDifference: {hours} hours {minutes} minutes {seconds} seconds\n")

    else:
        print('Invalid choice')



def formate_date():

    date = input('\nEnter date(DD-MM-YYYY hh:mm:ss):- ')

    date  = datetime.strptime(date, '%d-%m-%Y %H:%M:%S')

    format_string = input('Enter date formate which is you want. Ex.(%d-%m-%Y %H:%M:%S)):- ')

    formatted_date = date.strftime(format_string)

    print(F'\nFormatted Date:- {formatted_date}\n')


def stopWatch():
    print('Comming soon')


def countDown_timer():

    sec = 0

    while True:

        minutues = sec // 60
        hours = minutues // 60
        seconds = sec % 60
        minutues = minutues % 60

        print(f'{hours}:{minutues}:{seconds}')
        time.sleep(1)
        sec+=1

                

def main():

    print('\nDatetime and Time Operations:\n')

    while True: 

        print('1. Display current date and time')
        print('2. Calculate difference between two dates/times')
        print('3. Formate date into custom format')
        print('4. Stopwatch')
        print('5. Countdown timer')
        print('6. Back to Main Menu')

        choice = int(input('Enter your choice:- '))

        print('')

        match choice:
            case 1: 
                current_dateTime()
            case 2: 
                difference()
            case 3: 
                formate_date()
            case 4:
                stopWatch()
            case 5:
                countDown_timer()
            case 6:
                break
            case _:
                print('\nInvalid choice!\n')

