import os
import sys
import webbrowser


def get_base_path():
    return sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.abspath(".")


# 此处必须注意，绑定的事件函数中必须要包含event参数
def open_url(event):
    webbrowser.open("https://github.com/bzsome", new=0)


# 获得显示长度，中文占2位
def get_show_len(txt):
    len_txt = len(txt)
    len_txt_utf8 = len(txt.encode('utf-8'))
    return int((len_txt_utf8 - len_txt) / 2 + len_txt)


# 获得要显示的字符串
# start 显示长度起始位置
# end 显示长度结束位置
def get_show_txt(txt, show_start, show_end):
    def get_show_index(txt, i_len):
        res_txt = ''
        for index, char in enumerate(txt):
            res_txt = res_txt + char
            res_show_len = get_show_len(res_txt)
            if (res_show_len > i_len):
                return index
        return get_show_len(txt)

    i_start = get_show_index(txt, show_start)
    i_end = get_show_index(txt, show_end)

    return txt[i_start:i_end]
