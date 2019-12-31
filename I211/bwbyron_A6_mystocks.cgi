#! /usr/bin/env python
print 'Content-type: text/html\n'

import cgi, urllib, csv, cgitb

cgitb.enable()

html = """
<html>
    <head><title>Find Stock Info</title></head>
    <body>
"""

form = cgi.FieldStorage()

#I'm changing the string following the '&f' to have the .csv value return the only the values
#	required for this assignment.

#You can find the list of special tags and their meaning that the string following the '&f'
#	at the following link. http://www.jarloo.com/yahoo_finance/

#I will be using:
#	s	= Symbol
#	l1 	= Last Trade (Price Only)
#	c1 	= Change
#	v 	= Volume
#	a2 	= Average Daily Volume

#The following link shows the new &f string I will be using.
#http://quoate.yahoo.com/d/quotes.csv?s=GOOG&f=sl1c1va2&e=.csv

symbols = form['symbols'].value.split()

if len(symbols) != 0:
	html += '<table border="1" style="table-layout:fixed; width:400px;">'
	html += "<tr>"
	html += "<th>Name</th>"
	html += "<th>Price</th>"
	html += "<th>Change</th>"
	html += "<th>Volume</th>"
	html += "<th>Avg. Daily Volume</th>"
	html += "</tr>"

	for symbol in symbols:
		url = "http://quote.yahoo.com/d/quotes.csv?"
		s = "s=" + symbol
		f = "&f=sl1c1va2"
		e = "&e=.csv"
		
		url = url + s + f + e
		
		try:
			web_page = urllib.urlopen(url)
		except IOError:
			html += "Invalid URL</body></html>"
			print html
			break
		else:
			read = csv.reader(web_page)
			row = read.next()
			web_page.close()

			# html += str(row)

			if row[2] == "N/A" or float(row[2]) == 0.0:
				html += '<tr align="center">'
				html += "<td>" + row[0] + "</td>"
				html += '<td colspan="4">No stocks given.</td>'
				html += "</tr>"
				continue
			elif row[2][0] == '-':
				html += '<tr style="color:red" align="center">'
			elif row[2][0] == '+':
				html += '<tr style="color:green" align="center">'

			html += "<td>" + str(row[0]) + "</td>"
			html += "<td>" + str(row[1]) + "</td>"
			html += "<td>" + str(row[2]) + "</td>"
			html += "<td>" + str(row[3]) + "</td>"
			html += "<td>" + str(row[4]) + "</td>"
			html += "</tr>"

	html += "</table>"

else:
	html += "No stocks entered."
print html + "</body></html>"


