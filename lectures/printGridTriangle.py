# ask for the number of rows and print the triangle

rows = int(input("How many rows: "))
hashes = 1
for i in range(rows):
    spaces = rows - i - 1
    for j in range(spaces):
        print(" ", end = "")
    print("#" * hashes)

    hashes += 2
    #variable how many hashes to print, and change every time