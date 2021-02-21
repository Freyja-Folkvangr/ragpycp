from os import environ


def get_configuration(variable_name: str):
    try:
        return environ[variable_name]
    except KeyError:
        print('Config not present: %s' % variable_name)
        return None


def get_rss_address():
    feed_url = get_configuration('RSS_FEED')

    if not feed_url:
        return 'https://zapier.com/engine/rss/973076/freyja'
    else:
        return feed_url
