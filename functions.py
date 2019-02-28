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
                #tagDict[tag] = tagDict[tag].append(photo)
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

def PicComboScore(tagDict, photo_list):
    score = {}
    for tag in tagDict.keys():
        for i in range(len(tagDict[tag])):
            for j in range(i+1, len(tagDict[tag])):
                pi = photo_list[i]
                pj = photo_list[j]
                if frozenset({pi, pj}) not in score:
                    score[frozenset({pi, pj})] = getScore(pi, pj)
    return score


"""
    removes a photo from the tag dictionary and maybe vertical list
"""


def removePhoto(tagDict, vlist, photo):
    for tag in photo.tags:
        tagDict[tag].remove(photo)

    if photo.orientation == "V":
        vlist.remove(photo)

    return (tagDict,vlist)

 def FindinngVH(photo1,photo2,verticalphoto):
     mymax=0
     myset=set()
     for photo in verticalphoto:
         myset.join(photo1.tags)
         myset.join(photo.tags)
         sample=getScore(myset,photo2)
         if(sample>mymax):
             mymax=sample
             chosenphoto=photo
        myset=set()
    return chosenphoto
