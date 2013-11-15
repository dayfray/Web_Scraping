# web scrapeer for stock prices

import urllib
import re

symbol_file = open("symbols.txt")

symbols_list = symbol_file.read()

new_symbols_list = symbols_list.split("\n")



i = 0


while i < len(new_symbols_list):

    urls = "http://finance.yahoo.com/q?s=" + new_symbols_list[i]
    html_file = urllib.urlopen(urls)
    html_text = html_file.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, html_text)

    print "The price of " , new_symbols_list[i] , " is " , price
    i += 1

