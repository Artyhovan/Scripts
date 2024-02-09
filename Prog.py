import os
import time
current_time = time.time()
current_time_year = time.strftime("%Y")
current_time_month = time.strftime("%m")
current_time_day =time.strftime("%d.%m.%Y")
if current_time_month=="01":
    current_time_month = "01_Январь"
elif current_time_month=="02":
    current_time_month = "02_Февраль"
elif current_time_month=="03":
    current_time_month = "03_Март"
elif current_time_month=="04":
    current_time_month = "04_Апрель"
elif current_time_month == "05":
    current_time_month = "05_Май"
elif current_time_month=="06":
    current_time_month = "06_Июнь"
elif current_time_month=="07":
    current_time_month = "07_Июль"
elif current_time_month=="08":
    current_time_month = "08_Август"
elif current_time_month == "09":
    current_time_month = "09_Сентябрь"
elif current_time_month=="10":
    current_time_month = "10_Октябрь"
elif current_time_month=="11":
    current_time_month = "11_Ноябрь"
elif current_time_month=="12":
    current_time_month = "12_Декабрь"
print (current_time_year)
print (current_time_month)
print (current_time_day)
path = "D:\\На участок\\"+current_time_year+"\\"+current_time_month+"\\"+current_time_day

try:
    os.makedirs(path)
except: FileExistsError




