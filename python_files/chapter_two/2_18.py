total_useage = 30 * 8

if total_useage % 40 == 0:
    print(f"Needs to wash {total_useage // 40} times.")
else:
    print(f"Needs to wash {total_useage // 40 + 1} times.")