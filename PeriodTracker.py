# Main program

import pandas as pd
import time
import calendar

def Enter_Data ():
    date = calendar.datetime.datetime.ctime
    print('1: Period Cramps Starts\n',
          '2: Period Cramps Persists\n',
          '3: Period Cramps Ends\n',
          '4: Ovulation Starts\n',
          '5: User Note')
    instanceType = getInstanceType() # Select from options 1 - 5 for now, would like to make a gui for this eventually
    
    def getInstanceType ():
        
        def invalidInput ():
            print('Invalid Input\n')
            getInstanceType()

        try:    
            match int(input()):
                case 1:
                    # Do something
                    return
                case 2:
                    # Do something
                    return
                case 3:
                    # Do something
                    return
                case 4:
                    # Do something
                    return
                case 5:
                    # Do something
                    return
                case _:
                    invalidInput()
        except ValueError:
            invalidInput()
    return

# Loads the tracked data from a file
def Load_Data ():
    with open ('.\\PeriodData.csv', 'r+') as infile:
        return

# Saves the tracked data to a file
def Save_Data ():
    with open ('.\\PeriodData.csv', 'w+') as outfile:
        return