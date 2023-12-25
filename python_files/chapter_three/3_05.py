time = int(input())

if 0 <= time <= 720:
    if time < 30:
        money = 0
        print(money)
    else:
        less_than_fifteen = time % 30
        time = time // 30
        if 0 < less_than_fifteen:
            time += 1
        money = time * 15
        if 240 < money:
            print("240")
        else:
            print(money)
else:
    print("Please enter legal data.")