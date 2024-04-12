import time

import devtools.browser as luna
import devtools.page as page
import common.server_management as init


def main():
    """
        因为python版本、其实是我的golang版本的http协议方式封装
        也就是封装了可执行程序
        所以这个会自动找寻对应的 可执行程序、也就是一个web服务器;
        所以这个是必须要的;至于是否传入端口的区别是，一个你指定，你不写他就选随机未占用端口。
    """
    if not init.start():
        print("启动服务-失败")
    """
        浏览器地址、如果是windows请精确到.exe；如c:\\Default\\chrome.exe
        如果你不需要抗指纹特性,你可以用任何Chrome浏览器代替;如果遇到权限问题、mac、Windows 可以用快捷方式代替;linux 可以用软连接代替
        这个参数是必选项
    """
    chromium_path = "/Users/hongyuji/Documents/workspace/golang/Chromium.app/Contents/MacOS/Chromium"
    """
        可选项:cache_path 浏览器缓存目录、非多线程情况下；无所谓；多线程情况下、抗指纹情况下建议写；
        参考test_other_case.py的写法 是比较好的；
    """
    cache_path = "/Users/hongyuji/Documents/workspace/golang/cache/"
    """
        可选:这个是视觉相关的、暂时不准备放入python版本、所以可以不传入
    """
    img_path = ""
    """
        可选:隐身模式or显示模式 根据你自己需求来、如果你不传入默认显示模式
    """
    headless = False
    """
        可选:代理ip 参考test_proxy_case.py写法
    """
    proxy_str = ""
    """
        可选:抗指纹部分-参考test_fingerprint_case.py
    """
    fingerprint = ["--luna_cavans_random_str=B3B4", "--luna_hardwareConcurrency=16"]  # 示例指纹列表
    """
            可选:初始化窗口大小
    """
    window_size = luna.WindowSize(width=1024, height=768)  # 示例窗口大小
    # 调用 make_http_request 函数
    chrome_id = luna.new_browser(chromium_path, cache_path, img_path, headless, proxy_str, fingerprint, window_size)
    # 检查返回结果
    if chrome_id:
        print("Chrome ID:", chrome_id)
    else:
        print("Failed to create new browser.")
    print("chrome_id:", chrome_id)
    page.open_page(chrome_id, "http://www.baidu.com")
    time.sleep(60)


if __name__ == "__main__":
    main()
