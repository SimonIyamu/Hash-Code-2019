import classes


def Outputit(filename, Slides):
    FileDesc = open(filename, "w+")

    FileDesc.write(str(len(Slides))+"\n")
    for Slide in Slides:
        # create the string of photo IDS
        string = ""
        for id in Slide.picids:
            string += str(id) + " "
        string += "\n"

        FileDesc.write(string)
