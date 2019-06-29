import datetime
from os import *
from time import *
import webbrowser


def main():

    print("This is a simple countdown timer program.\nPlease use the following guide:\n\n")
    print("\tEnter 1:18:26 for 1 hour 18 minutes and 26 seconds.")
    print("\tEnter 18:26 for 18 minutes and 26 seconds.")
    print("\tEnter 26 for 26 seconds.\n\nNote: Max limit 24 hours only.\n\n")
   
    while True: #The loop ensures asking for a correct input if the privious inputs go wrong.
        duration_input = input("Enter the duration for the timer:\n")
        try:
            duration = [int(time) for time in duration_input.split(":")] #Creating a list of the time duration entered as [HH,MM,SS]
            if durationCheck(duration): #If True, break.
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM:SS or MM:SS or SS format.")

    seconds = timeInSec(duration)
    print("\n\nTimer started...")
    
    while True:
        print(f"Time left:\n\t{datetime.timedelta(seconds = seconds)}") #Prints the time left for the countdown to stop
        seconds -= 1 
        sleep(1) #Sleeping for a second with each decrement of a second.
        if seconds == 0: #Stop when time is over.
            break 
        clearScreen() #Clearing screen every time a new left over time is displayed.

    print("Time's up!")
    ringAlarm() #Ring alarm once done

def durationCheck(duration):
    '''
    Will check if the user input for the duration entered is valid or not. 
    Argument(s):
    duration: A list. Each index holds the value of specific time duration in HH:MM:SS format.
    '''
    if len(duration) == 1: #When only second(s) is/are entered.
        if duration[0] >= 0 and duration[0] <=60:
            return True
    elif len(duration) == 2: #When minute(s) and second(s) are entered.
        if duration[0] < 60 and duration[0] >= 0 and \
           duration[1] < 60 and duration[1] >= 0: 
            return True
    elif len(duration) == 3: #When hour(s), minute(s) and second(s) are entered.
        if duration[0] < 24 and duration[0] >= 0 and \
           duration[1] < 60 and duration[1] >= 0 and \
           duration[2] < 60 and duration[2] >= 0:
            return True
    else:
        return False

def clearScreen(): 
    '''
    Will clear the screen when you call it. We use it to show the countdown happening for each seconds.
    '''
    if name == 'nt': #For Windows OS
        _ = system('cls') 
    else: #For the others 
        _ = system('clear') 
  
def ringAlarm(): 
    '''
    Will play an alarm tone (a YouTube video) when called.
    '''
    webbrowser.open("https://youtu.be/iNpXCzaWW1s")

def timeInSec(duration):
    '''
    Will reduce the duration given to seconds.
    Argument(s):
    duration: A list. Each index holds the value of specific time duration in HH:MM:SS format.
    '''
    duration.reverse() #Since, seconds can be entered as '5' for 5 seconds, we reverse the list of duration to match correctly with the factors.
    factors = [1, 60, 3600] #Factors to be multiplied to each of SS, MM and HH for getting the time in seconds.
    duration_in_sec = sum([fact*time for fact,time in zip(factors[:len(duration)], duration)]) 
    return duration_in_sec

if __name__ == '__main__':
    main()
