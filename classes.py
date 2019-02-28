class picture:
    def  __init__(self, ID , tags , Orientation):
        self.ID = []
        self.tags = tags
        self.orientation = Orientation
        self.tagsNo=len(tags)
class slide:
    def __init__(self ,Pictures,id ):
        self.tags=[]
        if(len(Pictures)==2):
            self.type="V"
        else:
            self.type="H"
        for Picture in Pictures:
            for tag in Picture:
                self.tags.append(tag)
        self.id=id        
