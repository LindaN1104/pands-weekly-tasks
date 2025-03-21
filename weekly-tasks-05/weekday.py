# Weekly Task 05 - Part of coursework for ATU 24-25: 4122 -- PROGRAMMING AND SCRIPTING
# Author Linda Nikolajeva

# Programme that that outputs whether or not today is a weekday
# Per guidelines there is no user input
# In addition, it is not required to list what day of the week it is
# Only if it is a weekday or the weekend
'''
 I this case I assume that:
    Weekdays are Monday to Friday, and the weekend is Saturday and Sunday
    Public holidays, e.g. bank holidays, are not considered part of the weekend
    The time and date on the machine used, i.e. your laptop/desktop, is correct
    https://chatgpt.com/c/67d6007c-54ac-8005-87e5-723b19e46344
 '''

from datetime import date
# datetime is a module built into python, it allows me (us) to work with dates and times
# however, it must be imported 
# as python comes with many built in modules, but they are not automatically loaded into my programme
# supposedly this keeps python efficient, so only the necessary code is loaded
# importing just the date part makes sure I  don’t import unnecessary parts of datetime
# the code is also simpler because instead of using
    # today = datetime.datetime.today().weekday()
    # only this line is needed -> today = date.today().weekday() 

if date.today().weekday() < 5:
# this function gets the current day of the week, by returning a number between 0 to 6
# where 0 = monday, 1 = tuesday, 2 = wednesday etc.
# the if statement checks if today is less than 5 (meaning monday to friday)
# if it is 5 or 6 the programme autimatically assumes it is the weekend
    print('Yes, unfortunately today is a weekday. ')
    
else:
    print('It is the weekend, yay! ')
    # if today is 5 or 6 the programme moves to else, the next line of code

'''
since the task only asks to list whether it is a weekday or weekend, no list or dictionary is needed
if I wanted to display the name of the day, a list or dictionary would be needed

e.g. if I was to include a list, this is what it would look like
    list of days
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    to get the number associated with each weekday
        today_num = datetime.datetime.today().weekday()

    to get corresponding name
        today_name = days[today_num]'
            if today_num < 5:
                print(f"Today is {today_name}, a weekday.")
            else:
                print(f"Today is {today_name}, a weekend.

Additonally, if the name of the current day was needed elsewhere in the programme, 
then a list/ dictionary would be needed
'''

'''
This is also had me wondering how exactly this programme uses a boolean
The if statement evaluates a boolean expression
today < 5 checks if the number for today (0 to 6) is less than 5
The result is either true or false
If True, it runs the first block print('Yes, unfortunately today is a weekday. ')
If False, it runs the else block print('It is the weekend, yay! ')
So, while the whole program is not a boolean, it relies on a boolean condition to decide what to print
'''

# end