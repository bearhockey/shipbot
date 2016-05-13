""" Helper functions for searching for images (returns the url) """

from imgurpython import ImgurClient


def get_image_imgur(search, index=0, nsfw=False):
    client_id = "d423e3f49823d02"
    client_secret = "6d3052e94492d230cb7ef7117a781c52aafbaae4"
    imgur_client = ImgurClient(client_id, client_secret)
    result = imgur_client.gallery_search(search)
    # result = imgur_client.gallery_random()
    print "{0} results".format(len(result))
    got_image = False
    while not got_image:
        if index > len(result)-1:
            print "Reached end, wrapping"
            index = 0
        image = result[index]
        if image.is_album:
            print "Got album, skipping"
            index += 1
        else:
            got_image = True
    if image.nsfw and nsfw is False:
        response = "Image is NSFW"
    else:
        response = image.link
    return response