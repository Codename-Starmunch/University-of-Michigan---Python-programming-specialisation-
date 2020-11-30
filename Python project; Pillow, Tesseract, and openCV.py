from zipfile import ZipFile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import os

face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

print("This is going to take a reaaaaalllllly looooong tiiiiiime 0_o")

with ZipFile("readonly/images.zip", "r") as zipObj:
    zipObj.extractall("unzipped_files/")


def find_text(x):
    open_image = Image.open(x)
    image_to_string = pytesseract.image_to_string(open_image)
    image_to_string = image_to_string.lower()

    return image_to_string.split()


def squares(x):
    original_page = cv.imread(x)
    greyscale = cv.cvtColor(original_page, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(greyscale, scaleFactor=1.35, minNeighbors=5, minSize=(25, 25))

    contact_sheet = None

    if len(face) > 0:
        pillow_page = Image.open(x)
        contact_sheet = Image.new(pillow_page.mode, (5 * 100, 100 * (len(face) // 5 + 1)))

        x = 0
        y = 0

        for a, b, c, d in face:
            crop_faces = pillow_page.crop((a, b, a + c, b + d))
            contact_sheet.paste(crop_faces.resize((100, 100), Image.ANTIALIAS), (x, y))

            if x == 500:
                x = 0
                y += 100

            else:
                x += 100

        return contact_sheet


def name_scan(name):
    name = name.lower()

    print("Scan for: " + name + "... ")

    for x in os.listdir("unzipped_files/"):
        filepath = "unzipped_files/" + x

        if name in find_text(filepath):
            print("Results found in file " + x)

            if squares(filepath) is None:
                print("But there were no faces in that file! ")

            else:
                display(squares(filepath))


name_scan("Mark")
name_scan("Christopher")
