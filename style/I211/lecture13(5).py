#Lecture 13, New Titles

import urllib, xml.etree.ElementTree as ET


#Main
conn = urllib.urlopen("https://www.iu.edu/~iunews/services/newsrooms/feeds/?format=rss20&id=1232a17b814f4e1c77a8fb801f237996&sort=date")
lines = conn.read()
conn.close()

root = ET.XML(lines)

elements = root.findall("channel/item")

print "Current news items:"
for elem in elements:
    if "2014" in elem.find("pubDate").text:
        print "-"*50
        print "Title: " + elem.find("title").text
        print "Credit: " + elem.find("{http://search.yahoo.com/mrss/}credit").text
        print "Date: " + elem.find("pubDate").text
print "-"*50
