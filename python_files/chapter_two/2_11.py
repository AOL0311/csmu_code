walk_time = 3 * 60
black_tea = 1 * 60
milk_green = 2 * 60
add_pearl = 12

total_time = 5 * (black_tea + add_pearl) + 2 * black_tea + 2 * (milk_green + add_pearl) + 2 * walk_time

print(f"{total_time / 60:.2f}")