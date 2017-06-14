#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test_urllib.py
#
# Vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# Python source code - replace this with a description
# of the code and write the code below this text
#

def main(args):
    url = "https://www.baidu.com"
    print("第一种方法")
    response1 = urlopen(url)
    print(response1.getcode())
    print(len(response1.read()))

    print("第二种方法")
    request = Request(url)
    request.add_header("user-agent", "Mozilla/5.0")
    response2 = urlopen(request)
    print(response2.getcode())
    print(len(response2.read()))

    print("第三种方法")
    cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj))
    install_opener(opener)
    response3 = urlopen(url)
    print(response3.getcode())
    print("=======================")
    print(cj)
    print("=======================")
    print(response3.read())
if __name__ == '__main__':
    import sys
    from urllib.request import urlopen, Request, install_opener, build_opener, HTTPCookieProcessor
    from http.cookiejar import CookieJar
    sys.exit(main(sys.argv))
