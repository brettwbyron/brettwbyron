import urllib,re, os
from tools import *

def open_page(url):
    web_page = urllib.urlopen(url)
    lines = web_page.read()
    web_page.close()
    return lines

def link_list(lines):
    links = [item.replace('<li><a href="',"").replace('http://www.soic.indiana.edu/undergraduate/courses/',"").split('">') for item in re.findall('<li><a href="[\w.-]+:[\w./-]+">[\w\s.-]+', lines) if 'http://www.soic.indiana.edu/undergraduate/courses/' in item]
    return links

def find_classes(class_list):
    new_list = []
    for item in class_list:
        new_list.append([item[1][:4],item[1][5:]])
    table_print(["Number","Title"],new_list)
    return new_list

def find_class_info(page):
    info = [item.replace('</p><div class="courses">',"").replace("<strong>","").replace("</strong>","").split("<br />") for item in re.findall('Credits:</strong>[\w\W\s]+</p><div class="courses">',page)]     
    return info

##main
soicURL = "http://www.soic.indiana.edu/undergraduate/courses/index.php"
course_links = link_list(open_page(soicURL))
#print course_links


#returns class number and title
print "Here is a list of classes offered by SOIC:\n"
title_list = find_classes(course_links)
#print title_list


#returns credit value and prerequisites of selected course
newURL = ""
while not newURL:
    selected_course = raw_input("Which course would you like more info on? Enter course number:\n")
    for item in course_links:
        if selected_course.upper() == item[1][:4]:
            newURL = soicURL.replace(os.path.basename(soicURL),item[0])
    if not newURL:
        print "Sorry, that is not a valid course name.\n"


course_info = find_class_info(open_page(newURL))
#print course_info


print "-"*25,"\n"
print "Selected course:",selected_course.upper()
for item in title_list:
    if selected_course.upper() == item[0]:
        print "Course Title:",item[1]

for item in course_info:
    for i in range(len(item)):
        print item[i],"\n"
raw_input("\nPlease hit Enter to Exit")
