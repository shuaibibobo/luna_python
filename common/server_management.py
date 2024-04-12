import subprocess
import time
import threading
from common.executable_path_finder import get_executable_path
from globalconfig.global_variables import set_port, get_global_port
from devtools.browser import ready


def start_server(executable_path):
    """
    启动可执行程序作为服务器，监听端口，并返回进程对象。

    参数:
    executable_path (str): 可执行程序的路径。

    返回:
    subprocess.Popen: 表示启动的进程对象。
    """
    try:
        # 启动可执行程序作为子进程，并返回进程对象
        process = subprocess.Popen([executable_path, str(get_global_port())])
        return process
    except Exception as e:
        print("启动服务器失败:", e)
        return None


def is_process_running(process):
    """
    判断给定的进程是否在运行。

    参数:
    process (subprocess.Popen): 表示进程对象。

    返回:
    bool: 如果进程正在运行，则返回True，否则返回False。
    """
    if process is None:
        return False

    return process.poll() is None


def kill_process(process):
    """
    结束给定的进程。

    参数:
    process (subprocess.Popen): 表示进程对象。
    """
    if process is not None:
        try:
            # 结束进程
            process.kill()
            print("进程已结束")
        except Exception as e:
            print("结束进程失败:", e)


def server_function():
    # 启动服务器
    server_process = start_server(get_executable_path())
    print(server_process)


def start(port=None):
    # 将传入的端口确定为全局端口、
    set_port(port)
    # 启动服务器线程
    server_thread = threading.Thread(target=server_function)
    server_thread.start()
    # 循环5秒探测 是否已经启动完备、如果ok那么开始执行逻辑，否则等5秒后返回失败
    for i in range(5):
        if ready():
            return True
        if i == 4:
            print("连接服务器失败，程序退出")
        time.sleep(1)  # 暂停一秒钟
    return False


