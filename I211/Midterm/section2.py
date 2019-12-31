#Midterm: Find Research
#Brett Byron, Group 1

    #####################
    ##### Section 2 #####
    #####################

import urllib, re

#URL
#http://www.soic.indiana.edu/people/profiles/duncan-john.shtml

def find_research(url):
    research = []
    flag = False

    #Get webpage contents
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid URL."
    else:
        content = web_page.read()
        web_page.close()

        #Get name of person
        title = re.findall('<title>[\w\s./-]+[:]', content)

        for i in range(len(title)):
            title[i] = title[i].replace('<title>', '')
            title[i] = title[i].replace(':', '')
            name = title[i]

        #Get links to research areas
        links = [item for item in re.findall('<a href="../../research[\w./-]+.shtml">', content)]

        #Get research area text
        for link in links:
            research_area = re.findall(link+'[\w\s./-]+</a>', content)
            for areas in research_area:
                areas = areas.replace(link, '')
                areas = areas.replace('</a>', '')
                research.append(areas)

        #Get research area from user
        area = raw_input("Which research area? ")

        #Attempt to find research area in area's obtained from webpage.
        for each in research:
            #.title() in case of user error
            if area.title() == each:
                flag = True

        return flag, name



#Main
#url = "http://www.soic.indiana.edu/people/faculty.shtml"
url = raw_input("What is the url to the faculty page? ")
found, name = find_research(url)
if found:
    print "Found! " + name + "\t" + url
else:
    print "That faculty member doesn't list that research area."
