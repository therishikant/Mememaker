import cv2
import numpy as np
import os
from PIL import Image, ImageFont, ImageDraw

FWimage = 'E:/Animatedtimes/Meme Maker Automation/V2/temp/FW.png'
ATimage = 'E:/Animatedtimes/Meme Maker Automation/V2/temp/AT.png'

memefile = 'abcd.png'

inputDir = 'E:/Animatedtimes/Meme Maker Automation/V2/input';

fontDir = 'E:/Animatedtimes/Meme Maker Automation/V2/font';


def showImage(image):

    cv2.imshow('image', image)
    cv2.waitKey(0)


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
    print(os.getcwd())
    os.chdir('../font')
    print(os.getcwd())
    print("Font Changed" + os.getcwd())
    cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Pass the image to PIL
    pil_im = Image.fromarray(cv2_im_rgb)

    draw = ImageDraw.Draw(pil_im)
    # use a truetype font
    font = ImageFont.truetype("Bebas.ttf", 20)

    # Draw the text
    draw.text((500, 700), text, font=font)

    # Get back the image to OpenCV
    return cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)


def saveFinal(memeFile, fileName):
    memeFile = addCredits(memeFile, "@animatedtimes")
    os.chdir('../output')
    print(os.getcwd())
    saveImage(fileName + "_final.jpg", memeFile)


def chooseTemplate(templateName):

    if (templateName == "AT"):
        templateImage = readImage(ATimage)
        return templateImage

    if (templateName == "FW"):
        templateImage = readImage(FWimage)
        return templateImage

def getStart(name):
    if(name == "AT"):
        return 90
    if (name == "FW"):
        return 77

def makeMeme(memefile,templateName):
    start = getStart(templateName)

    templateImage = chooseTemplate(templateName)

    memeImage = readImage(memefile)
    usableDimensions = getUsableDimensions(templateImage, start)
    print(usableDimensions)
    scale = getScaleForImage(usableDimensions, memeImage.shape)
    print(scale)
    templateImage = resizeImage(templateImage, scale)

    start = int(start*scale)

    usableDimensionsX = int(usableDimensions[0] * scale)
    usableDimensionsY = int(usableDimensions[1] * scale)

    usableDimensions = (usableDimensionsX, usableDimensionsY)

    finalImage = putImageOnTemplate(memeImage, templateImage, start, usableDimensions)

    saveFinal(finalImage, memefile)
    print("Image processed")


def loadImagesFromInput():
    os.chdir("input")
    listDir = os.listdir()
    for i in range(len(listDir)):
        os.chdir('../input')
        memefile = listDir[i]
        makeMeme(memefile, "FW")

def makeMemeWebImage(memefile, templateName):
    makeMeme(memefile, templateName)

#loadImagesFromInput()  #Load Image Locally
