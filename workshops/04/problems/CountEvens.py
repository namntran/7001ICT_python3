# CountEvens.py
# program that reads whole numbers typed by user until a negative number
# print the number of even numbers entered
even_count = 0
odd_count = 0

i = int(input("Enter a number: "))
while i >= 0:
    i += 1
    i = int(input("Enter a number: "))
    # checking condition 
    if i % 2 == 0: 
        even_count += 1
    else:
        odd_count += 1  
print(even_count, "even numbers were entered |", odd_count, "odd numbers were entered")
