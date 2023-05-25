from __future__ import print_function
import datetime


def check_season(month):
    """
    Checks for a season where a month belongs
    This is achieved through importing the datetime module in python
    Finding the name of the module
    Finally knowing the seasons of the year
    and classifying the months of the year into their rsepective seasons
    """
    month_object = datetime.datetime.strptime(month, "%m")
    month_name = month_object.strftime("%B")

    if (month_name == "March"
            or month_name == "April"
            or month_name == "May"):
        return (f"{month_name} is in  Spring.")
    elif (month_name == "June"
            or month_name == "July"
            or month_name == "August"):
        return (f"{month_name} is in Summer.")
    elif (month_name == "September"
            or month_name == "October"
            or month_name == "November"):
        return (f"{month_name} is in Autumn.")
    elif (month_name == "December"
            or month_name == "January"
            or month_name == "February"):
        return (f"{month_name} is in Winter.")


# Enter any value between 1 and 12 as a string type
month = str(input("Enter number of the month: "))

# We have 12 months in a year, we enter 1 - 12 as a string
# Otherwise you an error is displayed i.e invalid month

if (month == '1' or month == '2' or month == '3' or month == '4'
        or month == '5' or month == '6' or month == '7' or month == '8'
        or month == '9' or month == '10' or month == '11' or month == '12'):
    print(check_season(month))
else:
    print("Enter a valid month")
