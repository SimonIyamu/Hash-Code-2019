import classes


def Outputit(filename, Slides):
    FileDesc = open(filename, "w+")

    for Slide in Slides:
        # create the string of photo IDS
        string = ""
        for id in Slide.picids:
            string += id + " "

        FileDesc.write(string)
