import classes


def ReadInput(filename):
    FileDesc = open(filename, "r")
    lines = [line.rstrip('\n').split(' ') for line in FileDesc]

    photo_list = []

    N = int(lines[0][0])
    del lines[0]
    for j, line in enumerate(lines):
        temp_list = set()
        orientation = line[0]
        length = int(line[1])
        for i in range(2, len(line)):
            temp_list.add(line[i])

        photo_list.append(classes.picture(j, temp_list, orientation, length))

    return (N, photo_list)


print ReadInput("a_example.txt")
