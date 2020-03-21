# marks.py
# indefinite loops
# read marks until negative numbers
n = 0
total = 0.0
mark = float(input("Enter a mark: "))
while mark >= 0.0:
    n += 1
    total += mark
    mark = float(input("Enter a mark: "))
print("The number of marks: ", n)
if n > 0:
    print("The average mark is: ", total/ n)