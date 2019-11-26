from re import compile
import datetime
a = True
# Function with the pattern which the input raw-plate must match to be a valid plate.
# Input must be:
#    three letters -> [a-zA-Z]{3} followed by three numbers -> [0-9]{3}
#    or
#    three letters -> [a-zA-Z]{3} followed by four numbers -> [0-9]{3}
# Thats the two patterns of car plates allowed in Ecuador
def plate_checker(raw_plate):
    plate_format_a = compile('[a-zA-Z]{3}[0-9]{3}')
    plate_format_b = compile('[a-zA-Z]{3}[0-9]{4}')
    print(raw_plate)

    for plate in raw_plate:
        if plate_format_a.match(plate) is not None or plate_format_b.match(plate) is not None:
            print "Correct plate"
            get_last_digit(raw_plate)
        else:
            print "Incorrect plate"
            a = False
            break

# Function to get the last digit of the already checked car-plate
# Input must be the correct plate
#    Returns the last digit of the car plate
def get_last_digit(correct_plate):
    plate_str = str(correct_plate)
    last_digit = plate_str[-3]
    print last_digit
    return last_digit

# Function with the pattern the input-year must match to be valid
# Input must be a list containing the year
#    Returns the valid year
def year_checker(year):
    year_format = compile('[[0-9]{4}')
    print year
    for y in year:
        if year_format.match(y) is not None:
            print "Correct year"
            return year
            a = False
        else:
            print "Incorrect year"
            a = False
            break

# Function with the pattern the input-month must match to be valid
# Input must be a list containing the month
#    Returns the valid month
def month_checker(month):
    month_format_a = compile('[[0-9]{2}')
    month_format_b = compile('[[0-9]{1}')
    print month
    for m in month:
        if month_format_a.match(m) is not None or month_format_b.match(m) is not None:
            print "Correct month"
            return month
            a = False
        else:
            print "Incorrect month"
            a = False
            break

# Function with the pattern the input-day must match to be valid
# Input must be a list containing the day
#    Returns the valid day
def day_checker(day):
    day_format_a = compile('[[0-9]{2}')
    day_format_b = compile('[[0-9]{1}')
    print day
    for d in day:
        if day_format_a.match(d) is not None or day_format_b.match(d) is not None:
            print "Correct day"
            return day
            a = False
        else:
            print "Incorrect day"
            a = False
            break

# Function to get the name of the day corresponding to the date
# Input must be lists containing the year, month and day
#    Returns the name of the day as a string
def get_dayname(y,m,d):
    year = int(y[0])
    month = int(m[0])
    day = int(d[0])
    x = datetime.datetime(year, month, day)
    dayofweek = x.strftime("%A")
    print dayofweek
    return dayofweek

def check_time(raw_time):
    time_format = compile('[[0-9]{2}:[0-9]{2}')
    print raw_time
    for time in raw_time:
        if time_format.match(time) is not None:
            return get_hour_n_minute(raw_time)

        else:
            print "Incorrect time"
            a = False
            break

def get_hour_n_minute(correct_time):
    time = str(correct_time)
    hour = int(time[2:4])
    minute = int(time[5:7])
    if hour < 24 and minute < 60:
        print "Correct Time"
        checked_time = [hour,minute]
        print checked_time
        return checked_time
    else:
        print "Incorrect time"
        a = False

def main():
#while a == True:
    print "Welcome to \"Pico y Placa\" checker program"
    input_plate = [raw_input("Enter car-plates: ")]
    plate_checker(input_plate)

    print "Enter the date you want to check in order yyyy, mm, dd"
    input_year = [raw_input("Enter year: ")]
    year_checker(input_year)
    input_month = [raw_input("Enter month: ")]
    month_checker(input_month)
    input_day = [raw_input("Enter day: ")]
    day_checker(input_day)
    get_dayname(input_year,input_month,input_day)

    print "Enter the time you want to check in 24Hour format hh:mm"
    input_time = [raw_input("Enter time: ")]

    check_time(input_time)



if __name__ == "__main__":
    main()
