# 讀入兩個數，並且顯示兩數相乘後的結果。

numOne, numTwo = map(float, input("輸入兩個數:").split(" "))

print(f"兩數相乘:{numOne * numTwo:.6f}")