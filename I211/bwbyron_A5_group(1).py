#Assignment 5, Group Work(1/2): New York Times RSS Feed
#Brett Byron; Group 1

import urllib, xml.etree.ElementTree as ET

#Main
conn = urllib.urlopen("http://feeds.nytimes.com/nyt/rss/World")
lines = conn.read()
conn.close()

root = ET.XML(lines)

items = root.findall("channel/item")

###Part A
##for elem in items:
##    print "\n" + elem.find("title").text + ": " + "( " + \
##          elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##          " )"

###Part B
##namespaces = ['http://www.nytimes.com/namespaces/keywords/nyt_geo', 'http://www.nytimes.com/namespaces/keywords/nyt_org_all']
##for elem in items:
##    regions = ", ".join([item.text for item in elem.findall("category") if item.items()[0][1] in namespaces])
##    if "sinosphere" in elem.find("title").text.lower():
##        print "\nChina: " + elem.find("title").text + ": " + \
##              elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##              " )"
##    else:
##        print "\n" + regions + ": " + elem.find("title").text + ": " + \
##              elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##              " )"

###Part C
##namespaces = ['http://www.nytimes.com/namespaces/keywords/nyt_geo', 'http://www.nytimes.com/namespaces/keywords/nyt_org_all']
##for elem in items:
##    regions = ", ".join([item.text for item in elem.findall("category") if item.items()[0][1] in namespaces])
##    if "sinosphere" in elem.find("title").text.lower():
##        print "\nChina: " + elem.find("title").text + ": " + \
##              elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##              " )"
##    else:
##        print "\n" + regions + ": " + elem.find("title").text + ": " + \
##              elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##              " )"
##    print "Link: \n" + elem.find("link").text

###Part D
##found = False
##keyword = raw_input("Please enter a category to search for: ")
##namespaces = ['http://www.nytimes.com/namespaces/keywords/nyt_geo', 'http://www.nytimes.com/namespaces/keywords/nyt_org_all']
##for elem in items:
##    for each in elem:
##        if each.text != None:
##            if keyword.lower() in each.text.lower():
##                regions = ", ".join([item.text for item in elem.findall("category") if item.items()[0][1] in namespaces])
##                if "sinosphere" in elem.find("title").text.lower():
##                    print "\nChina: " + elem.find("title").text + ": " + \
##                          elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##                          " )"
##                else:
##                    print "\n" + regions + ": " + elem.find("title").text + ": " + \
##                          elem.find("{http://purl.org/dc/elements/1.1/}creator").text + \
##                          " )"
##                print "Link: \n" + elem.find("link").text
##                found = True
##            else:
##                found = False
##if not found:
##    print "No matches found."
    
