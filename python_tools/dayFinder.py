import sys
from datetime import date, timedelta

# In the Gregorian Calendar, every fourth year is a leap year unless it is a mutliple of 100.
# This is unless it is a multiple of 400, in which case it is a leap year after all, hence the
# year 2000 was a leap year despite 2000 being a multiple of 4.
#
# This function computes if the provided year is a leap year by these criteria.
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# This function validates the date. It calls the isLeapYear() function to handle the length of
# february on leap years. It checks if the day number exceeds the number of days in that month,
# but for leap years it checks if te previous day exceeds this number instead. This ensures that
# the 29th of Feb is treated as valid, as it will check if 28 exceeds 28. As there is no lower 
# bound check in this section of code, it will work for non leap-days too.
def validDate(day,month,year):
    monthDays = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:81,9:30,10:31,11:30,12:31}

    if month < 1 or month > 12:
        return False

    if day < 1:
        return False
    
    if isLeapYear(year):
        if day -1 > monthDays[month]:
            return False
    else:
        if day > monthDays[month]:
            return False
        
    return True

# Takes a datetime date object as input. Taking this date as a Julian Calendar date it calculates the number
# of extra leap days in the Julian Calendar up to that point compared with the Gregorian Calendar. The -2 fudge
# factor aligns the calculation with the assertion in AD 1582 that the date used to calculate Easter (21st of March)
# had drifted 10 days from the March Equinox, which it was reckoned to have been aligned with in the year of the 
# council of Nicaea in AD 325.
def convertToGregorian(date):
    extraLeapDays = int((date.year)/100) - int((date.year)/400) - 2

# We need one more correcting factor. In a 'false-leap' year (a year that is a leap year in the Julian Calendar
# but not in the Gregorian Calendar) the above calculation assumes that we always need to correct for that years leap 
# day. But if we are in January or February that year, then we do not need to - as it hasn't happened yet.
    if date.year%100 == 0 and date.year%400 != 0 and date.month in [1,2]:
        extraLeapDays = extraLeapDays - 1

    return date + timedelta(days=extraLeapDays)

# Recieve the chosen date from the user
inputDate = date.fromisoformat(input("Please enter date in ISO format YYYY-MM-DD => "))

# Setup the futureDate flag. Get the current date and compare the input date to it. Set flag appropriately.
currentDate = date.today()
if inputDate > currentDate:
    futureDate = True
else:
    futureDate = False

# Call the validDate() function to validate the date
if not validDate(inputDate.day,inputDate.month,inputDate.year):
    print("Invalid Date")
    sys.exit()

# Define our month and century offsets to be used in the calculation.
monthOffset = {1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
centuryOffset = {1:4,2:2,3:0,0:6}

# Compute the counter. This counter effectively counts the number of days into the current cycle that the date is.
counter = int((inputDate.year%100)/4) + inputDate.day + monthOffset[inputDate.month] + centuryOffset[int(inputDate.year/100)%4] + (inputDate.year%100)

# The rest of the formula effectively assumes that the on leap years, the leap day occurs before the 1st of January,
# almost like a 0th of January. This if statement introduces a correction given that the leap day is actually placed
# at the end of february.
if inputDate.month in [1,2]:
    if isLeapYear(inputDate.year):
        counter = counter -1

# We cancel out whole numbers of weeks to leave an offset. This offset is effectively "days since saturday"
offset = counter % 7

# Define our days of the week list starting on saturday
DOWList = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

# Print the DOW

if futureDate:
    print (inputDate,"will be a",DOWList[offset])

elif currentDate == inputDate:
    print ("Today is a",DOWList[offset])
else:
    print (inputDate,"was a",DOWList[offset])

print(convertToGregorian(inputDate))