HOST = "localhost"
PORT = 80

USE_CDN = False  # 是否使用了CDN
REAL_IP_HEADER = "X-Forwarded-For"  # CDN回源请求头携带的真实客户端IP头部

IP_WHITE_LIST_ENABLE = False  # 是否启用IP白名单
IP_WHITE_LIST = []  # IP白名单

IP_BLACK_LIST_ENABLE = False  # 是否启用IP黑名单
IP_BLACK_LIST = []  # IP黑名单
