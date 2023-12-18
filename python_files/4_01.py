# 請輸入三個分數，調整為原分數開根號乘以十為新分數，並算出其平均值(平均
# 值顯示到小數第二位)，並判斷及格與否(及格為 60 分整)

import math as mt

score_one, score_two, score_three = map(float, input().split(" "))

new_score_one = mt.sqrt(score_one) * 10
new_score_two = mt.sqrt(score_two) * 10
new_score_three = mt.sqrt(score_three) * 10

average_score = (new_score_one + new_score_two + new_score_three) / 3

if average_score >= 60:
    print(f"{average_score:.2f} 及格")
else:
    print(f"{average_score:.2f} 不及格")