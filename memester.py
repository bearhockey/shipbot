""" Takes an image from a passed in url and makes it into a meme """

import cStringIO
import urllib2

from PIL import Image, ImageFont, ImageDraw


def make_meme(image_url, file_name, meme_text):
    file = cStringIO.StringIO(urllib2.urlopen(image_url).read())
    try:
        img = Image.open(file)
    except Exception as e:
        print "Fuck it didn't work"
        return "WHOOPS"
    try:
        img.seek(1)
    except EOFError:
        isanimated = False
    else:
        isanimated = True
        img.paste(img.seek(1))

    print "Image is animted GIF: {0}".format(isanimated)
    new_img = img.resize((300, 300))

    font = ImageFont.truetype("impact.ttf", 64)
    draw = ImageDraw.Draw(new_img)
    text_length = len(meme_text)
    draw.text((300 - (text_length * 34), 224), meme_text, font=font, fill=(0, 0, 0, 255))
    draw.text((296 - (text_length * 34), 220), meme_text, font=font, fill=(255, 255, 255, 255))

    new_img = new_img.convert('P')
    new_img.save(file_name, optimize=True)

    return file
