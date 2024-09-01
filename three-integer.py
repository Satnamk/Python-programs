# Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

# Ask the user for three integer numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate the sum, product, and average of the numbers
sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3

# Print out the results
print(f"The sum of the numbers is: {sum_of_numbers}")
print(f"The product of the numbers is: {product_of_numbers}")
print(f"The average of the numbers is: {average_of_numbers}")
