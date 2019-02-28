import classes


def ReadInput(filename):
    FileDesc = open(filename, "r")
    lines = [line.rstrip('\n').split(' ') for line in FileDesc]

    photo_list = []
    verticalphoto = []
    N = int(lines[0][0])
    del lines[0]
    for j, line in enumerate(lines):
        temp_list = set()
        orientation = line[0]
        length = int(line[1])
        if(orientation == "V"):
            verticalphoto.append(j)
        for i in range(2, len(line)):
            temp_list.add(line[i])
            x = classes.picture(j, temp_list, orientation, length)
        photo_list.append(x)
        if(orientation == "V"):
            verticalphoto.append(x)

    return (N, photo_list, verticalphoto)


#print ReadInput("a_example.txt")
