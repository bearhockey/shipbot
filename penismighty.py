import requests
from random import choice


def get_word_from_site():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    all_words = response.content.splitlines()
    return choice(all_words)
