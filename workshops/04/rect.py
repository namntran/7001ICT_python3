#rect.py
#print a rectangle of #
row = int(input("Enter rows: "))
col = int(input("Enter columns: "))
for j in range(row):
    for i in range(col):
        print("#", end = "")
    print()