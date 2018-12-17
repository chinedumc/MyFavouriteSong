#Home Assignment#4: Lists

#Create a global variable called myUniqueList. It should be an empty list

myUniqueList = []



# A function to check if the Input is a member of myUniqueList
def AddToList(Input):
    if (Input not in myUniqueList):  #If the Input exists in myUniqueList, print False and do not append the Input variable
        print(True)
        myUniqueList.append(Input) # If the Input variable is not in myUniqueList, print True and append Input variable
        return myUniqueList
        
    
    else:
        print("False, the list already contains the element", Input)
        return myUniqueList
    

# Test codes
AddToList(50)
print(myUniqueList) #Print out the recent myUniqueList


AddToList(60)
print(myUniqueList)    #Print out the recent myUniqueList


AddToList(65)
print(myUniqueList)  #Print out the recent myUniqueList


AddToList(55)
print(myUniqueList)  #Print out the recent myUniqueList

AddToList(50)
print(myUniqueList)  #Print out the recent myUniqueList without appending 50 to myUniqueList

AddToList(50)
print(myUniqueList)  #Print out the recent myUniqueList without appending 50 to myUniqueList


AddToList(70)
print(myUniqueList)  #Print out the recent myUniqueList without appending 50 to myUniqueList
