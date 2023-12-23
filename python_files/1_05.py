# 請印出三角形，如下方範例輸出。

# print("       *")
# print("      * *")
# print("     *   *")
# print("    *     *")
# print("   *       *")
# print("  *         *")
# print(" *           *")
# print("***************")

# 設定三角形的高度
triangle_height = 8

# 迴圈印出三角形的每一行
for i in range(triangle_height - 1):
    spaces = " " * (triangle_height - i - 1)
    if i == 0:
        stars = "*"
    else:
        stars = "*" + " " * (2 * i - 1) + "*"
    print(spaces + stars)

# 最後一行印出橫線
print("*" * (2 * triangle_height - 1))
