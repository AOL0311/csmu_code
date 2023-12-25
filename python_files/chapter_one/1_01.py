# 汽油一公升 23.7元，輸入欲加的公升數，計算其所需金額，並輸出到小數第一
# 位。

gas = input()

money = float(gas) * 23.7

print(f"{money:.1f}")