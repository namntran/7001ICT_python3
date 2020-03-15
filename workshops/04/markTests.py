# marksTests.py
# prompt for and read marks of a test until a negative number is entered (which can not be a valid mark)
# print the number number of marks entered and the average (arithmetic mean) of the marks
# print out the highest and lowest marks

n = 0
total = 0.0
mark = float(input("Enter a mark: "))
highestMark = mark
lowestMark = mark
while mark >= 0.0:
    #body
    n += 1
    total += mark
    if mark > highestMark:
        highestMark = mark
    if mark < lowestMark:
        lowestMark = mark
    mark = float(input("Enter a mark: "))
print("The number of marks: ", n)
if n > 0:
    print("The average mark is: ", total/n)
    print("The lowest mark is: ", lowestMark)
    print("The highest mark is: ", highestMark) 