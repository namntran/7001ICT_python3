# ask for the number of rows and print the triangle

rows = int(input("How many rows: "))
hashes = 1
for i in range(rows):
    spaces = rows - i - 1
    print(" "  * spaces, "#" * hashes, sep = "")
    hashes += 2
    #variable how many hashes to print, and change every time