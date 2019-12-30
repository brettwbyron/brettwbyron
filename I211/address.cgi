#! /usr/bin/env python
print 'Content-type: text/html\n'

import cgi

html = """
<html>
    <head><title>Address List</title></head>
    <body>
"""

form = cgi.FieldStorage()

name = form.getfirst('name_input', '')
line1 = form.getfirst('address1', '')
line2 = form.getfirst('address2', '')
city = form.getfirst('city', '')
state = form.getfirst('state', '')
zipcode = form.getfirst('zipcode', '')

if name != '' and line1 != '' and city != '' and state != '' and zipcode != '':
	the_file = open("address.txt", "a+")
	places = the_file.readlines()
	
	new_address = "Name: " + name + "<br>"
	new_address += "Address:<br>" + line1 + " " + line2 + "<br>"
	new_address += city + ", " + state + " " + zipcode + "<hr>"
	places.append(new_address)
	
	the_file.write(new_address)
	the_file.close()
	
	for record in places:
		html += record

	html += "</body></html>"
	print html
else:
	html += "Please fill in all the text boxes."
	html += "</body></html>"
	print html