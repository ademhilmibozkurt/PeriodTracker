# Main program

#import pandas as pd
import time
import calendar

TrackPoint = {'date':'', 'type':'', 'extra':''}
InstanceType = {'Period Cramps Start':1, 'Period Cramps Persist':2, 'Period Cramps End':3, 'Ovulation Starts': 4, 'User Note':5}

def Enter_Data ():
    date = calendar.datetime.datetime.ctime
    print('Enter a number corresponding to the type of data you\'d like to track:\n', InstanceType)
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
    instanceType = getInstanceType() # Select from options 1 - 5 for now, would like to make a gui for this eventually
    
    return

# Loads the tracked data from a file
def Load_Data ():
    with open ('.\\PeriodData.csv', 'r+') as infile:
        return

# Saves the tracked data to a file
def Save_Data ():
    with open ('.\\PeriodData.csv', 'w+') as outfile:
        return

