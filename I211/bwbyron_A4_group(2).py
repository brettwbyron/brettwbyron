#Assignment 4: Group Work, Pt 2: Wikipedia Images
#Brett Byron: Group 1

import urllib, random, re, os

def get_links(url):
    pages = []
    #Get page info
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid webpage."
    else:
        lines = web_page.read()
        web_page.close()

        links = re.findall('"/wiki/[\w.-]+"', lines)

        for link in links:
            link = link.replace("\"", "")
            pages.append(link.replace('/wiki', 'http://en.wikipedia.org/wiki'))

        return pages

def image_list(url):
    #Get image urls
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid webpage."
    else:
        lines = web_page.read()
        web_page.close()

        img_lines = re.findall('img .*?[alt=""]? src="(.*?)"', lines)
        for each in img_lines:
            each = each.replace("//", "http://")
            if ".png" in each.lower() or ".gif" in each.lower() or ".jpg" in each.lower():
                image = os.path.basename(each)
                print "Saving " + image + " to wiki_pics/"
                urllib.urlretrieve(each, os.path.join(os.getcwd(), "wiki_pics", image))

#Main
url = raw_input("Where would you like to start: ")
while True:
    try:
        jumps = int(raw_input("How many jumps? "))
    except ValueError:
        print "You need to enter a number."
    else:
        break


for i in range(jumps):
    links = get_links(url)
    print "Jumping From: " + url
    image_list(url)
    newURL = random.choice(links)
    print "To: " + newURL
    url = newURL
    print
