from Helpers.config import USE_CDN, IP_WHITE_LIST_ENABLE, IP_BLACK_LIST_ENABLE, IP_BLACK_LIST, IP_WHITE_LIST, \
    REAL_IP_HEADER


def ip(request):
    if USE_CDN:
        realIP = str(request.headers.get(REAL_IP_HEADER))
    else:
        realIP = str(request.remote_addr)
    if IP_WHITE_LIST_ENABLE:
        if realIP in IP_WHITE_LIST:
            return True
        else:
            return False
    elif IP_BLACK_LIST_ENABLE:
        if realIP in IP_BLACK_LIST:
            return False
        else:
            return True
    else:
        return True
