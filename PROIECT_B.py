import PROGECT_A
import exceptions
import time
# This file will convert the amounts from Kilogram to Gram and vice versa .
# But this is just a simple example .
# You can understand as well as develop your earnings .
# Source_Name_Make = HALIM _ HIOUANI .
# This file is for vulnerable people in Python .
#
# This Python file uses the following encoding: utf-8

if __name__ == '__main__':
    V = float(input('YOUR VALUE :'))
    if V <= 0:
        print('\n THIS IS A FALSE VALUE < Must be greater than zero >\n')
    else:
        APP = PROGECT_A.TRANSFORM(VALUE=V)
        TALL = 16
        CHOICE = ['\t'*TALL, 'C', 'H', 'O', 'I', 'C', 'E', '', 'Y', 'O', 'U', 'R', '', 'V', 'A', 'L', 'U', 'E', ' :',
                  '\n\n']
        COUNTER = 0
        while COUNTER < CHOICE.__len__():
            """ LOOP CHOICE """
            time.sleep(.4)
            print CHOICE[COUNTER],
            COUNTER += 1

        RESPONSE = '< To convert from kg to gram, press : 1 > or < To convert from gram to kg, press : 2 > or ' \
                   '< Displays the item description : 3>'
        print(RESPONSE)

        CHECK = int(input('THE CHOICE : '))
        CK = [1, 2, 3]
        if CHECK == CK[0]:
            APP.__mul__()
        elif CHECK == CK[1]:
            APP.__pow__()
        elif CHECK == CK[2]:
            print PROGECT_A.TRANSFORM.__doc__
        else:
            ERROR = 'THIS VALUE NOT IN LIST '
            print(exceptions.ValueError, ERROR)
