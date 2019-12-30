#! /usr/bin/env python

print 'Content-type: text/html\n'

import MySQLdb, cgi, cgitb, xml.etree.ElementTree as ET
cgitb.enable()

#establish DB connection
string = "i211u14_bwbyron"
password = "my+sql=i211u14_bwbyron"
db_con = MySQLdb.connect(host="burrow.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

#xml
#Get plant info
root = ET.parse(source="plant_catalog.xml")
plants = root.findall("PLANT")
plant_info = []
for plant in plants:
    deets = []
    for details in plant:
        if details.tag == "COMMON":
            if "'" in details.text:
                details.text = details.text.replace("'", "&#39")
        deets.append(details.text)
    plant_info.append(deets)

#Page start
try:    #Create Plant table
    SQL = "CREATE TABLE Plant ("
    SQL += "PlantID int(11) UNIQUE AUTO_INCREMENT, "
    SQL += "Common varchar(25) NOT NULL, "
    SQL += "Image varchar(300) NOT NULL, "
    SQL += "Botanical varchar(25) NOT NULL, "
    SQL += "Zone varchar(10) NOT NULL, "
    SQL += "Light varchar(25) NOT NULL, "
    SQL += "Price varchar(25) NOT NULL, "
    SQL += "Availability int(11) NOT NULL);"
    cursor.execute(SQL)
    db_con.commit()
except Exception:		#Here we handle the error
    SQL = "DROP TABLE Plant;"
    cursor.execute(SQL)
    db_con.commit()
    SQL = "CREATE TABLE Plant ("
    SQL += "PlantID int(11) UNIQUE AUTO_INCREMENT, "
    SQL += "Common varchar(25) NOT NULL, "
    SQL += "Image varchar(300) NOT NULL, "
    SQL += "Botanical varchar(25) NOT NULL, "
    SQL += "Zone varchar(10) NOT NULL, "
    SQL += "Light varchar(25) NOT NULL, "
    SQL += "Price varchar(25) NOT NULL, "
    SQL += "Availability int(11) NOT NULL);"
    cursor.execute(SQL)
    db_con.commit()

#HTML
#Add form to page
html = "<html><body>"
html += '<div align="center">'
html += '<h1>Plant data loaded from <a href="plant_catalog.xml">plant_catalog.xml</a><br></h1>'
html += '<h2>Click on a Header to sort by that column!</h2>'
html += '<form action="PlantDB.cgi" method="get">'
html += '<input type="hidden" name="sort" value="PlantID">'
html += 'Common: <input type="text" name="common" /><br />'
html += 'Botanical: <input type="text" name="botanical" /><br />'
html += 'Zone: <input type="text" name="zone" /><br />'
html += 'Light: <input type="text" name="light" /><br />'
html += '<input type="submit" value="Search">&nbsp;&nbsp;&nbsp;&nbsp;'
html += '<input type="reset" value="Reset All Fields"><br />'
html += '</form>'
html += '</div>'
print html

form = cgi.FieldStorage() 

common = form.getfirst('common', '')
botanical = form.getfirst('botanical', '')
zone = form.getfirst('zone', '')
light = form.getfirst('light', '')

#If user enters text into search forms and submits
if common or botanical or zone or light:
    search = True

sort = form.getfirst('sort', 'PlantID')

try:    #insert plant info into db
    SQL = "DELETE FROM Plant;"
    cursor.execute(SQL)
    db_con.commit()

    for plant in plant_info:
        SQL = "INSERT INTO Plant "
        SQL += "(Common, Image, Botanical, Zone, Light, Price, Availability)"
        SQL += "VALUES('" + plant[0] + "','View Images','" + plant[1] + "','"
        SQL += plant[2] + "','" + plant[3] + "','" + plant[4] + "','" + plant[5] + "');"
        cursor.execute(SQL)
        db_con.commit()
    if sort == 'PlantID':
        SQL = "SELECT * FROM Plant ORDER BY PlantID;"
    elif sort == 'Common':
        SQL = "SELECT * FROM Plant ORDER BY Common;"
    elif sort == 'Botanical':
        SQL = "SELECT * FROM Plant ORDER BY Botanical;"
    elif sort == 'Zone':
        SQL = "SELECT * FROM Plant ORDER BY Zone;"
    elif sort == 'Light':
        SQL = "SELECT * FROM Plant ORDER BY Light;"
    elif sort == 'Price':
        SQL = "SELECT * FROM Plant ORDER BY Price;"
    elif sort == 'Availability':
        SQL = "SELECT * FROM Plant ORDER BY Availability;"
    else:
        SQL = "SELECT * FROM Plant;"
    cursor.execute(SQL)
    results = cursor.fetchall()
except Exception, e:
    print "<p>Something went wrong while inserting into db from xml.</p>"
    print SQL, "Error:", e
else:
    #Display plant table
    html = "<html><body><table border='1' width='100%'>"
    html += "<tr>"
    html += "<th><a href='PlantDB.cgi?sort=PlantID'>PlantID</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Common'>Common</a></th>"
    html += "<th>Image</th>"
    html += "<th><a href='PlantDB.cgi?sort=Botanical'>Botanical</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Zone'>Zone</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Light'>Light</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Price'>Price</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Availability'>Availability</a></th>"
    html += "</tr>"

    for row in results:
        html += "<tr>"
        for i in range(len(row)):
            if i == 2:
                html += "<td align='center'><a href='https://www.google.com/search?q=" + row[i+1].replace(' ', '+') + "&tbm=isch'>" + row[i] + "</a></td>"
            else:
                html += "<td align='center'>" + str(row[i]) + "</td>"
        html += "</tr>"
        
    html += "</table></body></html>"

if common or botanical or zone or light:
    SQL = "SELECT * FROM Plant WHERE "
    SQL += "Common like '%" + common + "%'"
    SQL += "and Botanical like '%" + botanical + "%'"
    SQL += "and Zone like '%" + zone + "%'"
    SQL += "and Light like '%" + light + "%' ORDER BY " + sort + ";"
    cursor.execute(SQL)
    results = cursor.fetchall()

    #Display plant table
    html = "<html><body>"
    html += "<a href='PlantDB.cgi'>Clear Search</a><br /><br />"
    html += "<table border='1' width='100%'>"
    html += "<tr>"
    html += "<th><a href='PlantDB.cgi?sort=PlantID'>PlantID</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Common'>Common</a></th>"
    html += "<th>Image</th>"
    html += "<th><a href='PlantDB.cgi?sort=Botanical'>Botanical</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Zone'>Zone</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Light'>Light</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Price'>Price</a></th>"
    html += "<th><a href='PlantDB.cgi?sort=Availability'>Availability</a></th>"
    html += "</tr>"

    for row in results:
        html += "<tr>"
        for i in range(len(row)):
            if i == 2:
                html += "<td align='center'><a href='https://www.google.com/search?q=" + row[i+1].replace(' ', '+') + "&tbm=isch'>" + row[i] + "</a></td>"
            else:
                html += "<td align='center'>" + str(row[i]) + "</td>"
        html += "</tr>"
        
    html += "</table></body></html>"

print html
