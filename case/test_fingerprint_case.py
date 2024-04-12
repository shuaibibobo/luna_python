import time

import devtools.browser as luna
import devtools.page as page
import common.server_management as init

"""
测试目的:希望你可以正常使用指纹
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

    args = [
        "--luna_cavans_random_str=B3B4",
        "--luna_user_agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "--luna_platform=win64",
        "--luna_languages=en-GB",
        "--luna_deviceMemory=8",
        "--luna_UNMASKED_VENDOR_WEBGL=Intel Corporation",
        "--luna_UNMASKED_RENDERER_WEBGL=Intel(R) UHD Graphics 620",
        "--luna_GL_VERSION=WebGL 1.0 (OpenGL ES 3.0 Intel(R) UHD Graphics 620)",
        # 仅是示例、更多指纹设置参考luna golang版本文档-都是一样的
    ]  # 示例指纹列表,

    chrome_id = luna.new_browser(chromium_path, fingerprint=args)

    time.sleep(1)

    page_id = page.open_page(chrome_id, "http://www.baidu.com")

    print("便于您查看指纹、暂停1分钟")
    time.sleep(60)

    page.close_page(page_id)
    # 关闭浏览器
    print("关闭浏览器", luna.close_browser(chrome_id))


if __name__ == "__main__":
    main()
