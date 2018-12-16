#The SongTitle function:
 
Title = "Bad"  #The title of the song

def SongTitle(Title): #Definition of function
    print(Title)
    return SongTitle

SongTitle(Title)     #Function call

#The Artist function:

Singer = "Michael Jackson"

def Artist(Singer):  #Function definition
    print(Singer)
    return 

Artist(Singer)   #Function call

#The Release Year function:

ReleaseYear = "1987"

def YearReleased(ReleaseYear):
    print(ReleaseYear)
    return YearReleased

YearReleased(ReleaseYear)

#The Extra Function

Var1 = 3  #Declaraation of a Variable Var1

def ReturnBoo(Number):
    Number += 1
    print(Number)
    return (Var1 > Number)

check = ReturnBoo(5)  #Check how Var1 compares to Number using ReturnBoo function
print(check)
