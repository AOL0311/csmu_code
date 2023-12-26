a = 1
b = 2
c = 3
print(f"A0={a}, B0={b}, C0={c}")
c = b
b = a
print(f"A1={a}, B1={b}, C1={c}")
b = b + 1
a = a * 2
print(f"A2={a}, B2={b}, C2={c}")