#!/usr/bin/python

"""
Hello! I'm Ship Bot. I do things.
"""

import argparse
import os

from imgurpython import ImgurClient
from random import choice

import lighthouse
import memester
import wikiwiki


class ShipBot(object):
    def __init__(self):
        self.client_id = "d423e3f49823d02"
        self.client_secret = "6d3052e94492d230cb7ef7117a781c52aafbaae4"
        self.imgur_client = ImgurClient(self.client_id, self.client_secret)

        self.prog_path = os.path.dirname(os.path.realpath(__file__))
        self.meme_path = os.path.join(self.prog_path, "images", "ship.png")

        self.ship_names = ["ship", "ships", "boat", "shipwreck", "tugboat", "cruise ship", "submarine", "pirate",
                           "sail", "craft", "navy", "haul", "transfer", "release"]

    def listen(self, in_string):

        if isinstance(in_string, basestring):
            lower_string = in_string.lower()

            if "ship it" in lower_string:
                response = lighthouse.get_image_imgur(choice(self.ship_names))
                print response
                if "http" in response:
                    memester.make_meme(response, self.meme_path, "SHIP IT")
                    # response = lighthouse.upload_image_to_imgur(self.meme_path)
            elif "burger" in lower_string:
                noun, url = wikiwiki.get_random_noun()
                response = "'{0}' makes the best hamburgers!".format(noun)
            else:
                response = "You said: {0}".format(in_string)
        else:
            response = "This isn't even a string. Come on."
        return response

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="A friendly bot to make some ship memes.", version="1.0")

    parse.add_argument("command", help="The command to give to Ship Bot.")

    args = parse.parse_args()
    ship_bot = ShipBot()
    print ship_bot.listen(args.command)
