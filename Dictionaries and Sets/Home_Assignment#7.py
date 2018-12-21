"""
A program that takes the features of my favourite song into a dictionary 
And then uses one print statement to print out the property of each feature in a 
key-value pair.
"""

# Define the dictionary using features from My Faourite Song
FavSongDict = {"SongTitle" : "Bad", 
               "Artist" : "Michael Jackson",
               "YearReleased":"1987",
               "AlbumTitle" : "Bad",
               "Genre" : "Pop",
               "DurationInSeconds" : "246",
               "SalesCert" : "Platinum",
               "RecordLabel" : "Epic",
               "Producer" : "Quincy Jones",
               "CoProducer" : "Michael Jackson",
               "SongWriter" : "Michael Jackson"}

for feature in FavSongDict:
    print(feature + " = " + FavSongDict[feature]) #Print each feature and it's value
    
    
'''
A function to checkthe Key-Value pair entered for a Feature and its corresponding 
value in the FavSongDict dictionary of My FavouriteSong.
When the Key and Value are correct, True is returned. But when any 
wrong Key or Value is entered, the output False is printed to the screen
'''
Enter_FeatureValue = FavSongDict[feature]

def checkFeature(feature, Enter_FeatureValue):
    if (Enter_FeatureValue) == (FavSongDict[feature]):
        print(True)
    else:
        print(False)   
    
checkFeature("SalesCert", "Platinum") #Output is True
checkFeature("CoProducer", "Chinedum") #Output is False
