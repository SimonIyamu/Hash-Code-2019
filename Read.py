import classes


def ReadInput(filename):
    FileDesc = open(filename, "r")
    lines = [line.rstrip('\n').split(' ') for line in FileDesc]

    photo_list = []

    N = int(lines[0][0])
    del lines[0]
    for j, line in enumerate(lines):
        temp_list = []
        orientation = line[0]
        for i in range(2, len(line)):
            temp_list.append(line[i])

        photo_list.append(classes.picture(j, temp_list, orientation))

    return (N, photo_list)


print ReadInput("a_example.txt")
