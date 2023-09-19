##Date:28-06-2023

from datetime import datetime

check_in = input("Enter Check_intimes in HH:MM\n").split()

for time in check_in:
     hour, min = [int(i) for i in time.split(":")]
     print(hour, "hours and", min, "minutes")
     hours = hour + 12
     print(hours)
        

check_out = input("Enter Check_out times in HH:MM\n").split()

for time in check_out:
     hour, min = [int(i) for i in time.split(":")]
     print(hour, "hours and", min, "minutes")

