import re
import wikipedia


def get_random_noun():
    page = wikipedia.random(pages=1)
    noun = re.sub("List of", '', page)
    return noun, wikipedia.page(page).url
