from datetime import date, datetime
today = date(datetime.today().year, datetime.today().month, datetime.today().day)
day = int(input("Day"))
month = int(input("Month"))
year = datetime.today().year
dop = int(year)
birthday = date(dop + 1, month, day)
between = birthday - today
print("Days till birthday: " + str(between))
