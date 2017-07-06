#open(name[,mode[,buffering]])
# f = open("test.txt",'w')
# f.write("hi i hate u")
# f.close()
# r = open("test.txt",'r')
# r.read()
# print r.read()
import datetime
import calendar

def add_months(days,months):
    month = days.month - 1 + months
    year = days.year + month / 12
    month = month % 12 + 1
    day = min(days.day, calendar.monthrange(year, month)[1])
    return days.replace(year=year, month=month, day=day)

def getBetween_TwoMonth(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m")
        date_list.append(date_str)
        begin_date = add_months(begin_date,1)
    return date_list
print getBetween_TwoMonth('2015-06-01','2015-07-01')
