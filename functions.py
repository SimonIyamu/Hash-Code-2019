import Read

def getTagDict(Photos):
    tagDict = {}
    for photo in Photos:
        for tag in photo.tags:
            if tag in tagDict:
                x = tagDict[tag]
                x.append(photo)
                tagDict[tag]= x
                #tagDict[tag] = tagDict[tag].append(photo)
            else:
                tagDict[tag]=[photo]
    return tagDict
