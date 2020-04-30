import wikipedia


def get_full_info(topic):
    return wikipedia.page(topic).content


    