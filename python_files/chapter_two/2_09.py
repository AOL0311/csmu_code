for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(f"{i}*{j}= {i*j}", end=" ")
        else:
            print(f"{i}*{j}={i*j}", end=" ")
    print(end="\n")