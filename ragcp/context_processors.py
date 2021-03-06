from django.conf import settings


def user_settings(request):
    return {
        'FEED_ENABLED': settings.FEED_ENABLED,
        'CHANGELOG_ENABLED': settings.CHANGELOG_ENABLED,
        'RAGCP_CHANGELOG': settings.RAGCP_CHANGELOG,
        'STATIC_INDEX': settings.STATIC_INDEX
    }
