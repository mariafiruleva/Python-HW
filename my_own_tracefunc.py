import sys


def tracefunc(frame, event):
    if event == "return":
        print("function:", frame.f_code.co_name, ", local vars:", [*frame.f_locals])
    return tracefunc
