# marksTests.py
# prompt for the number of marks and read them
# print the number number of marks entered and the average (arithmetic mean) of the marks
# print out the highest and lowest marks

n = int(input("How many marks: "))
if n > 0:
    mark = float(input("Enter a mark: "))
    highestMark = mark
    lowestMark = mark
    total = mark
    for i in range(n-1):
        mark = float(input("Enter a mark: "))
        total += mark
        if mark > highestMark:
            highestMark = mark
        if mark < lowestMark:
            lowestMark = mark
    print("The number of marks: ", n)
    print("The average mark is: ", total/n)
    print("The lowest mark is: ", lowestMark)
    print("The highest mark is: ", highestMark) 

