import math

num_one, num_two, num_three = map(int, input().split(" "))

num_one = math.sqrt(num_one) * 10
num_two = math.sqrt(num_two) * 10
num_three = math.sqrt(num_three) * 10

print(f"{(num_one + num_two + num_three) / 3:.2f}")