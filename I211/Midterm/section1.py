#Midterm: Link List
#Brett Byron, Group 1

    #####################
    ##### Section 1 #####
    #####################

import urllib, re

#URL
#http://www.soic.indiana.edu/people/faculty.shtml

def link_list(url):
    profiles = []

    #Get webpage contents
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid URL."
    else:
        content = web_page.read()
        web_page.close()

        links = [item for item in re.findall('<td><h3><a href="profiles/[\w.-]+.shtml">', content)]

        for link in links:
            link = link.replace('<td><h3><a href="', "http://www.soic.indiana.edu/people/")
            link = link.replace('">', "")
            profiles.append(link)

        for each in profiles:
            print each

#Main
#url = "http://www.soic.indiana.edu/people/faculty.shtml"
url = raw_input("What is the url to the faculty page? ")
link_list(url)
    
