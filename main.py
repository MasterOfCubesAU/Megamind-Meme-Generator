from PIL import Image, ImageDraw, ImageFont
import requests
import math
from io import BytesIO

DEFAUT_SIZE = 75


def calculateScaleFactor(word, maxLength):
    captionLength = ImageFont.truetype("Impact", size=DEFAUT_SIZE).getlength(word)
    return (
        (1 - ((captionLength - maxLength) / captionLength))
        if captionLength > maxLength
        else 1
    )


def generateImage(word):
    caption = f"NO {word}?"
    template = Image.open(
        BytesIO(requests.get("https://i.imgflip.com/64sz4u.png").content)
    )
    font = ImageFont.truetype(
        "Impact",
        size=round(
            DEFAUT_SIZE
            * calculateScaleFactor(caption, math.floor(template.size[0] * 0.9))
        ),
    )
    canvas = ImageDraw.Draw(template)
    canvas.text(
        ((template.size[0] / 2) - (font.getlength(caption) / 2), 20),
        caption,
        fill="#fff",
        font=font,
        stroke_fill="#000",
        stroke_width=3,
    )
    return template


generateImage(
    requests.get("https://random-WORD-form.herokuapp.com/random/noun").json()[0].upper()
).show()
