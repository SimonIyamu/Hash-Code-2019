import Read
import classes


def getTagDict(PhotosDict):
    tagDict = {}
    for photo in PhotosDict.dic.keys():
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
    bestPhoto = None
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


def removePhoto(tagDict, vdict, pdict, photo):
    # print "REMOVE", photo
    for tag in photo.tags:
        # print tag, tagDict[tag]
        tagDict[tag].remove(photo)

    pdict.dlt(photo)
    if photo.orientation == "V":
        vdict.dlt(photo)


def FindinngVH(photo1, slide, tagDict):
    chosenphoto = None
    mymax = -float('Inf')
    for tag in slide.tags:
        for photo in tagDict[tag]:
            if photo.orientation == "V":
                temp_slide = classes.slide([photo1, photo], 21)
                sample = getScore(temp_slide, slide)
                if(sample > mymax):
                    mymax = sample
                    chosenphoto = photo
    return chosenphoto


"""

"""


def getSlideShow(tagDict, photo_dict, vdict):

    # Pick a random photo ( TODO better choice )

    it = photo_dict.dic.iterkeys()
    if vdict.count > 1:
        firstPhoto = next(it)
    else:
        while 1:
            photo = next(it)
            if photo.orientation == "H":
                firstPhoto = photo
                break

    usedPhotos = 1
    removePhoto(tagDict, vdict, photo_dict, firstPhoto)

    if firstPhoto.orientation == "H":
        slide = classes.slide([firstPhoto], 0)
    else:
        it = vdict.dic.iterkeys()
        secondPhoto = next(it)
        usedPhotos += 1
        slide = classes.slide([firstPhoto, secondPhoto], 0)
        removePhoto(tagDict, vdict, photo_dict, secondPhoto)

    slideShow = [slide]
    slideID = 1
    while photo_dict.count > 1:
        # print "slideShow=", slideShow
        bestPhoto = SlideComboScore(slide, tagDict)
        # print "bestPhoto is", bestPhoto

        if bestPhoto is None:
            it = photo_dict.dic.iterkeys()
            if vdict.count > 1:
                bestPhoto = next(it)
            else:
                while 1:
                    photo = next(it)
                    if photo.orientation == "H":
                        bestPhoto = photo
                        break
        removePhoto(tagDict, vdict, photo_dict, bestPhoto)

        if bestPhoto.orientation == "H":
            nextSlide = classes.slide([bestPhoto], slideID)
            usedPhotos += 1
        else:
            # The photo is vertical
            bestFit = FindinngVH(bestPhoto, slide, tagDict)
            if bestFit is None:
                it = vdict.dic.iterkeys()
                bestFit = next(it)
            nextSlide = classes.slide([bestPhoto, bestFit], slideID)
            removePhoto(tagDict, vdict, photo_dict, bestFit)
            usedPhotos += 2

        slideShow.append(nextSlide)
        print usedPhotos
        slideID += 1

        slide = nextSlide

    return slideShow
