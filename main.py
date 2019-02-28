import functions
import Read

for i in range(5):
    if i == 0:
        N, photo_list, vertical_list = Read.ReadInput("a_example.txt")
    elif i == 1:
        N, photo_list, vertical_list = Read.ReadInput(
            "b_lovely_landscapes.txt")
    elif i == 2:
        N, photo_list, vertical_list = Read.ReadInput(
            "c_memorable_moments.txt")
    elif i == 3:
        N, photo_list, vertical_list = Read.ReadInput("d_pet_pictures.txt")
    elif i == 4:
        N, photo_list, vertical_list = Read.ReadInput("e_shiny_selfies.txt")

    tagDict = functions.getTagDict(photo_list)
    scores = functions.PicComboScore(tagDict, photo_list)

    # for tag in tagDict:
    #     print tag,
    #     for photo in tagDict[tag]:
    #         print photo.ID, ",",
    #     print ""

    print(len(tagDict))
    print "output"+str(i)+".txt"
    #print tagDict
