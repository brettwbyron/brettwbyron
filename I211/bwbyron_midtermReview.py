#Midterm Review - Course Listing

import urllib, re, os

#URL
#http://registrar.indiana.edu/browser/soc4148/index.shtml

#Open URL
def get_linkContents(url):
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid URL."
    else:
        contents = web_page.read()
        web_page.close()
        return contents

#Get all departments from URL
def get_departments(url, contents):
    the_links = []
    the_names = []
    the_descripts = []

    print "Searching for departments on: " + url
    links = [item for item in re.findall('<strong><a href="[\w./-]+">', contents)]
    names = [item for item in re.findall('.shtml">[\w]+[-]?[\w]?[-]?[ ]?[\d]?[\d]?[\d]?</a></strong>', contents)]
    descripts = [item for item in re.findall('</a></strong>[\s][\w\s]+[&/-]?[\w\s]+<br', contents)]

    #Get links
    for link in links:
        link = link.replace('<strong><a href="', '')
        link = link.replace('">', '')
        the_links.append(link)

    #Get names
    for name in names:
        name = name.replace('.shtml">', '')
        name = name.replace('</a></strong>', '')
        the_names.append(name)

    #Get descriptions
    for each in descripts:
        each = each.replace('</a></strong> ', '')
        each = each.replace('<br', '')
        the_descripts.append(each)

    while True:
        list_deps = raw_input("List them (Y/N)? ")
        if list_deps.lower() == "y":
            for i in range(len(links)):
                if len(the_links[i]) < 16:
                    print the_names[i] + "\t" + the_links[i] + "\t\t" + the_descripts[i]
                else:
                    print the_names[i] + "\t" + the_links[i] + "\t" + the_descripts[i]
            break
        elif list_deps.lower() == "n":
            break
        else:
            print "You must enter Y or N."


    return the_links, the_names, the_descripts

#Get user's specific department URL
def next_url(url, department):
    baseurl = os.path.basename(url)
    base_index = url.index(baseurl)
    return url[:base_index] + department + "/" + url[base_index:]





##Main##

#Get URL input, and contents
while True:
    url = raw_input("What is the url to the course page? ")
    contents = get_linkContents(url)
    if contents:
        break

links, names, descriptions = get_departments(url, contents)


#Get department, department URL
while True:
    department = raw_input("What department would you like? ")
    if department.upper() not in names:
        print "Not a valid department."
    else:
        #Get department URL, and contents
        dept_url = next_url(url, department)
        break



#Get department contents
while True:
    contents = get_linkContents(dept_url)
    if contents:
        break

links, names, descriptions = get_departments(dept_url, contents)
