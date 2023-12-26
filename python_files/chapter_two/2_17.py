money = int(input())

exchange_ten = money // 10
money %= 10
exchange_five = money // 5
exchange_one = money % 5

print(f"Can exchange {exchange_ten} ten dollar coins.")
print(f"Can exchange {exchange_five} five dollar coins.")
print(f"Can exchange {exchange_one} one dollar coins.")