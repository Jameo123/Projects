# decimal input from user
userInput = int(input("Enter decimal number: "))
# declaring string variable for later
result = ""
# assigning new variable to userInput
quota = userInput
# creating while loop that terminates when 0 is greater than quota
while quota > 0:
    # finds the remainder for each individual operation of quota
    remainder = quota % 2
    # floor divides quota by 2 and saves the result for next operation
    quota //= 2
    # combines each remainder one by one into the varuable result
    result += str(remainder)
# printing result using original input and result printed backwards for binary formation
print(f"Decimal {userInput} equals {result[::-1]} in Binary")