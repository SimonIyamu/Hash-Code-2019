import functions
import Output
import Read

for i in range(5):
    if i == 0:
        N, photo_list, vertical_list = Read.ReadInput("a_example.txt")
    elif i == 1:
        continue
        N, photo_list, vertical_list = Read.ReadInput(
            "b_lovely_landscapes.txt")
    elif i == 2:
        N, photo_list, vertical_list = Read.ReadInput(
            "c_memorable_moments.txt")
    elif i == 3:
        continue
        N, photo_list, vertical_list = Read.ReadInput("d_pet_pictures.txt")
    elif i == 4:
        N, photo_list, vertical_list = Read.ReadInput("e_shiny_selfies.txt")

    tagDict = functions.getTagDict(photo_list)

    slideShow = functions.getSlideShow(tagDict, photo_list, vertical_list)

    filename = "output"+str(i)+".txt"
    print filename
    Output.Outputit(filename, slideShow)
