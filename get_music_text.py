#!/usr/bin/python3.5
import urllib.request, re, sys
from bs4 import BeautifulSoup
if len(sys.argv)-1 < 1:
    name = input ("enter a music name: ")
else :
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
div = soup.findAll("div", {"class": "mylink-more"})
if len(div) == 0:
    print ("not found!!")
    exit()

match = re.search('<a +href="(.+?)" *>', str(div))
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
