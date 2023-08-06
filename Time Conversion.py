'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/time-conversion
'''



def timeConversion(s):
    # Extract hours, minutes, seconds, and AM/PM indicator from the input string
    time_parts = s.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds_ampm = time_parts[2]

    # Determine if it's AM or PM
    is_pm = seconds_ampm[-2:] == "PM"

    # Handle the special case of 12:00 AM and 12:00 PM
    if hours == 12:
        hours = 0

    # Convert to 24-hour format
    if is_pm:
        hours += 12

    # Format the output string in 24-hour format
    output_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, int(seconds_ampm[:2]))
    return output_string

# Test cases
a=input()
print(timeConversion(a))  # Output: 19:05:45
