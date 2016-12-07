""" Takes an image from a passed in url and makes it into a meme """

import cStringIO
import urllib2

from PIL import Image, ImageFont, ImageDraw
import gifextract


def make_meme(image_url, file_name, meme_text):
    image_file = cStringIO.StringIO(urllib2.urlopen(image_url).read())
    meme_text = unicode(meme_text)
    try:
        img = Image.open(image_file)
    except Exception as e:
        print "Fuck it didn't work"
        return "WHOOPS"

    try:
        img.seek(1)
    except EOFError:
        isanimated = False
        img.seek(0)
    else:
        isanimated = True
        img = gifextract.process_image(image_file, frame=0)
        # img.seek(1)

    print "Image is animted GIF: {0}".format(isanimated)
    width = 640
    height = 480
    text_size = int(height * 0.2)

    new_img = img.resize((width, height))

    try:
        font = ImageFont.truetype("impact.ttf", text_size)
        draw = ImageDraw.Draw(new_img)
        text_length = font.getsize(meme_text)[0]
        print "Text width is: {0}".format(text_length)
        # text_length = len(meme_text)
    except Exception as e:
        print "Something went wrong with drawing: {0}".format(e)
        return "bad"

    try:
        x_position = int(width / 2 - text_length / 2)
        y_position = int(height - text_size - 8)
        # border
        draw.text((x_position - 2, y_position - 2), meme_text, font=font, fill=(0, 0, 0, 255))
        draw.text((x_position + 2, y_position - 2), meme_text, font=font, fill=(0, 0, 0, 255))
        draw.text((x_position - 2, y_position + 2), meme_text, font=font, fill=(0, 0, 0, 255))
        draw.text((x_position + 4, y_position + 4), meme_text, font=font, fill=(0, 0, 0, 255))
        draw.text((x_position, y_position), meme_text, font=font, fill=(255, 255, 255, 255))
    except Exception as e:
        print "Something went wrong with text: {0}".format(e)
        return "bad"

    try:
        new_img = new_img.convert('P')
        new_img.save(file_name, optimize=True)
    except Exception as e:
        print "Something went wrong with saving file: {0}".format(e)
        return "bad"

    return image_file
