#!/usr/bin/python3
import urllib.request, re, sys
from bs4 import BeautifulSoup
name = sys.argv
name = str(name[1])
name = name.replace(" ", "%20")

request = urllib.request.Request('http://www.texahang.org/?s='+name)
try:
    response = urllib.request.urlopen(request)
except:
    print("something wrong")

htmlBytes = response.read()
htmlStr = htmlBytes.decode("utf8")

soup = BeautifulSoup(htmlStr, "lxml")
mydivs = soup.findAll("div", {"class": "mylink-more"})
match = re.search('<a +href="(.+?)" *>', str(mydivs))
request = urllib.request.Request(match.group(1))
try:
    response = urllib.request.urlopen(request)
except:
    print("something wrong")

htmlBytes = response.read()
htmlStr = htmlBytes.decode("utf8")
soup = BeautifulSoup(htmlStr, "lxml")
main = soup.findAll("div", {"class": "main-post"})

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

text_main = remove_tags(str(main))
text_main = text_main.replace("]", "")
text_main = text_main.replace("[", "")
print(text_main)
