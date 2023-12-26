money, year = map(int, input().split(" "))

if year == 1:
    print(f"{money * 0.0063 * 12 * year + money:.6f}")
elif year == 2:
    print(f"{money * 0.0066 * 12 * year + money:.6f}")
elif year == 3:
    print(f"{money * 0.0069 * 12 * year + money:.6f}")
elif year == 5:
    print(f"{money * 0.0075 * 12 * year + money:.6f}")
elif year == 8:
    print(f"{money * 0.0084 * 12 * year + money:.6f}")
else:
    print("error")