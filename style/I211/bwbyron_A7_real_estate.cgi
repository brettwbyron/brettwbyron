#! /usr/bin/env python

print 'Content-type: text/html\n'

import cgi, MySQLdb
import cgitb
cgitb.enable()

def open_page(page):
    try:
        web_page = urllib.urlopen(page)
        lines = web_page.read()
        if "404 Page Not Found" in lines:
            print "That page doesn't exist on the server."
        web_page.close()
    except:
        print "Error opening that URL!"
        lines = []

    return lines

#establish DB connection
string = "i211u14_bwbyron"
password = "my+sql=i211u14_bwbyron"
db_con = MySQLdb.connect(host="burrow.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()

choice = form.getfirst('choice', '')
order = form.getfirst('order', '')

print "<html><body>"

if choice == 'showall':
    if order == 'PersonID':
        SQL = "SELECT * FROM Person ORDER BY PersonID;"
    elif order == 'FirstName':
        SQL = "SELECT * FROM Person ORDER BY FirstName;"
    elif order == 'LastName':
        SQL = "SELECT * FROM Person ORDER BY LastName;"
    elif order == 'Birth':
        SQL = "SELECT * FROM Person ORDER BY Birth;"
    elif order == 'Age':
        SQL = "SELECT * FROM Person ORDER BY Age;"
    else:
        SQL = "SELECT * FROM Person;"
    try:
        cursor.execute(SQL)
        results = cursor.fetchall()
    except Exception, e:
        print "<p>Something went wrong with the SQL!</p>"
        print SQL
        print "\nError:", e
    else:
        print "<h1>Acme Real Estate Company</h1>"
        print "<h3>Current Clients</h3>"
        print "<table border='1'>"
        print "<tr>"
        print "<th><a href='bwbyron_A7_real_estate.cgi?choice=showall&order=PersonID'>PersonID</a></th>"
        print "<th><a href='bwbyron_A7_real_estate.cgi?choice=showall&order=FirstName'>FirstName</a></th>"
        print "<th><a href='bwbyron_A7_real_estate.cgi?choice=showall&order=LastName'>LastName</a></th>"
        print "<th><a href='bwbyron_A7_real_estate.cgi?choice=showall&order=Birth'>Birth</a></th>"
        print "<th><a href='bwbyron_A7_real_estate.cgi?choice=showall&order=Age'>Age</a></th>"
        print "<th>Edit</th>"
        print "<th>Delete</th>"
        print "</tr>"
        for row in results:
            print "<tr>"
            for i in range(len(row)+2):
                if i <= 4:
                    print "<td align='center'>", row[i], "</td>"
                elif i == 5:
                    urlbase = "http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=edit&personid="
                    personid = str(row[0])
                    url = urlbase + personid
                    print "<td align='center'><a href='" + url + "'>Edit</a></td>"
                elif i == 6:
                    urlbase = "http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=delete&personid="
                    personid = str(row[0])
                    url = urlbase + personid
                    print "<td align='center'><a href='" + url + "'>Delete</a></td>"
            print "</tr>"
        print "</table>"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.html'>Go Back</a></body></html>"

elif choice == 'showallhouses':
    if order == 'HouseID':
        SQL = "SELECT * FROM House ORDER BY HouseID;"
    elif order == 'City':
        SQL = "SELECT * FROM House ORDER BY City;"
    elif order == 'Value':
        SQL = "SELECT * FROM House ORDER BY Value;"
    elif order == 'Owner':
        SQL = "SELECT * FROM House ORDER BY Owner;"
    else:
        SQL = "SELECT * FROM House;"
    try:
        cursor.execute(SQL)
        results = cursor.fetchall()
    except Exception, e:
        print "<p>Something went wrong with the SQL!</p>"
        print SQL
        print "\nError:", e
    else:
        html = "<h1>Acme Real Estate Company</h1>"
        html += "<h3>%s</h3>"
        html += "<h3>Current Clients</h3>"
        html += "<table border='1'>"
        html += "<tr>"
        html += "<th><a href='bwbyron_A7_real_estate.cgi?choice=showallhouses&order=HouseID'>HouseID</a></th>"
        html += "<th><a href='bwbyron_A7_real_estate.cgi?choice=showallhouses&order=City'>City</a></th>"
        html += "<th><a href='bwbyron_A7_real_estate.cgi?choice=showallhouses&order=Value'>Value</a></th>"
        html += "<th><a href='bwbyron_A7_real_estate.cgi?choice=showallhouses&order=Owner'>Owner</a></th>"
        html += "<th>Edit</th>"
        html += "<th>Delete</th>"
        html += "</tr>"
        invalidname = False
        for row in results:
            html += "<tr>"
            for i in range(len(row)+2):
                SQL = "select concat(FirstName,' ', LastName) FROM Person WHERE PersonID=" + row[3]
                cursor.execute(SQL)
                results2 = cursor.fetchall()
                realname = str(results2).replace('((\'', '').replace('\',),)', '')
                if realname != "()":
                    if i == 2:
                        html += "<td align='center'>$" + str(row[i]) + " </td>"
                    elif i == 3:
                        html += "<td align='center'> " + realname + " </td>"
                    elif i == 4:
                        urlbase = "http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=edithouse&houseid="
                        houseid = str(row[0])
                        url = urlbase + houseid
                        html += "<td align='center'> <a href='" + url + "'>Edit</a> </td>"
                    elif i == 5:
                        urlbase = "http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=deletehouse&houseid="
                        houseid = str(row[0])
                        url = urlbase + houseid
                        html += "<td align='center'> <a href='" + url + "'>Delete</a> </td>"
                    else:
                        html += "<td align='center'>" + str(row[i]) + " </td>"
                else:
                    invalidname = True
                    
        html += "</table>"
        html += "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.html'>Go Back</a></body></html>"
        if invalidname:
            print html % ("<h2>Some Houses have invalid Owner numbers and are not shown.</h2>")
        else:
            print html % ("")
elif choice == 'addperson':
    try:
        SQL = "INSERT INTO Person (FirstName, LastName, Birth, Age)"
        if form.getfirst('age', '') == "":
            SQL += "VALUES('" + form.getfirst('first','') + "','" + form.getfirst('last','') + "','" + form.getfirst('birth', '') + "','" + "18" + "');"
	else:
            SQL += "VALUES('" + form.getfirst('first','') + "','" + form.getfirst('last','') + "','" + form.getfirst('birth', '') + "','" + form.getfirst('age', '') + "');"
        cursor.execute(SQL)
        db_con.commit()
    except Exception, e:
        print "Something went wrong"
        print SQL
        print "\nError:", e
    else:
        print "Person added!"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.html'>Go Back</a></body></html>"
elif choice == 'addhouse':
    try:
        SQL = "INSERT INTO House (City, Value, Owner)"
        SQL += "VALUES('" + form.getfirst('city', '') + "','" + form.getfirst('value', '') + "','" + form.getfirst('owner', '') + "');"
        cursor.execute(SQL)
        db_con.commit()
    except Exception, e:
        print "Something went wrong"
        print SQL
        print "\nError:", e
    else:
        print "House added!"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.html'>Go Back</a></body></html>"
elif choice == 'edit':
    try:
        SQL = "SELECT * FROM Person WHERE PersonID =" + form.getfirst('personid','')
        cursor.execute(SQL)
        results = cursor.fetchall()
    except Exception, e:
        print "Something went wrong"
        print SQL
        print "\nError:", e
    else:
        print "<h1>Acme Real Estate Company</h1>"
        print "<h2>Edit a Client</h2>"
        print "<form action='bwbyron_A7_real_estate.cgi' method='get'>"
        print "<input type='hidden' value='saveedit' name='choice'>"
        print "<input type='hidden' name='personid' value='" + form.getfirst('personid', '') + "'/><br />"
        print "First Name: <input type='text' name='first' value='" + results[0][1] + "'/><br />"
        print "Last Name: <input type='text' name='last' value='" + results[0][2] + "'/><br />"
        print "Birthdate (yyyy-mm-dd): <input type='text' name='birth' value='" + str(results[0][3]) + "'/><br />"
        print "Age: <input type='text' name='age' value='" + str(results[0][4]).replace('L','') + "'/><br />"
        print "<input type='submit' value='Save Changes'><br /></form>"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.html'>Go Back</a></body></html>"
elif choice == 'edithouse':
    try:
        SQL = "SELECT * FROM House WHERE HouseID=" + form.getfirst('houseid', '')
        cursor.execute(SQL)
        results = cursor.fetchall()
    except Exception, e:
        print "Something went wrong"
        print SQL
        print "\nError:", e
    else:
        print "<h1>Acme Real Estate Company</h1>"
        print "<h2>Edit a House</h2>"
        print "<form action='bwbyron_A7_real_estate.cgi' method='get'>"
        print "<input type='hidden' value='savehedit' name='choice'>"
        print "<input type='hidden' name='houseid' value='" + form.getfirst('houseid', '') + "'/><br />"
        print "City: <input type='text' name='city' value='" + str(results[0][1]) + "'/><br />"
        print "Value: <input type='text' name='value' value='" + str(results[0][2]).replace('L', '') + "'/><br />"
        print "Owner: <input type='text' name='owner' value='" + str(results[0][3]) + "'/><br />"
        print "<input type='submit' value='Save Changes'><br /></form>"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.html'>Go Back</a></body></html>" 
elif choice == 'delete':
    print "<h1>Acme Real Estate Company</h1>"
    print "<h2>Deleting a Client</h2>"
    try:
        SQL = "DELETE FROM Person WHERE PersonID = '" + form.getfirst('personid', '')+ "'"
        cursor.execute(SQL)
        db_con.commit()
    except Exception, e:
        print "Something went wrong deleting that record"
        print SQL
        print "\nError:", e
    else:
        print "<p>Delete Succeeded!</p>"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=showall'>Go Back</a></body></html>"

elif choice == 'deletehouse':
    print "<h1>Acme Real Estate Company</h1>"
    print "<h2>Deleting a House</h2>"
    try:
        SQL = "DELETE FROM House WHERE HouseID = '" + form.getfirst('houseid', '') + "'"
        cursor.execute(SQL)
        db_con.commit()
    except Exception, e:
        print "Something went wrong deleting that record"
        print SQL
        print "\nError:", e
    else:
        print "<p>Delete Succeeded!</p>"
        print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=showallhouses'>Go Back</a></body></html>"

elif choice == "saveedit":
    print "<h1>Acme Real Estate Company</h1>"
    print "<h2>Saving Client Changes</h2>"
    try:
        SQL = "DELETE FROM Person WHERE PersonID = '" + form.getfirst('personid', '')+ "'"
        cursor.execute(SQL)
        db_con.commit()
    except Exception, e:
        print "Something went wrong deleting that record"
        print SQL
        print "\nError:", e
    else:
        try:
            SQL = "INSERT INTO Person (FirstName, LastName, Birth, Age)"
            SQL += "VALUES('" + form.getfirst('first','') + "','" + form.getfirst('last','') + "','" + form.getfirst('birth', '') + "','" + form.getfirst('age', '') + "');"
            cursor.execute(SQL)
            db_con.commit()
        except Exception, e:
            print "Something went wrong inserting updated record"
            print SQL
            print "\nError:", e
        else:
            print "Update Succeeded!"
            print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=showall'>Go Back</a></body></html>"

elif choice == "savehedit":
    print "<h1>Acme Real Estate Company</h1>"
    print "<h2>Saving House Changes</h2>"
    try:
        SQL = "DELETE FROM House WHERE HouseID = '" + form.getfirst('houseid', '')+ "'"
        cursor.execute(SQL)
        db_con.commit()
    except Exception, e:
        print "Something went wrong deleting that record"
        print SQL
        print "\nError:", e
    else:
        try:
            SQL = "INSERT INTO House (City, Value, Owner)"
            SQL += "VALUES('" + form.getfirst('city', '') + "','" + form.getfirst('value', '') + "','" + form.getfirst('owner', '') + "');"
            cursor.execute(SQL)
            db_con.commit()
        except Exception, e:
            print "Something went wrong inserting updated record"
            print SQL
            print "\nError:", e
        else:
            print "Update Succeeded!"
            print "<a href='http://cgi.soic.indiana.edu/~bwbyron/bwbyron_A7_real_estate.cgi?choice=showallhouses'>Go Back</a></body></html>"
