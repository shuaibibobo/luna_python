import time
import devtools.browser as luna
import devtools.page as page
from common.kill_process import kill_process
from common.create_cache_dir import create_cache_dir_in_sub_dir
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
        new_browser 打开浏览器
    """
    # 杀掉其他的所有chromium相关进程->主要针对测试场景下、很多未被正常关闭的浏览器
    kill_process()
    path = "/Users/hongyuji/Documents/workspace/python/luna_pro/cache"
    # 在给定目录下创建缓存目录,在多线程场景下，这个函数是几乎必须的;这会影响到你的指纹和稳定性
    # 逻辑是你每次打开浏览器的时候，都会新创建一个缓存目录； 如果目录文件积累太大，自己记得写逻辑清除。
    cp = create_cache_dir_in_sub_dir(path)
    chrome_id = luna.new_browser(chromium_path, cache_path=cp)
    time.sleep(1)
    """
          new_browser 打开网址;chrome_id 代表的是你准备在哪个浏览器打开网址;
      """
    page.open_page(chrome_id, "http://www.baidu.com")
    time.sleep(5)


if __name__ == "__main__":
    main()
