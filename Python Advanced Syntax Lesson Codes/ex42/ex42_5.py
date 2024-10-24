from datetime import datetime

now = datetime.today()

# 转化datetime对象为字符串
date_string = now.strftime("%Y/%m/%d %H:%M:%S")
print("格式化的日期和时间:", date_string)

# 将字符串解析为datetime对象
# date_string = "October 24, 2024 18:30:00"
# parsed_date = datetime.strptime(date_string, "%B %d, %Y %H:%M:%S")
# print("解析后的日期时间对象:", parsed_date)
