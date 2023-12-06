python
import calendar  
  
def print_calendar(year, month):  
    print(calendar.month(year, month))  
  
year = int(input("请输入年份: "))  
month = int(input("请输入月份: "))  
print_calendar(year, month)
