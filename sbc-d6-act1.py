emptyList = []# Initialize an empty list

userInput = input("Enter the word: ")#Take input in the user 

# Generate the reversed version of the userInput, remove spaces, converted into lowercase
palindrome = "".join(reversed(userInput.replace(" ","").lower()))

# Store the cleaned and lowercase version of the userInput input in the list
characterReplace = userInput.replace(" ","").lower() 

emptyList.append(characterReplace)
# Iterate through the list (although it only has one element)

for char in emptyList:
    if char == palindrome:
       print(f" '{userInput}'. Is a Palindrome" ) # If the cleaned input is equal to its reversed version, print it's a palindrome
    # If not, print the original input and its reversed version, stating it's not a palindrome

    else:
       print(f"""The reversed version of '{userInput}' is '{palindrome}', And it is not a palindrome.""")