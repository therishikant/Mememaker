import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

imagefile = 'E:/Animatedtimes/Meme Maker Automation/V2/temp/AT1.png'

memefile = 'abcd.png'

inputDir = 'E:/Animatedtimes/Meme Maker Automation/V2/input';


def showImage(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def readImage(filename):
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    return img


def resizeImage(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    size = (width, height)
    return cv2.resize(image, size)


def drawCircle(x, y, image):
    center_coordinates = (x, y)
    radius = 2
    color = (255, 0, 0)
    thickness = 2
    image = cv2.circle(image, center_coordinates, radius, color, thickness)


def getUsableDimensions(templateImage, offset):
    return (templateImage.shape[1] - 2 * offset, templateImage.shape[0] - 2 * offset)


def saveImage(imageName, image):
    cv2.imwrite(imageName, image)


def getScaleForImage(shape, usableDimensions):
    dWidth = abs(shape[0] - usableDimensions[0])
    dHeight = abs(shape[1] - usableDimensions[1])

    if dWidth < dHeight:
        return usableDimensions[0] / shape[0]
    return usableDimensions[1] / shape[1]


def putImageOnTemplate(image, template, offset, usableDimensions):
    x_off1 = 0
    x_off2 = 0
    y_off1 = 0
    y_off2 = 0
    if image.shape[0] != usableDimensions[0]:
        diff_x = abs(image.shape[0] - usableDimensions[0])
        x_off1 = diff_x // 2
        x_off2 = diff_x - x_off1
    else:
        diff_y = abs(image.shape[1] - usableDimensions[1])
        y_off1 = diff_y // 2
        y_off2 = diff_y - y_off1

    template[offset: offset + usableDimensions[0], offset: offset + usableDimensions[1]] = np.zeros(
        (usableDimensions[0], usableDimensions[1], template.shape[2]), np.uint8)
    template[offset + x_off1: offset + usableDimensions[0] - x_off2,
    offset + y_off1: offset + usableDimensions[1] - y_off2] = image
    return template


def addCredits(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 2
    color = (255, 255, 255)
    thickness = 2
    return cv2.putText(image, text, org, font,
                       fontScale, color, thickness, cv2.LINE_AA)


def saveFinal(memeFile, fileName):
    os.chdir('E:/Animatedtimes/Meme Maker Automation/V2/output')
    saveImage(fileName + "_final.jpg", addCredits(memeFile, ""))


def makeMeme(memefile):
    print(memefile)
    start = 90
    templateImage = readImage(imagefile)
    memeImage = readImage(memefile)
    print(templateImage.shape, memeImage.shape)
    usableDimensions = getUsableDimensions(templateImage, start)
    # scale = getScaleForImage(memeImage.shape, usableDimensions)
    scale = getScaleForImage(usableDimensions, memeImage.shape)
    print(scale)

    # scaledImage = resizeImage(memeImage, getScaleForImage(memeImage.shape, usableDimensions))
    # print(usableDimensions, scaledImage.shape, templateImage.shape)
    # finalImage = putImageOnTemplate(scaledImage, templateImage, start, usableDimensions)
    # drawCircle(start, start, templateImage)

    templateImage = resizeImage(templateImage, scale)
    start = int(start*scale)
    usableDimensionsX = int(usableDimensions[0] * scale)
    usableDimensionsY = int(usableDimensions[1] * scale)

    print(usableDimensionsX)
    print(usableDimensionsY)

    usableDimensions = (usableDimensionsX, usableDimensionsY)


    print(usableDimensions, memeImage.shape, templateImage.shape)
    finalImage = putImageOnTemplate(memeImage, templateImage, start, usableDimensions)

    saveFinal(finalImage, memefile)


def loadImages():
    os.chdir(inputDir)
    listDir = os.listdir()
    for i in range(len(listDir)):
        os.chdir(inputDir)
        memefile = listDir[i]
        makeMeme(memefile)


loadImages()

