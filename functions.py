import Read
import classes


def getTagDict(Photos):
    tagDict = {}
    for photo in Photos:
        for tag in photo.tags:
            if tag in tagDict:
                x = tagDict[tag]
                x.append(photo)
                tagDict[tag] = x
                # tagDict[tag] = tagDict[tag].append(photo)
            else:
                tagDict[tag] = [photo]
    return tagDict

# calculate the score of BOTH pictures and slides


def getScore(Slide1, Slide2):
    list = []
    x = Slide1.tags.intersection(Slide2.tags)
    list.append(len(x))
    x = Slide1.tags.difference(Slide2.tags)
    list.append(len(x))
    x = Slide2.tags.difference(Slide1.tags)
    list.append(len(x))

    return min(list)


def SlideComboScore(slide, tagDict):
    max_score = -float('Inf')
    for tag in slide.tags:
        for photo in tagDict[tag]:
            combo_score = getScore(slide, photo)
            if combo_score > max_score:
                max_score = combo_score
                bestPhoto = photo
    return bestPhoto


"""
    removes a photo from the tag dictionary and maybe vertical list
"""

def removePhoto(tagDict, vlist, photo):
    for tag in photo.tags:
        tagDict[tag].remove(photo)

    if photo.orientation == "V":
        vlist.remove(photo)

    return (tagDict, vlist)


def FindinngVH(photo1, photo2, verticalphoto):
    mymax = 0
    myset = set()
    for photo in verticalphoto:
        myset.union(photo1.tags)
        myset.union(photo.tags)
        sample = getScore(myset, photo2)
        if(sample > mymax):
            mymax = sample
            chosenphoto = photo
    myset = set()
    return chosenphoto

"""

"""
def getSlideShow(tagDict,photo_list,vlist):
    
    # Pick a random horizontal ( TODO better choice )

    for photo in photo_list:
        if photo.orientation == "H":
            firstPhoto = photo
            break

    slide = classes.slide(firstPhoto,0)

    while something:
        

    #return slideShow
