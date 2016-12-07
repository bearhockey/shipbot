""" Helper functions for searching for images (returns the url) """
import datetime

from imgurpython import ImgurClient
from random import randint


def get_image_imgur(search, index=None, nsfw=False):
    client_id = "d423e3f49823d02"
    client_secret = "6d3052e94492d230cb7ef7117a781c52aafbaae4"
    imgur_client = ImgurClient(client_id, client_secret)
    if search.lower() == "random":
        result = imgur_client.gallery_random()
    else:
        result = imgur_client.gallery_search(search)
    print "{0} results".format(len(result))
    got_image = False
    image = None
    if len(result) > 0:
        if index is None:
            index = randint(0, len(result))
        while not got_image:
            if index > len(result) - 1:
                print "Reached end, wrapping"
                index = 0
            image = result[index]
            if image.is_album:
                print "Got album, getting ID from cover: {0}".format(image.cover)
                image = imgur_client.get_image(image.cover)
                got_image = True
            else:
                got_image = True
            if image.nsfw and nsfw is False:
                print "Image is NSFW"
                got_image = False
                index += 1
        response = image.link
        print "Fun facts: {0} - {1}".format(image.title, image.description)
        return response, image.title, image.description
    else:
        print "Length of result was {0}?!?".format(len(result))
        return "A bad thing happened"


def upload_image_to_imgur(file_path):
    client_id = "d423e3f49823d02"
    client_secret = "6d3052e94492d230cb7ef7117a781c52aafbaae4"
    imgur_client = ImgurClient(client_id, client_secret)
    config = {
        "album": None,
        "name": "SHIP IT",
        "title": "SHIP IT",
        "description": "Ship Bot strikes again! {0}".format(datetime.datetime.now())
    }
    print "Uploading image '{0}' to Imgur...".format(file_path)
    image = imgur_client.upload_from_path(file_path, config=config, anon=True)
    image_url = image["link"]
    print "Returned url: {0}".format(image_url)
    return image_url
