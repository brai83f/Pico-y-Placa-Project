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
    plate_format_a = compile('^[a-zA-Z]{3}[0-9]{3}$')
    plate_format_b = compile('^[a-zA-Z]{3}[0-9]{4}$')
    print(raw_plate)

    for plate in raw_plate:
        if plate_format_a.match(plate) is not None or plate_format_b.match(plate) is not None:
            print "Correct plate-format"
            return get_last_digit(raw_plate)
        else:
            print "Incorrect plate-format!!! Try again"
            main()

# Function to get the last digit of the already checked car-plate
# Input must be the correct plate
#    Returns the last digit of the car plate
def get_last_digit(correct_plate):
    plate_str = str(correct_plate)
    last_digit = int(plate_str[-3])
    return last_digit

# Function with the pattern the input-year must match to be valid
# Input must be a list containing the year
#    Returns the valid year
def year_format_checker(year):
    year_format = compile('^[0-9]{4}$')
    print year
    for y in year:
        if year_format.match(y) is not None:
            int_year = int(year[0])
            if int_year < 1900 or int_year > 3000:
                print "Out of range year!!! Please try a valid year"
                return 0
            print "Correct year-format"
            return year
        else:
            print "Incorrect year-format!!! Try it like \'yyyy\'"
            return 0

# Function with the pattern the input-month must match to be valid
# Input must be a list containing the month
#    Returns the valid month
def month_format_checker(month):
    month_format_a = compile('^[0-9]{2}$')
    month_format_b = compile('^[0-9]{1}$')
    print month
    for m in month:
        if month_format_a.match(m) is not None or month_format_b.match(m) is not None:
            int_month = int(month[0])
            if int_month < 1 or int_month > 12:
                print "Out of range month!!! Please try a valid month"
                return 0
            print "Correct month-format"
            return month
        else:
            print "Incorrect month-format!!! Try it like \'mm\'"
            return 0

# Function with the pattern the input-day must match to be valid
# Input must be a list containing the day
#    Returns the valid day
def day_format_checker(day):
    day_format_a = compile('^[0-9]{2}$')
    day_format_b = compile('^[0-9]{1}$')
    print day
    for d in day:
        if day_format_a.match(d) is not None or day_format_b.match(d) is not None:
            int_day = int(day[0])
            if int_day < 1 or int_day > 31:
                print "Out of range day!!! Please try a valid day"
                return 0
            print "Correct day-format"
            return day
        else:
            print "Incorrect day-format!!! Try it like \'dd\'"
            return 0

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

def input_date():
    input_year = [raw_input("Enter year \'yyyy\': ")]
    while year_format_checker(input_year) == 0:
        input_year = [raw_input("Enter year \'yyyy\': ")]
    y = input_year

    input_month = [raw_input("Enter month \'mm\': ")]
    while month_format_checker(input_month) == 0:
        input_month = [raw_input("Enter month \'mm\': ")]
    m = input_month

    input_day = [raw_input("Enter day \'dd\': ")]
    while day_format_checker(input_day) == 0:
        input_day = [raw_input("Enter day \'dd\': ")]
    d = input_day
    return y,m,d

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

def day_n_number(day_name):
    weekdays = {
        1: "Monday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        6: "Wednesday",
        7: "Thursday",
        8: "Thursday",
        9: "Friday",
        0: "Friday",
        }
    return weekdays.get(day_name, "There's not Pico y Placa running this day!!!")

def main():

    print "Welcome to \"Pico y Placa\" checker program"
    input_plate = [raw_input("Enter car-plates: ")]
    car_plate = plate_checker(input_plate)
    print car_plate

    print "Enter the date you want to check in this order -> yyyy, mm, dd"
    date = input_date()
    print date
    get_dayname(date[0],date[1],date[2])

    print "Enter the time you want to check in 24Hour format hh:mm"
    input_time = [raw_input("Enter time: ")]

    check_time(input_time)



if __name__ == "__main__":
    main()
