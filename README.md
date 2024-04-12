# luna_python Luna - 基于视觉的抗指纹爬虫第三方库

golang版本地址:https://github.com/musiclover789/luna

本版本是基于golang的版本封装的python版本;

缺点是相对于golang版本更加年轻,优点是方便比较熟悉python的开发者、如果您发现任何bug或者

本框架不太完善的地方,欢迎提出任何意见，酌情优化。但是目前python并未封装 视觉部分。




Luna 是一款强大的第三方库，专为抗指纹自动化爬虫而设计。通过利用视觉特征和先进的算法，Luna 提供了一种有效的方法来对抗现代爬虫检测技术，保护您的网络资源免受恶意爬取和滥用。

## 功能亮点

- **强大的抗指纹技术：** Luna 提供了先进的抗指纹技术，使您的爬虫程序难以被识别。
- **视觉特征解析：** 基于视觉特征的页面解析和操作，使爬虫更智能。
- **简单易用的接口：** Luna 提供简单易用的接口，轻松集成和使用它的功能。
- **智能化行为模拟：** 模拟用户行为，有效应对现代爬虫检测技术。
- **绕过检测技术：** 具备绕过常见爬虫检测技术的能力，确保您的爬虫不容易被拦截。

  效果展示-加载可能有些慢
![效果展示-g](https://i.ibb.co/yPkZLd0/mnggiflab-compressed-20231026-215253-min.gif)

## 为什么选择 Luna

使用 Luna，您可以快速构建出智能、高效、难以被识别的爬虫程序。不论是在开发自动化测试脚本、数据采集应用还是其他需要模拟用户行为的场景中，Luna 都能为您提供可靠的解决方案。

不论您是开发人员、数据科学家还是网络安全专家，Luna 都是您在抗指纹爬虫领域的得力助手。让 Luna 成为您的选择，保护您的网络资源，确保您的数据安全。



目前支持的操作系统是 Windows，且仅限于 x86-64 架构。已经在 Windows x86-64 硬件环境下进行了测试。其他操作系统或平台的测试尚不充分，因此不建议在这些系统上使用。



## 开始使用 Luna

详细的使用说明和示例代码，请查看本项目的[文档](https://musiclover789.github.io/lunadocs/)。

示例代码部分也可以查看源码的case包下内容。


## Luna浏览器部分
浏览器部分是 Luna 的核心功能之一，它使您能够执行抗指纹爬虫任务。请注意，您需要下载适用于 Luna 的专用浏览器才能实现指纹防识别。该浏览器的大小约为 2GB，因此需要一些时间来下载。如果您没有抗指纹需求、可以直接用您的chrome或其他浏览器即可。

目前，我们已经将浏览器文件上传到 百度 网盘，并提供了下载链接：



链接: https://pan.baidu.com/s/14EZw9DvCtO998LOwo_epvA 提取码: mm6s



### 如何测试



正常使用情况下，这部分完全代码来控制。但是为了方便您测试luna浏览器的基础功能，可以使用手动的方式来测试。

原理：这个是基于chromium的源代码，对内核进行修改编译的。

测试步骤：

1、在您的c盘根目录，手工建立一个文件夹luna-temp
示例:           C:\luna-temp

2、打开浏览器，有些同学不太知道怎么打开浏览器，就是下载好后，找到目录里面的 chrome.exe 用鼠标双击打开.
ps:" I 服了 you ，如果不知道怎么双击打开，我建议你直接放弃研究本项目"

3、你会发现，C:\luna-temp 目录里面会有一个uname.txt文件，你测试的时候无需关心。

4、在这个目录下，手工创建一个文件，命名为1696987203497907900 



也就是路径应该是 C:\luna-temp\1696987203497907900



注意不要有.txt的扩展名。



然后用记事本打开，黏贴如下内容：

```
luna_user_agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
luna_platform=win64
luna_timezone=Europe/London
luna_timezone_offset=3600000
luna_languages=en-GB
luna_userAgentData=Google Chrome:92-luna-Chromium:92-luna-Not-A.Brand:24-luna-platform:win32-luna-mobile:false-luna-platform_version:6.1-luna-ua_full_version:92.0.4515.186-luna-model:PC-luna-architecture:x86_64
luna_header_1=User-Agent-lunareplace-Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
luna_header_2=sec-ch-ua-arch-lunaremove-
luna_header_3=sec-ch-ua-platform-lunaremove-
luna_header_4=accept-language-lunareplace-en;q=0.9
luna_deviceMemory=8
luna_hardwareConcurrency=16
luna_UNMASKED_VENDOR_WEBGL=Intel Corporation
luna_UNMASKED_RENDERER_WEBGL=Intel(R) UHD Graphics 620
luna_GL_VERSION=WebGL 1.0 (OpenGL ES 3.0 Intel(R) UHD Graphics 620)
luna_GL_SupportedExtensions=["ANGLE_instanced_arrays", "EXT_blend_minmax", "EXT_color_buffer_half_float", "EXT_disjoint_timer_query", "EXT_float_blend", "EXT_frag_depth", "EXT_shader_texture_lod", "EXT_texture_compression_rgtc", "EXT_texture_filter_anisotropic", "WEBKIT_EXT_texture_filter_anisotropic", "EXT_sRGB", "KHR_parallel_shader_compile", "OES_element_index_uint", "OES_fbo_render_mipmap", "OES_standard_derivatives", "OES_texture_float", "OES_texture_float_linear", "OES_texture_half_float", "OES_texture_half_float_linear", "OES_vertex_array_object", "WEBGL_color_buffer_float", "WEBGL_compressed_texture_s3tc", "WEBKIT_WEBGL_compressed_texture_s3tc", "WEBGL_compressed_texture_s3tc_srgb", "WEBGL_debug_renderer_info", "WEBGL_debug_shaders", "WEBGL_depth_texture", "WEBKIT_WEBGL_depth_texture", "WEBGL_draw_buffers", "WEBGL_lose_context", "WEBKIT_WEBGL_lose_context", "WEBGL_multi_draw"]
luna_GL_VENDOR=WebKit
luna_GL_RENDERER=WebKit WebGL
luna_GL_SHADING_LANGUAGE_VERSION=WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)
luna_cavans_random_str=B3B4
remote-debugging-port=55392
user-data-dir=C:\workspace\tempcatch\chromium_user_data_1696987203497907900
```

退出浏览器，再次打开。理论上你可以抓包看一下，无论你访问任何网站，无论你的电脑是什么配置，你的useragent会改成配置文件里面的 

Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36

还记得这个配置文件的命名么？1696987203497907900

这个是当前毫秒数而已，如果多个配置文件，他只会选用最新的。也就是最新的当前毫秒数，正常情况下，我们都是用程序去调用，并不会人工去测试这些东西。

仅提供 手工测试 爱好者。





## 快速入门

```python
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
        chromium_path 是必须要传入的参数、就是你抗指纹浏览器所在的路径 如c:\\Default\\chrome.exe        
    """
    chromium_path = "c:\\Default\\chrome.exe"
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

```

## 特点

## 1. 抗指纹特性

Luna 强大的抗指纹技术可以模拟和对抗多种常见爬虫检测技术，包括但不限于：

- 时区指纹
- 显卡指纹
- User-Agent 指纹
- Platform 指纹
- Languages 指纹
- Device Memory 指纹
- Hardware Concurrency 指纹
- Canvas 指纹
- 鼠标滚动指纹（真实很难被识别）
- 鼠标移动轨迹（真实很难被识别）
- 键盘真实输入（包括内置转输入法等）

理论上，Luna 可以成功对抗这些指纹技术，使您的爬虫在操作时不容易被识别。更多详细信息请查看我们的[文档](https://musiclover789.github.io/lunadocs/)。

## 2. 基于视觉的操作

Luna 基于视觉的页面操作方法让您可以使用截图的方式来控制浏览器，也支持传统的 CSS 和 XPath 选择器等方式。这意味着您可以立即看到页面上的内容并执行操作，而不必等待特定事件触发。

这一特性的最大优势在于速度，因为您可以像人一样看到什么就可以操作什么。这样的交互方式使得 Luna 极为高效。

## 3. 代理 IP 多样性

Luna 支持市面上所有类型的代理 IP，包括 HTTP、HTTPS 和 SOCKS5，无论代理 IP 是否需要密码，Luna 都完全兼容。理论上，使用 Luna 进行爬取的请求将无法被追踪。

## 4. 多进程和多线程

Luna 考虑到了多进程和多线程的应用场景，使得您可以并发执行多个任务，提高了爬虫的效率。

## 5. 网络数据包过滤

Luna 考虑到了、可能会协议和浏览器混编的方式、和可能的协议采集需求,所以继承了比较完备的cookie方案，和数据包过滤方案、方便采集数据使用、已经封装了比较完善的 一对一 请求过滤。




- 另外、鼠标移动轨迹、键盘输入、鼠标滚轮、如果没有luna浏览器配合、那么依然会被轻易识别。


如果您有技术方便问题、或者bug反馈、欢迎反馈!

----------------------



代码调用抗指纹部分示例，最好您参考文档里面的详细内容，这里仅黏贴一部分代码，提供参考。

## 

```bash
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

```


#### 常见问题回复

1、可以自己随便修改指纹吗？

答：是的

2、目前支持Linux 系统 or 苹果m1,m2芯片吗？

答:暂时不支持、

3、有http协议版本吗？

答：有

4、有体积更小的浏览器么？

答：无、本身就是抗指纹的，如果精简版 不利于抗指纹。

5、为什么我测试基于视觉时候发现，出现bug

答：下载代码后不要修我的项目名字

6、第三封库可以用的么，如Selenium Pyppeteer Playwright 。

答：可以，但是强烈不建议，因为这样基本上等于阉割了抗指纹的部分核心功能。

7、我没有找到如何类似xpath cssselecter选择器。

答：参考如下代码

```
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
    chromiumPath = "/Chromium.app/Contents/MacOS/Chromium"
    CachePath = "/golang/cache/"
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

```

8、如何操作cookie、文档中我并没有找到

答：参考如下代码

```
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

```



更多案例：直接参考源码的case包里面案例;<非付费用户，只能测试useragent 部分效果> 如需授权 联系作者QQ: 80258153

