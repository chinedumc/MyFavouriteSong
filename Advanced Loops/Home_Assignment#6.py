'''
A program to print out the following pattern shown below: 
 | | 
-----
 | | 
-----
 | |  
'''

for row in range(1,6): # Defining our pattern to have 5 rows
    if row%2 !=0:    
        for column in range(5): # Defining our pattern to have 5 columns
           
            if column%2 ==0:    # To ensure we get the " " and "|" in the odd rows 
                if column < 4:  # To ensure we do not get new lines from the print function for all columns in the odd rows:
                    print(" ", end = "")
                else:
                    print(" ")
                
            else:
                print("|", end = "")
            
    else:
        print("-----") 
print("True")
