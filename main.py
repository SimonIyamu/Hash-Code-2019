import functions
import Read

N,photo_list = Read.ReadInput("a_example.txt")
tagDict = functions.getTagDict(photo_list)

for tag in tagDict:
    print tag,
    for photo in tagDict[tag]:
        print photo.ID , ",",
    print ""

#print tagDict
