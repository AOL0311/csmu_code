height = float(input("Height:"))
weight = float(input("Weight:"))

BMI = weight / (height / 100) ** 2

if BMI < 18.500000:
    print(f"{BMI:.6f} Too light")

elif 18.500000 <= BMI < 24.000000:
    print(f"{BMI:.6f} Medium")

elif 24.000000 <= BMI < 27.000000:
    print(f"{BMI:.6f} Heavy")

elif 27.000000 <= BMI < 30.000000:
    print(f"{BMI:.6f} Little fat")

elif 30.000000 <= BMI < 35.000000:
    print(f"{BMI:.6f} Medium fat")

else:
    print(f"{BMI:.6f} Too fat")