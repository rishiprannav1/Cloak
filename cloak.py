print("1- 12 hours clock")
print("2- 24 hours clock")
time=int(input("Enter your choice : "))

if time==1:
    print("You have selected 12 hours clock")
elif time==2:
    print("You have selected 24 hours clock")
else:
    print("Invalid choice")
min=int(input("Enter minutes : "))
hour=int(input("Enter hours : "))
if time==1:
    if hour>12 or hour<1:
        print("Invalid hour for 12 hours clock")
    elif min>59 or min<0:
        print("Invalid minutes")
    else:
        print(f"Time is {hour}:{min} {'AM' if hour<12 else 'PM'}")
elif time==2:
    if hour>23 or hour<01:
        print("Invalid hour for 24 hours clock")
    elif min>59 or min<0:
        print("Invalid minutes")
    else:
        print(f"Time is {hour}:{min}")
else:
    print("Invalid choice")
