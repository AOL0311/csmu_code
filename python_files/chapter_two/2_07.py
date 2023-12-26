year = int(input())

if year % 100 != 0 and year % 4 == 0:
    print("It's a leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print("It's a leap year.")
else:
    print("Not a leap year.")