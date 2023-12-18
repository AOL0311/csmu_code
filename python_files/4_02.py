# 一路領到爆銀行年複利 12%，小明存入本金 10000 元，儲蓄五年可拿到多少金
# 額？顯示每年之利息與本利和，最後總結五年可拿到多少？
# 此外，若每年疊加的本金以及本利和超過本金的 150%後，這份合約便會宣告終
# 止，請計算出在經過多少時間後此份合約會宣告終止。
# 複利公式：S=P(1+𝑖)^𝑛
# P 代表本金，n 代表時期，i 代表利率，S 代表本利和。

origin = 10000
annual_rate = 0.12
years = 5
limit = 1.5

total_amount = origin
year_count = 0
rate = 1
all_time_total = 0

while year_count < years and total_amount <= origin * limit:
    year_count += 1
    interest = total_amount * annual_rate
    total_amount *= (1 + annual_rate)
    rate *= (1 + annual_rate)
    all_time_total += total_amount
    print(f"第{year_count}年 利率:{rate:.2f} 本利和:{total_amount:.2f}")

print(f"==> 儲蓄{year_count}年之本利和 = {all_time_total:.2f}")