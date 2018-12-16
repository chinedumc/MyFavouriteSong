
'''
Create a function that accepts 3 parameters and checks for 
equality between any two of them. 

Your function should return True if 2 or more of the parameters are equal, 
and false if none of them are equal to any of the others.
'''

# Initialize the 3 variables
a = 3
b = 3
c = 5

# The If statement:
if a == b or b == c or a == c:  # Checking that at least 2 of the 3 parameters are equal
    print ("True")

else:
    print("False")  # To be printed when none of the 3 parameters are equal

'''
Modifying the function so that strings can be compared to 
integers if they are equivalent.
'''
# Initialize the 3 variables
a = 3
b = "3"
c = 5

# The If statement:
if a == int(b) or int(b) == c or a == c:  # Checking that at least 2 of the 3 parameters are equal
    print ("True")

else:
    print("False")  # To be printed when none of the 3 parameters are equal
 
    
