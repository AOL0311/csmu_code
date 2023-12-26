DBP = int(input("Enter your DBP:"))

SBP = DBP * 1.5

MAP = DBP + (SBP - DBP) / 3

print(f"MAP = {MAP:.2f}")