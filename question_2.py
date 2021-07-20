from collections import defaultdict
from datetime import time, timedelta, date, datetime

a = [2, 0, 1, 3, -1, -5]
# find triplets with sum zero
# constraint_1:  unique elements in array
# [[-5, 2, 3],[-1, 0, 1]]
out = []
q = set(a)
for x in range(len(a)):
    for y in range(x + 1, len(a)):
        possible = -(a[x] + a[y])
        if possible in q and possible != a[x] and possible != a[y] and sorted([possible, a[x], a[y]]) not in out:
            out.append(sorted([possible, a[x], a[y]]))
print(out)

# Candidate says that he is available from 10AM - 11:AM, Generate possible slots in the multiples of 15 mins
# [10 - 10:15, 10:15 - 10:30, 10 - 10:30, 10 - 11, 10:45 - 11, 10:15 - 11]
# Find the similar case for 11 AM - 1 PM
# 180 min, 0,15, 30, ...165

durations = [15, 30, 45, 60]
out = defaultdict(list)  # duration: [start_time1, start_time_2, ..]

start_time = datetime.combine(date.today(), time(hour=10, minute=00))
end_time = datetime.combine(date.today(), time(hour=13, minute=00))
max_limit = int((end_time - start_time).total_seconds()/60)
# max_limit = 180
for x in range(0, max_limit, 15):  # 15, 30 45 60 75
    for duration in durations:
        if x + duration <= max_limit:
            out[duration].append(x)

for x in out:
    for y in out[x]:
        print((start_time + timedelta(minutes=y)).time(), "-",
              (start_time + timedelta(minutes=y) + timedelta(minutes=x)).time())

# from 10:00 to 11:00 possible cases
# 15: [0, 15, 30, 45]  # (10:00 - 10:15, 10:15- 10:30, 10:30 - 10:45, 10:45 - 11:00 )
# 30: [0, 15, 30]  # (10:00 - 10:30, 10:15 - 10:45, 10:30 - 11:00)
# 45: [0, 15]  # (10:00 - 10:45 , 10:15 - 11:00 )
# 60: [0](10:00 - 11: 00 )
#
# 10:00 + ans + duration(15)
