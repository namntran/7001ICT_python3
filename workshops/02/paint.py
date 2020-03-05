# estimate paint needed for rectangular wall. 
# litres per square metre is 0.3 litres

width = float(input("Enter the width of the wall in metres: "))
height = float(input("Enter the height of the wall in metres: "))
rate  = float(input("Litres per square metres: "))

print("Width of wall (m): ", width)
print("Height of wall (m): ", height)
print("Litres per square metre: ",rate)
# print the total litres required
print("Litres required = ", width*height*rate)