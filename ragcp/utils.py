from os import getenv


def get_configuration(variable_name: str):
    return getenv(variable_name, None)


def get_rss_address():
    feed_url = get_configuration('RSS_FEED')

    if feed_url:
        return feed_url
    else:
        return 'https://zapier.com/engine/rss/973076/freyja'
