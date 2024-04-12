import portpicker

global_port = 9876
global_host = "127.0.0.1"


def set_port(port=None):
    if port is None:
        port = portpicker.pick_unused_port()
    global global_port  # 声明要修改的是全局变量 global_port
    global_port = port


def get_server_address():
    return f"http://{global_host}:{global_port}"


def get_global_port():
    return global_port
