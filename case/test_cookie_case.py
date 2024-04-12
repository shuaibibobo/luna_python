import time

import devtools.browser as luna
import devtools.page as page
import devtools.script as js
import common.server_management as init


def main():
    if not init.start():
        print("启动服务-失败")

    chromiumPath = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"

    windowSize = luna.WindowSize(width=1024, height=768)  # 示例窗口大小
    # 调用 make_http_request 函数
    chrome_id = luna.new_browser(chromiumPath, window_size=windowSize)
    # 检查返回结果
    time.sleep(1)

    page_id = page.open_page(chrome_id, "http://www.baidu.com")

    page.set_cookie(page_id, "abk", "1jsk", ".baidu.com")

    cookies = page.get_cookie(page_id, "http://www.baidu.com")

    print("获取到到cookies:", cookies)
    time.sleep(3)
    page.run_js(page_id, js.show_mouse_position())
    print("当前的url是", page.get_currentURL(page_id))
    time.sleep(10)
    page.close_page(page_id)
    luna.close_browser(chrome_id)


if __name__ == "__main__":
    main()
