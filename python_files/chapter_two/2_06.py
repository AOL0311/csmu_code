num = 10
multiple_sum = 1

while num > 0:
    multiple_sum *= num
    num -= 1

print(f"10!={multiple_sum}")