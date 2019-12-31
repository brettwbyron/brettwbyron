#Assignment 5, Group Work: Creating XML Files
#Brett Byron; Group 1

import csv, os, xml.etree.ElementTree as ET

#Add class to xml file
def add_xml_class(dept, abbr, num, name, credit, days, seats, building, room):
    root = ET.parse(source="classes.xml")
    elements = root.getiterator()
    class_list = elements[0]

    new_class = ET.SubElement(class_list, "Class")
    department = ET.SubElement(new_class, "department")
    department.text = dept
    department.set("abbr", abbr)
    title = ET.SubElement(new_class, "title")
    class_num = ET.SubElement(title, "number")
    class_num.text = num
    class_name = ET.SubElement(title, "name")
    class_name.text = name
    class_cred = ET.SubElement(new_class, "credits")
    class_cred.text = credit
    class_days = ET.SubElement(new_class, "days")
    class_days.text = days
    class_seats = ET.SubElement(new_class, "class")
    class_seats.set("building", building)
    class_seats.set("room", room)

    root.write("classes.xml")

    print "New class added: " + abbr + " " + num



classes = open(os.path.join(os.getcwd(), "classes.csv"), "r")
read = csv.reader(classes)
read.next()
for row in read:
    abbr, number = row[0].split()
    department = row[1]
    name = row[2]
    credit = row[3]
    days = row[4]
    seats = row[-1]
    building, room = row[5].split()
    add_xml_class(department, abbr, number, name, credit, days, seats, building, room)
