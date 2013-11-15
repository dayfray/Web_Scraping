# web scraper for news site title

import urllib
import re

urls = ["http://lxer.com", "http://macrumors.com", "http://naturalbuildingblog.com"]

i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)


while i < len(urls):
    
    html_file = urllib.urlopen(urls[i])
    html_text = html_file.read()
    titles = re.findall(pattern,html_text)
    print titles
    i += 1
