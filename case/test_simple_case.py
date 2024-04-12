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
            因为python版本、其实是我的golang版本的http协议方式封装
            也就是封装了可执行程序
            所以这个会自动找寻对应的 可执行程序、也就是一个web服务器;
            所以这个是必须要的;至于是否传入端口的区别是，一个你指定，你不写他就选随机未占用端口。
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
    time.sleep(5)
    html = page.get_html(page_id)
    print("网页内容大小是:", len(html))
    page.close_page(page_id)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
