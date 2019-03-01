import functions
import Output
import Read

for i in range(3):
    if i == 0:
        N, photo_dict, vertical_dict = Read.ReadInput("a_example.txt")
    elif i == 1:
        N, photo_dict, vertical_dict = Read.ReadInput(
            "b_lovely_landscapes.txt")
    elif i == 2:
        N, photo_dict, vertical_dict = Read.ReadInput(
            "c_memorable_moments.txt")
    elif i == 3:
        continue
        N, photo_dict, vertical_dict = Read.ReadInput("d_pet_pictures.txt")
    elif i == 4:
        N, photo_dict, vertical_dict = Read.ReadInput("e_shiny_selfies.txt")

    tagDict = functions.getTagDict(photo_dict)

    slideShow = functions.getSlideShow(tagDict, photo_dict, vertical_dict)

    filename = "output"+str(i)+".txt"
    print filename
    Output.Outputit(filename, slideShow)
