import time

import devtools.browser as luna
import devtools.page as page
import devtools.script as js
import common.server_management as init


def main():
    # 我建议他自己随便选用一个未被占用的端口
    if not init.start():
        print("启动服务-失败")
    # 设置要传递给 make_http_request 函数的参数
    chromiumPath = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"
    CachePath = "/Users/hongyuji/Documents/workspace/golang/cache/"
    ImgPath = ""
    Headless = False
    ProxyStr = ""
    Fingerprint = ["--luna_cavans_random_str=B3B4", "--luna_hardwareConcurrency=16"]  # 示例指纹列表
    windowSize = luna.WindowSize(width=1024, height=768)  # 示例窗口大小

    # 调用 make_http_request 函数
    chrome_id = luna.new_browser(chromiumPath, CachePath, ImgPath, Headless, ProxyStr, Fingerprint, windowSize)
    # 检查返回结果
    if chrome_id:
        print("Chrome ID:", chrome_id)
    else:
        print("Failed to create new browser.")
    print("chrome_id:", chrome_id)
    page_id = page.open_page(chrome_id, "http://www.baidu.com")
    page.set_cookie(page_id, "abk", "1jsk", ".baidu.com")
    print(page.get_cookie(page_id, "http://www.baidu.com"))
    # print(page.get_html(page_id))
    time.sleep(3)
    page.run_js(page_id, js.show_mouse_position())
    print(page.get_currentURL(page_id))
    for node in page.get_all_child_element_by_css(page_id, "#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap"):
        print("Node Type:", node.NodeType)
        print("Node Name:", node.NodeName)
        print("Node Value:", node.NodeValue)
        print("Text Content:", node.TextContent)
        print("HTML Content:", node.HTMLContent)
        print("CSS Selector:", node.CSSSelector)
        print("XPath Selector:", node.XPathSelector)
        print("-----------------------------------")
    ka = page.get_element_by_css(page_id, "#form > span.bg.s_ipt_wr.new-pmd.quickdelete-wrap")
    print(ka.CSSSelector, ka.XPathSelector)
    position = page.simulate_mouse_move_to_element(page_id, "#kw")
    print(position, ">>>>")
    if position is not None:
        x, y = position
        # page.simulate_mouse_move_to_target(page_id, x, y)
        page.simulate_mouse_click(page_id, x, y)
        time.sleep(1)
        page.simulate_keyboard(page_id, "123123")
        page.simulate_mouse_move_on_page(page_id, x, y, 100, 100)
        time.sleep(5)
        ##page > div > strong > span
        page.simulate_scroll_to_element(page_id, "#page > div > strong > span")
        page.simulate_drag(page_id, 100, 100, 500, 500)
        page.upload_files(page_id, "#page > div > strong > span")
    else:
        print("获取元素位置失败。")
    time.sleep(5)
    page.close_page(page_id)
    # 关闭浏览器
    print(">>>>>", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
