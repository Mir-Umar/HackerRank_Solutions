import os
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    # Calculate the absolute difference in seconds
    difference_seconds = abs((time1 - time2).total_seconds())
    
    return int(difference_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()



# The datetime.strptime() function in Python is used to parse a string representing a date and time into a datetime object. It stands for "string parse time". This function takes two arguments: the string to parse and the format string that specifies the format of the input string.

# The format string consists of format codes, also known as placeholders or directives, that represent various components of the date and time. These placeholders tell Python how to interpret each part of the input string.

# Here are some common format codes used in the datetime.strptime() function:

# %Y: Year with century as a decimal number (e.g., 2023).
# %m: Month as a zero-padded decimal number (01 to 12).
# %d: Day of the month as a zero-padded decimal number (01 to 31).
# %H: Hour (24-hour clock) as a zero-padded decimal number (00 to 23).
# %M: Minute as a zero-padded decimal number (00 to 59).
# %S: Second as a zero-padded decimal number (00 to 59).
# %a: Abbreviated weekday name (e.g., Mon).
# %b: Abbreviated month name (e.g., Jan).
# %z: UTC offset in the form +HHMM or -HHMM (e.g., +0530).
# You can combine these placeholders in any order to match the format of your input string. For example, if your input string is in the format "Wed 27 Oct 2021 14:30:00", you would use the format string "%a %d %b %Y %H:%M:%S" to parse it.
