import requests
import json
from globalconfig.global_variables import get_server_address


def open_page_and_listen_network(chrome_id, url, port, event_name):
    # 封装请求参数
    request_data = {
        "chrome_id": chrome_id,
        "url": url,
        "port": f":{port}/receive/{event_name}",
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/open_page_and_listen_network", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        page_id = response_data.get("page_id", None)
        return page_id
    else:
        return None


def open_page(chrome_id, url):
    # 封装请求参数
    request_data = {
        "chrome_id": chrome_id,
        "url": url,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/open_page", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        page_id = response_data.get("page_id", None)
        return page_id
    else:
        return None


def close_page(page_id):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/close_page", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        chrome_id = response_data.get("page_id", None)
        return chrome_id
    else:
        return None


def get_html(page_id):
    # 发送 HTTP 请求
    response = requests.get(get_server_address() + "/get_html", params="page_id=" + page_id)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        chrome_id = response_data.get("data", None)
        return chrome_id
    else:
        return None


def get_cookie(page_id, url):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "url": url,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_cookie", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        chrome_id = response_data.get("data", None)
        return chrome_id
    else:
        return None


def run_js(page_id, js):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "js": js,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/run_js", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        return False


def run_js_sync(page_id, js, timeout=60):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "js": js,
        "time_out": timeout,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/run_js_sync", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        result = response_data.get("data", None)
        if result:
            result = json.loads(result)['result']['result']['value']
            return result
    else:
        return None


def get_element_position_by_selector(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_element_position_by_css_on_page", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get("x", 0), response_data.get("y", 0)
    else:
        print("获取元素位置失败。")
        return None


def simulate_mouse_click(page_id, x, y):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "x": x,
        "y": y,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_mouse_click", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        return False


def simulate_mouse_move_to_target(page_id, x, y):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "x": x,
        "y": y,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_mouse_move_to_target", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        return False


def simulate_mouse_move_to_element(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_mouse_move_to_element", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get("x", 0), response_data.get("y", 0)
    else:
        print("获取元素位置失败。")
        return None


# simulateDrag
def simulate_drag(page_id, start_x, start_y, end_x, end_y):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "sx": start_x,
        "sy": start_y,
        "ex": end_x,
        "ey": end_y,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_drag", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        print("获取元素位置失败。")
        return False


def simulate_mouse_move_on_page(page_id, start_x, start_y, end_x, end_y):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "sx": start_x,
        "sy": start_y,
        "ex": end_x,
        "ey": end_y,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_mouse_move_on_page", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        print("获取元素位置失败。")
        return False


def simulate_keyboard(page_id, text):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "text": text,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_keyboard_input_on_page", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        print("获取元素位置失败。")
        return False


def simulate_scroll_to_element(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/simulate_scroll_to_element_by_selector", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        return True
    else:
        print("获取元素位置失败。")
        return False


class Node:
    def __init__(self, NodeType, NodeName, NodeValue, TextContent, HTMLContent, CSSSelector, XPathSelector):
        self.NodeType = NodeType
        self.NodeName = NodeName
        self.NodeValue = NodeValue
        self.TextContent = TextContent
        self.HTMLContent = HTMLContent
        self.CSSSelector = CSSSelector
        self.XPathSelector = XPathSelector


# get_first_child_element_by_css
def get_first_child_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_first_child_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # 提取data中的内容
        node_data = data['data']
        # 创建Node对象并返回
        return Node(**node_data)
    else:
        print("get_first_child_element_by_css 获取元素位置失败。")
        return None


# get_first_child_element_by_css
def get_next_sibling_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_next_sibling_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # 提取data中的内容
        node_data = data['data']
        # 创建Node对象并返回
        return Node(**node_data)
    else:
        print("get_next_sibling_element_by_css 获取元素位置失败。")
        return None


# get_previous_sibling_element_by_css
def get_previous_sibling_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_previous_sibling_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # 提取data中的内容
        node_data = data['data']
        # 创建Node对象并返回
        return Node(**node_data)
    else:
        print("get_previous_sibling_element_by_css 获取元素位置失败。")
        return None


# get_last_child_element_by_css
def get_last_child_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_last_child_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # 提取data中的内容
        node_data = data['data']
        # 创建Node对象并返回
        return Node(**node_data)
    else:
        print("get_last_child_element_by_css 获取元素位置失败。")
        return None


# get_parent_element_by_css
def get_parent_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_parent_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # 提取data中的内容
        node_data = data['data']
        # 创建Node对象并返回
        return Node(**node_data)
    else:
        print("get_parent_element_by_css 获取元素位置失败。")
        return None


# get_element_by_css
def get_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # 提取data中的内容
        node_data = data['data']
        # 创建Node对象并返回
        return Node(**node_data)
    else:
        print("get_element_by_css 获取元素位置失败。")
        return None


# get_all_child_element_by_css
def get_all_child_element_by_css(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/get_all_child_element_by_css", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        data = response.json()
        # # 创建Node对象并返回
        nodes_data = data['data']
        nodes = []
        for node_data in nodes_data:
            node = Node(
                node_data['NodeType'],
                node_data['NodeName'],
                node_data['NodeValue'],
                node_data['TextContent'],
                node_data['HTMLContent'],
                node_data['CSSSelector'],
                node_data['XPathSelector']
            )
            nodes.append(node)
        return nodes
    else:
        print("get_element_by_css 获取元素位置失败。")
        return None


def upload_files(page_id, selector):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "selector": selector,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/upload_files", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        True
    else:
        print("get_element_by_css 获取元素位置失败。")
        return False


# set_cookie
def set_cookie(page_id, key, value, domain):
    # 封装请求参数
    request_data = {
        "page_id": page_id,
        "key": key,
        "value": value,
        "url": domain,
    }
    # 发送 HTTP 请求
    response = requests.post(get_server_address() + "/set_cookie", data=request_data)
    # 解析返回结果
    if response.status_code == 200:
        True
    else:
        print("set_cookie 失败。")
        return False


# set_cookie

def get_currentURL(page_id):
    # 封装请求参数
    return run_js_sync(page_id, "window.location.href;", 60)
