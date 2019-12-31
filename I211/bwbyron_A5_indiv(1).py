#Assignment 5, individual(1/2): CD Catalog
#Brett Byron, Group 1

import xml.etree.ElementTree as ET

#Variables
price_all = 0   #Sum of each CD price
price_min = 0   #Minimum CD price
price_max = 0   #Maximum CD price
price_avg = 0   #Average CD price

root = ET.parse(source="cd_catalog.xml")

#Total # of CDs
cd_count = root.findall("CD")
cd_count = len(cd_count)

#Sum CD price
price_all = sum([float(each.text) for each in root.findall("CD/PRICE")])

#Minimum CD price
price_min = min([float(each.text) for each in root.findall("CD/PRICE")])

#Maximum CD price
price_max = max([float(each.text) for each in root.findall("CD/PRICE")])

#Average CD price
price_avg = price_all/cd_count

#All American artists
american = [elem.find("ARTIST").text for elem in root.findall("CD") if elem.find("COUNTRY").text == "USA"]

#Printing
print "Total # of CDs:", cd_count
print "Sum of all prices:", price_all
print "Minimum CD price:", price_min
print "Maximum CD price:", price_max
print "Average CD price:", price_avg
print "American Artists:"
for artist in american:
    print "\t" + artist
