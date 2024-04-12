import time

import devtools.browser as luna
import devtools.page as page
import common.server_management as init

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
            proxy 支持多种方式 代理ip;http、https、sockts5代理类型、同时无论是否有用户名密码均支持。
            如："socks5://username:password@ip:port"
            如："https://username:password@ip:port"
            如："http://ip:port"
            ProxyStr:  "https://username:password@ip:port",
    """
    proxy_xxx = "http://42.179.160.60:39349"
    chrome_id = luna.new_browser(chromium_path, proxy_str=proxy_xxx)
    time.sleep(1)
    """
          new_browser 打开网址;chrome_id 代表的是你准备在哪个浏览器打开网址;
      """
    page_id = page.open_page(chrome_id, "http://www.baidu.com")
    time.sleep(5)
    html = page.get_html(page_id)
    print("网页内容大小是:", len(html))
    page.close_page(page_id)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
