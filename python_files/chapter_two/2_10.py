num_one, num_two, num_three = map(float, input().split(" "))

fuction = ((num_two ** 2) - (4 * num_one * num_three)) / (2 * num_one)

print(f"{fuction:.2f}")