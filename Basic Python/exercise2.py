#exercise 2 : Greeting according to time 
import time
timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp>=6 and timestamp<12):
    print("Good Morning")
elif(timestamp>12 and timestamp<18):
    print("Good Afternoon")
elif(timestamp>18 and timestamp<23):
    print("Good Evening")
else:
    print("Good Night")