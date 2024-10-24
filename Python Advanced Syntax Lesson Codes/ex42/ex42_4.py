from datetime import datetime, timedelta

# 创建时间差对象
delta = timedelta(days=5, hours=3)
print("时间间隔:", delta)

# 日期加减操作
now = datetime.now()
future = now + delta
past = now - delta

print("当前时间:", now)
print("未来时间:", future)
print("过去时间:", past)
