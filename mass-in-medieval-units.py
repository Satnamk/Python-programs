# Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti). The program converts
# the input to full kilograms and grams and outputs the result to the user:
#

# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

# Conversion constants
LOT_TO_GRAMS = 13.3
POUND_TO_LOTS = 32
TALENT_TO_POUNDS = 20

# Ask the user for the mass in talents, pounds, and lots
talents = int(input("Enter the number of talents (leiviskä): "))
pounds = int(input("Enter the number of pounds (naula): "))
lots = float(input("Enter the number of lots (luoti): "))

# Convert the entire mass to grams
total_grams = (talents * TALENT_TO_POUNDS * POUND_TO_LOTS * LOT_TO_GRAMS) + \
              (pounds * POUND_TO_LOTS * LOT_TO_GRAMS) + \
              (lots * LOT_TO_GRAMS)

# Convert grams to kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Print out the result
print(f"The total mass is {kilograms} kilograms and {grams:.2f} grams.")
