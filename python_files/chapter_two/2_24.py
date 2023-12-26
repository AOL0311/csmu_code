stairs = 23
escalator = 15
elavator = 7

floor = int(input())

first_person = (floor - 1) * stairs
second_person = (floor - 1) * escalator + 20
third_person = (floor - 1) * elavator + 45

print(f"{first_person} seconds   {second_person} seconds   {third_person} seconds")
