# input MM/DD/YYYY
# Sunday:0 ... Saturday:6

# 4/4, 6/6, 8/8, 10/10, 12/12
# 7/11, 11/7, 5/9, 9/5
# 3/14, 1/3-4, 2/28-29

doom = {
    1:3,
    2:28,
    3:14,
    4:4,
    5:9,
    6:6,
    7:11,
    8:8,
    9:5,
    10:10,
    11:7,
    12:12
}

theDay = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

i = input()
month = int(i[0:2])
day = int(i[3:5])
year = int(i[6:10])

ytd = year%100
doomsyear = (year-year%100)/100


if (((year % 4 == 0) and (not year%100 == 0)) or (year % 400 == 0)):
    isLeapYear = True
else:
    isLeapYear = False

if (doomsyear % 4 == 0):
    doomsday = 2
elif (doomsyear % 4 == 1):
    doomsday = 0
elif (doomsyear % 4 == 2):
    doomsday = 5
elif (doomsyear % 4 == 3):
    doomsday = 3

doomsday += ytd + (ytd-(ytd%4))/4
doomsday %= 7


ans = doomsday - (((doom[month] > day)*2)-1)*abs(doom[month]+((month in [1,2])*isLeapYear)-day)%7
if(ans<0):
    ans +=7
    
print(theDay[ans])