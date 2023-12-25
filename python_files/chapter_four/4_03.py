# 某零件進口商的驗收退貨制度如下表
# 進口數<=5000
# 狀況    瑕疵品<=2%   2%<瑕疵品<=5%   瑕疵品>5%
# 退貨數   0           瑕疵品          全數退貨
# 進口數>5000
# 狀況    瑕疵品<=3%   3%<瑕疵品<=6%   瑕疵品>6%
# 退貨數   0           瑕疵品          全數退貨
# 例一：進口 4000 個零件，瑕疵品有 400 個，佔比例 10%，所以退貨數為 4000個。
# 例二：進口 6000 個零件，瑕疵品有 200 個，佔比例 3.33%，所以退貨數為 200個。
# 輸入值：第一個數字是進口數，第二個數字是瑕疵數
# 輸出值：退貨數

import_quantity, defective_quantity = map(int, input().split(" "))
defective_rate = float(defective_quantity / import_quantity * 100)

if import_quantity <= 5000:
    if defective_rate <= 2:
        return_quantity = 0
    elif 2 < defective_rate <= 5:
        return_quantity = defective_quantity
    else:
        return_quantity = import_quantity

else:
    if defective_rate <= 3:
        return_quantity = 0
    elif 3 < defective_rate <= 6:
        return_quantity = defective_quantity
    else:
        return_quantity = import_quantity

print(f"退貨數為 {return_quantity} 個")