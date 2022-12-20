def leap_year(year):
    if 0 == year % 4 and 0 != year % 400 or 0 == year % 400:
        return True
    else:
        return False


def get_month_days(year, month):
    days = 31
    if 2 == month:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif 4 == month or 6 == month or 9 == month or 11 == month:
        days = 30
    return days


def get_total_days(year, month):
    total_days = 0
    for i in range(1, year):
        if leap_year(year):
            total_days += 366
        else:
            total_days += 365
    for i in range(1, month):
        total_days += get_month_days(year, i)
    return total_days


_year_ = input("请输入年份：")
_month_ = input("请输入月份：")

print()
print("日\t一\t二\t三\t四\t五\t六")
print()

count = 0
y = int(_year_)
m = int(_month_)

for c in range(get_total_days(y, m) % 7):
    print(end="\t")
    count += 1

for day in range(1, get_month_days(y, m)+1):
    print(day, end="\t")
    count += 1
    if 0 == count % 7:
        print("\n")
