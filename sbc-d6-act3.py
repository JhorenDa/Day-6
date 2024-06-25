ROWS = int(input("Enter the number of rows for the Pyramid: "))

# Loop to print the top part of the pyramid
for stars in range(ROWS, 1, -1):
    print("*" * stars)  # Print a row with 'stars' number of asterisks

# Print the middle row with one asterisk at the beginning and end, and spaces in between
if ROWS > 1:
    print("*" + " " * (ROWS - 2) + "*")

# Loop to print the bottom part of the pyramid
for moons in range(2, ROWS + 1):
    print("*" * moons)  # Print a row with 'moons' number of asterisks



#------------------------------------------------------------------------------------------------------------------

          
