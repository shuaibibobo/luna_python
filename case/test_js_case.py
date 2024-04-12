import time

import devtools.browser as luna
import devtools.page as page
import common.server_management as init
import devtools.script as js

"""
这是一个简单的案例
测试目的:希望你可以正常打开指纹浏览器、并且打开一个网址
"""


def main():
    """
    start函数是启动 服务、你可以选择传入参数;就是端口号、你也可以不传入、如果你不传入 程序会自动选择一个未被占用的端口。
    如果你不清楚他有什么用、可以不予理睬
    """
    if not init.start(9876):
        print("启动服务-失败")

    """
        chromium_path 是必须要传入的参数、就是你抗指纹浏览器所在的路径 如 c:\\luna\\Default\\chrome.exe
    """
    chromium_path = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"
    """
        new_browser 打开浏览器
    """
    chrome_id = luna.new_browser(chromium_path)
    time.sleep(1)
    """
          new_browser 打开网址;chrome_id 代表的是你准备在哪个浏览器打开网址;
      """
    page_id = page.open_page(chrome_id, "http://www.baidu.com")
    time.sleep(3)
    page.run_js(page_id, js.show_mouse_position())

    js_result = page.run_js_sync(page_id, "window.location.href;")
    print("js_result:", js_result)

    time.sleep(60)
    page.close_page(page_id)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
