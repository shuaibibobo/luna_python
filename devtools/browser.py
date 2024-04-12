import requests
from globalconfig.global_variables import get_server_address


class WindowSize:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def new_browser(chromium_path, cache_path='', img_path='', headless=False, proxy_str='', fingerprint=[],
                window_size=None):
    # 封装请求参数
    request_data = {
        "chromiumPath": chromium_path,
        "cachePath": cache_path,
        "imgPath": img_path,
        "headless": headless,
        "proxyStr": proxy_str,
        "fingerprint": fingerprint,
        "windowSize": None if window_size is None else {"width": window_size.width, "height": window_size.height}
    }

    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/new_browser", json=request_data)

    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        chrome_id = response_data.get("chrome_id", None)
        return chrome_id
    else:
        return None


def close_browser(chromeId):
    # 封装请求参数
    form_data = {
        "chrome_id": chromeId
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/close_browser", data=form_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        return False


def ready():
    try:
        # 发送 HTTP 请求
        response = requests.get(get_server_address() + "/ready")
        # 解析返回结果
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False
