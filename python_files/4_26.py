a, b = map(int, input().split(" "))

has_automorphic_number = False

if 0 < a < b < 10000:
    for num in range(a, b + 1):
        square = num ** 2
        num_string = str(num)
        square_string = str(square)[-len(num_string):]

        if num_string == square_string:
            has_automorphic_number = True
            break

    if has_automorphic_number:
        print("Yes")

    else:
        print("No")

else:
    print("Requirement: 0 < a < b < 10000")
    continue