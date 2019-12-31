#Midterm: Faculty Research Area Finder
#Brett Byron, Group 1

    #####################
    ##### Section 3 #####
    #####################


import urllib, re

#URL
#http://www.soic.indiana.edu/people/faculty.shtml


#Get faculty links
def link_list(url):
    profiles = []
    names = []

    #Get webpage contents
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid URL."
    else:
        content = web_page.read()
        web_page.close()


        #Get profile links
        links = [item for item in re.findall('<td><h3><a href="profiles/[\w.-]+.shtml">', content)]

        for link in links:
            #Get names using each link as a starting point
            titles = re.findall(link+'[\w\s./-]+</a>', content)
            for name in titles:
                name = name.replace(link, '')
                name = name.replace('</a>', '')
                if len(name.split()) == 3:
                    first, middle, last = name.split()
                    first = str(first)+" "+str(middle)
                if len(name.split()) == 2:
                    first, last = name.split()
                names.append((" "+last, first))
            link = link.replace('<td><h3><a href="', "http://www.soic.indiana.edu/people/")
            link = link.replace('">', "")
            profiles.append(link)

        #Return list of names, and profile links
        return profiles, names


#Find research area
def find_research(url, area):
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


        #Get links to research areas
        links = [item for item in re.findall('<a href="../../research[\w./-]+.shtml">', content)]

        #Get research area text
        for link in links:
            research_area = re.findall(link+'[\w\s./-]+</a>', content)
            for areas in research_area:
                areas = areas.replace(link, '')
                areas = areas.replace('</a>', '')
                research.append(areas)

        #Attempt to find research area in area's obtained from webpage.
        for each in research:
            #.title() in case of user error
            if area.title() == each:
                flag = True

        #Return found flag
        return flag

######################
######## Main ########
######################

#All profile links with research area
profiles = []
matches = []

#Get url from user
url = raw_input("What is the url to the faculty page? ")

#Get all profile links and corresponding names
links, names = link_list(url)

#Add links and names to profiles list
for i in range(len(links)):
    profiles.append([names[i], links[i]])

#Get research area from user
area = raw_input("Which research area? ")

#Check for research area in each profile
#   Add each profile that has a matching research area listed to profiles list
for i in range(len(links)):
    found = find_research(links[i], area)
    if found:
        matches.append(profiles[i])

#Check if profiles list is empty
if not matches:
    print "No matches found for that research area."
else:
    #Sorted output
    matches.sort()
    for i in range(len(matches)):
        print matches[i][0][1] + matches[i][0][0] + "\t" + matches[i][1]
