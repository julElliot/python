import datetime
import sys
from time import sleep
import os
SYMBOL = "\u2593"

class Zero():
    first = f'{SYMBOL * 5}'
    second = f'{SYMBOL * 1}   {SYMBOL * 1}'
    third = f'{SYMBOL * 1}   {SYMBOL * 1}'
    forth = f'{SYMBOL * 1}   {SYMBOL * 1}'
    fifth = f'{SYMBOL * 5}'

class One():
    first = f'{SYMBOL * 3}  '
    second = f'  {SYMBOL * 1}  '
    third = f'  {SYMBOL * 1}  '
    forth = f'  {SYMBOL * 1}  '
    fifth = f'{SYMBOL * 5}'

class Two():
    first = f'{SYMBOL * 5}'
    second = f'    {SYMBOL * 1}'
    third = f'{SYMBOL * 5}'
    forth = f'{SYMBOL * 1}    '
    fifth = f'{SYMBOL * 5}'

class Three():
    first = f'{SYMBOL * 5}'
    second = f'    {SYMBOL * 1}'
    third = f'{SYMBOL * 5}'
    forth = f'    {SYMBOL * 1}'
    fifth = f'{SYMBOL * 5}'

class Four():
    first = f'{SYMBOL * 1}   {SYMBOL * 1}'
    second = f'{SYMBOL * 1}   {SYMBOL * 1}'
    third = f'{SYMBOL * 5}'
    forth = f'    {SYMBOL * 1}'
    fifth = f'    {SYMBOL * 1}'

class Five():
    first = f'{SYMBOL * 5}'
    second = f'{SYMBOL * 1}    '
    third = f'{SYMBOL * 5}'
    forth = f'    {SYMBOL * 1}'
    fifth = f'{SYMBOL * 5}'

class Six():
    first = f'{SYMBOL * 5}'
    second = f'{SYMBOL * 1}    '
    third = f'{SYMBOL * 5}'
    forth = f'{SYMBOL * 1}   {SYMBOL * 1}'
    fifth = f'{SYMBOL * 5}'

class Seven():
    first = f'{SYMBOL * 5}'
    second = f'    {SYMBOL * 1}'
    third = f'    {SYMBOL * 1}'
    forth = f'    {SYMBOL * 1}'
    fifth = f'    {SYMBOL * 1}'

class Eight():
    first = f'{SYMBOL * 5}'
    second = f'{SYMBOL * 1}   {SYMBOL * 1}'
    third = f'{SYMBOL * 5}'
    forth = f'{SYMBOL * 1}   {SYMBOL * 1}'
    fifth = f'{SYMBOL * 5}'

class Nine():
    first = f'{SYMBOL * 5}'
    second = f'{SYMBOL * 1}   {SYMBOL * 1}'
    third = f'{SYMBOL * 5}'
    forth = f'    {SYMBOL * 1}'
    fifth = f'{SYMBOL * 5}'

class Separator():
    first = f'     '
    second = f'  {SYMBOL * 1}  '
    third = f'     '
    forth = f'  {SYMBOL * 1}  '
    fifth = f'     '

def printClock(firstHour, secondHour, separator, firstMinute, secondMinute, firstSec, secondSec):
    print(firstHour.first + '   ' + secondHour.first + separator.first + firstMinute.first + '   ' + secondMinute.first + separator.first + firstSec.first + '   ' + secondSec.first)
    print(firstHour.second + '   ' + secondHour.second + separator.second + firstMinute.second + '   ' + secondMinute.second + separator.second + firstSec.second + '   ' + secondSec.second)
    print(firstHour.third + '   ' + secondHour.third + separator.third + firstMinute.third + '   ' + secondMinute.third + separator.third + firstSec.third + '   ' + secondSec.third)
    print(firstHour.forth + '   ' + secondHour.forth + separator.forth + firstMinute.forth + '   ' + secondMinute.forth + separator.forth + firstSec.forth + '   ' + secondSec.forth)
    print(firstHour.fifth + '   ' + secondHour.fifth + separator.fifth + firstMinute.fifth + '   ' + secondMinute.fifth + separator.fifth + firstSec.fifth + '   ' + secondSec.fifth)

def timeParser(time):
    if time < 10:
        firstNumber = Zero()
        number = int(str(time)[0])
        secondNumber = numbers[number]
    else:
        number = int(str(time)[0])
        firstNumber = numbers[number]
        number = int(str(time)[1])
        secondNumber = numbers[number]
    return firstNumber, secondNumber

numbers = {
    0: Zero(),
    1: One(),
    2: Two(),
    3: Three(),
    4: Four(),
    5: Five(),
    6: Six(),
    7: Seven(),
    8: Eight(),
    9: Nine()
}

def main():
    separator = Separator()
    try:
        while True:
            sec = datetime.datetime.now().second
            min = datetime.datetime.now().minute
            hour = datetime.datetime.now().hour

            firstHour, secondHour = timeParser(hour)
            firstMinute, secondMinute = timeParser(min)
            firstSec, secondSec = timeParser(sec)

            printClock(firstHour, secondHour, separator, firstMinute, secondMinute, firstSec, secondSec)
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        print()
        print("Leaving clock")

if __name__ == "__main__":
    main()



