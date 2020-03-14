# ask for the number of rows and print the triangle

rows = int(input("How many rows: "))
for i in range(rows):
    print(" "  * (rows - i - 1), "#" * (i * 2 + 1), sep = "")