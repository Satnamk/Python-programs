# Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

# Ask the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the perimeter and area of the rectangle
perimeter = 2 * (length + width)
area = length * width

# Print out the results
print(f"The perimeter of the rectangle is: {perimeter}")
print(f"The area of the rectangle is: {area}")
