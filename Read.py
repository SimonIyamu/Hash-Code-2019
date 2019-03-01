import classes
import util


def ReadInput(filename):
    FileDesc = open(filename, "r")
    lines = [line.rstrip('\n').split(' ') for line in FileDesc]

    photo_dict = util.EnhDictionary()
    verticalphoto = util.EnhDictionary()
    N = int(lines[0][0])
    del lines[0]
    for j, line in enumerate(lines):
        temp_list = set()
        orientation = line[0]
        length = int(line[1])
        # if(orientation == "V"):
        # verticalphoto.append(j)
        for i in range(2, len(line)):
            temp_list.add(line[i])
            x = classes.picture(j, temp_list, orientation, length)
        photo_dict.add(x, length)
        if(orientation == "V"):
            verticalphoto.add(x, length)

    return (N, photo_dict, verticalphoto)


#print ReadInput("a_example.txt")
