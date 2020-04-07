"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def print_header(header):

    print(f'\n--- {header} ---\n')
    return


def parse_call_args(args):

    errors = []
    year = None
    month = None

    if len(args) > 1:
        try:
            month = int(args[1])
        except:
            errors.append('MonthFormatError')

    if len(args) > 2:
        try:
            year = int(args[2])
        except:
            errors.append('YearFormatError')

    if len(args) > 3:
        errors.append('TooManyArgs')

    return (errors, year, month)


def handle_call_errors(errors):

    if 'MonthFormatError' in errors:
        print('''MonthFormatError
- Input `month` must be an `Int`.
''')

    if 'YearFormatError' in errors:
        print('''YearFormatError
- Input `year` must be an `Int`.
''')

    if 'TooManyArgs' in errors:
        print('''TooManyArgs
- This script was called with too many arguments.
- The call format is `<script_name> [month] [year]`.
''')

    if len(errors) > 0:
        exit(len(errors))

    return


def get_date(
    year=None,
    month=None,
    default=datetime.now()
):

    if year == None:
        year = default.year

    if month == None:
        month = default.month

    return (year, month)


############################################################
# MAIN
############################################################

# print_header('parse call args')
errors, user_year, user_month = parse_call_args(sys.argv)

# print_header('handle call errors')
handle_call_errors(errors)

# print_header('get date')
year, month = get_date(user_year, user_month)

# print_header('print month calendar')
cal = calendar.TextCalendar(-1)
print()
cal.prmonth(year, month)

# print_header('done')
exit(0)
