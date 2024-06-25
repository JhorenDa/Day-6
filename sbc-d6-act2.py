# Ask for numbers of columns and rows to display
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
# Initialize a variable to track the current row (stars)
asterisk = 0
# Outer loop to iterate over each row
while asterisk < rows:
    circle = 0 # Initialize a variable to track the current column (moon)
    while circle < columns:
        # Inner loop to iterate over each column within the current row
        if asterisk == 0 or asterisk == rows -1 or circle == 0 or circle == columns -1:
            print("*", end="")# Print '*' if the current position is on the border
        else:
            print(" ", end="")# Print ' ' (space) if the current position is inside the border
        circle += 1  # Increment the column counter
    print() # Move to the next line after printing all columns for the current row
    asterisk += 1 # Increment the row counter
   
       
