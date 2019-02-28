class picture:
    def __init__(self, ID, tags, Orientation, Notags):
        self.ID = ID
        self.tags = tags
        self.orientation = Orientation
        self.tagsNo = Notags


class slide:
    def __init__(self, Pictures, id):
        self.tags = set()
        if(len(Pictures) == 2):
            self.type = "V"
        else:
            self.type = "H"
        self.picids = []
        for Picture in Pictures:
            self.picids.append(Picture.ID)
            for tag in Picture:
                self.tags.add(tag)

        self.id = id
