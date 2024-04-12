from bottle import Bottle, request
import threading


class SubscriptionHandler:
    _subscriptions = {}
    _lock = threading.Lock()

    @classmethod
    def subscribe(cls, path, handler, method='GET'):
        with cls._lock:
            if path not in cls._subscriptions:
                cls._subscriptions[path] = {}
            cls._subscriptions[path][method] = handler

    @classmethod
    def notify_subscribers(cls, path, data, method='GET'):
        with cls._lock:
            if path in cls._subscriptions and method in cls._subscriptions[path]:
                subscriber_handler = cls._subscriptions[path][method]
                # Start a new thread to handle the notification
                thread = threading.Thread(target=subscriber_handler, args=(data,))
                thread.start()


app = Bottle()


@app.route('/subscribe/<path:path>', method=['POST', 'GET'])
def subscribe(path):
    def handler(data):
        print(f"Received data for path '{path}': {data}")

    if request.method == 'POST':
        SubscriptionHandler.subscribe(path, handler, 'POST')
        return f"Subscribed to path '{path}' via POST"
    else:  # GET request
        SubscriptionHandler.subscribe(path, handler)
        return f"Subscribed to path '{path}' via GET"


@app.get('/receive/<path:path>')
def receive_data_get(path):
    SubscriptionHandler.notify_subscribers(path, request.query)
    return f"Notified subscribers for path '{path}'"


@app.post('/receive/<path:path>')
def receive_data_post(path):
    SubscriptionHandler.notify_subscribers(path, request.body.read().decode('utf-8'), 'POST')
    return f"Notified subscribers for path '{path}' via POST"


def start_event_server(r_port):
    """
    启动 Bottle 服务器并等待完全启动后执行其他逻辑

    参数：
    - port: 服务器端口号
    """

    # 定义启动 Bottle 服务器的函数
    def run_server():
        app.run(host='127.0.0.1', port=r_port, debug=True)

    # 创建一个线程来启动 Bottle 服务器
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # # 等待服务器启动
    # print("等待 Bottle 服务器启动...")
    # server_started.wait()
    # print("Bottle 服务器已启动，可以执行其他操作了。")

# def run_server(r_port):
#     app.run(host='localhost', port=r_port, debug=True)

# if __name__ == "__main__":
#     server_thread = threading.Thread(target=run_server)
#     server_thread.start()
#
#
#     def custom_handler_get(data):
#         print(f"Custom handler received data get : {data}")
#
#
#     def custom_handler_post(data):
#         print(f"Custom handler received data post : {data}")
#
#
#     SubscriptionHandler.subscribe("23423qweewe4", custom_handler_get, 'GET')
#     SubscriptionHandler.subscribe("3423weqwer", custom_handler_post, 'POST')
