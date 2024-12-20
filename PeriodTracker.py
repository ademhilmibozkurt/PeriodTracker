# Main program

import time
import calendar
import pandas as pd

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
                    return 1
                case 2:
                    # Do something
                    return 2
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
    extra = input('Provide extra explanation.\n')

    TrackPoint = {'date':date, 'type':instanceType, 'extra':extra}
    return TrackPoint


def create_df(df:pd.DataFrame, TrackPoint:dict):
    return pd.DataFrame(data=TrackPoint).T

# Loads the tracked data from a file
def Load_Data (path:str):
    try: 
        with open (path, 'r') as infile:
            return infile.read()
    except FileNotFoundError:
        print('File not found!')

# Saves the tracked data to a file
def Save_Data (path:str, df:pd.DataFrame):
    with open (path, 'a') as outfile:
        outfile.write(df)

def main():
    trackPoint:dict = Enter_Data()
    df = create_df(trackPoint) 
    Save_Data('.\\PeriodData.csv', df)

if '__name__' == '__main__':
    main()