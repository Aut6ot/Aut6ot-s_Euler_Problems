#     THE PROMPT:
#     ==========================================================================================================
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#     How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#     ==========================================================================================================

LEAP_YEAR_MONTH = 29
months_in_a_year = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days_in_a_month = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}


def is_leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:  # special condition for Centuries
            if x % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Sundays In A Year: Provide the day of the first sunday.
def sundays_in_a_year(starting_sunday, year):
    date = starting_sunday
    year_carryover = 0
    first_sundays = 0
    for month in months_in_a_year:
        # Ensure February has 29 days in a leap year
        if month == "Feb" and is_leap_year(year):
            month_max = LEAP_YEAR_MONTH
            # print(f"For the month of: {month}; ({month_max} days-- {year} is a LEAP YEAR!)")
        else:
            month_max = days_in_a_month[month]
            # print(f"For the month of: {month}; ({month_max} days)")

        # Check if 1st sunday of the month
        if date == 1:
            print(f"{month} in {year} started on a Sunday!!!")
            first_sundays += 1

        # Determine the Sundays of the month; Track the day #.
        while date <= month_max:
            date += 7
        if date > month_max:  # backtrack if went over month capacity
            date -= 7
        remaining_days = month_max - date

        # the first sunday for the next month
        date = 7 - remaining_days
        if month == "Dec":
            year_carryover = date
            # print(f"CARRYOVER FOR THE YEAR: {date}")
    carryover_and_sunday_count = [year_carryover, first_sundays]
    return carryover_and_sunday_count


def counting_sundays(first_sunday, start_year):
    # Determine the date of the first Sunday in 1901.
    carryover_and_sunday_count = sundays_in_a_year(first_sunday, start_year)
    first_sunday = carryover_and_sunday_count[0]

    # First year starts with Sunday, Jan 6th, 1901
    sunday_counter = 0
    for year in range(1901, 2001):
        result = sundays_in_a_year(first_sunday, year)
        first_sunday = result[0]
        sunday_counter += result[1]
        print(f"{year} had {result[1]} months starting with Sunday.")
    print(f"TOTAL: There were {sunday_counter} months that started with Sunday between 1901 and 2000.")


counting_sundays(7, 1900)
