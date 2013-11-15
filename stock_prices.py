# web scrapeer for stock prices

import urllib
import re

symbols_list = ["aapl", "spy", "good", "nflx"]

i = 0


while i < len(symbols_list):

    urls = "http://finance.yahoo.com/q?s=" + symbols_list[i]
    html_file = urllib.urlopen(urls)
    html_text = html_file.read()
    regex = '<span id="yfs_l84_' + symbols_list[i] + '">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, html_text)

    print "The price of " , symbols_list[i] , " is " , price
    i += 1

