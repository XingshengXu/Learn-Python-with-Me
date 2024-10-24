from datetime import datetime
import pytz

# 当前时间加上时区
now_utc = datetime.now(pytz.utc)
print("UTC 当前时间:", now_utc)

# 转换到其他时区
now_est = now_utc.astimezone(pytz.timezone('US/Eastern'))
print("美国东部时间:", now_est)

# now_shanghai = now_utc.astimezone(pytz.timezone('Asia/Shanghai'))
# print("上海时间:", now_shanghai)

# now_london = now_utc.astimezone(pytz.timezone('Europe/London'))
# print("伦敦时间:", now_london)
