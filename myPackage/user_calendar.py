import calendar

# Enter the month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

cal = calendar.calendar(2019,2)
print cal