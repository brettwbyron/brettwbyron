#Homework 4, Group Work: Pt. 1.2, Earthquakes
#Brett Byron, Group 1

#URL ALL
#http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv

import urllib, csv, datetime


def earthquakeInfo(src, mag):
    total = 0
    total_yesterday = 0
    total_origin = 0
    total_mag = 0

    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv"

    #Get csv info
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid webpage."
    else:
        read = csv.reader(web_page)
        row = read.next()

        yesterday = datetime.date.today() - datetime.timedelta(1)

        for row in read:
            #Total earthquakes
            total += 1

            #Check for earthquake yesterday
            year, month, day = row[0][:4], row[0][5:7], row[0][8:10]
            record_date = datetime.date(int(year), int(month), int(day))
            if record_date == yesterday:
                total_yesterday += 1

            #Check for earthquake from source
            if src == row[10]:
                total_origin += 1

            #Check for earthquake from magnitude
            if mag == row[4]:
                total_mag += 1

        web_page.close()
        return total, total_yesterday, total_origin


#Main
src = "ak"
mag = "3"
total, total_yesterday, total_origin = earthquakeInfo(src, mag)
print "Today's date: " + str(datetime.date.today())
print "Total number of magnitude " + mag + " Earthquakes past 7 days: " + str(total)
print "Earthquakes with magnitude " + mag + " yesterday " + str(datetime.date.today() - datetime.timedelta(1)) + ": " + str(total_yesterday)
print "Earthquakes with magnitude " + mag + " and source " + str(src) + ": " + str(total_origin)
