#Homework 4, individual: Stocks
#Brett Byron, Group 1

import re, urllib, csv, datetime

#Takes string argument; returns last trade, change,
#   date, open, and previous close.
def getStockData(company):
    url = "http://quote.yahoo.com/d/quotes.csv?s=" + \
          company + \
          "&f=sl1d1t1c1ohgvj1pp2owern&e=.csv"

    #List for last trade, change, date, open, and previous close
    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid webpage."
    else:
        read = csv.reader(web_page)
        #Return indecies corresponding to list above
        row = read.next()
        web_page.close()
        return row[1], row[4], row[2], row[5], row[10]

#Display formatted info
def display(company, lst_trd, change, the_date, opn, prev_cls):
    if change < 0:
        change = change[1:]
        print "The last trade for " + company + " was $" + str(lst_trd) + " and the " \
          + "change was -$" + str(change) + " on " + \
          str(the_date.strftime("%B %d, %Y")) + ". The open was" \
          + " $" + opn + " and the previous close was $" + prev_cls + ".\n"
    else:
        change = change[1:]
        print "The last trade for " + company + " was $" + str(lst_trd) + " and the " \
          + "change was +$" + str(change) + " on " + \
          str(the_date.strftime("%B %d, %Y")) + ". The open was" \
          + " $" + opn + " and the previous close was $" + prev_cls + ".\n"

#Get stock symbols
def get_symbols(url):
    companies = []

    try:
        web_page = urllib.urlopen(url)
    except IOError:
        print "Not a valid URL."
    else:
        lines = web_page.read()
        web_page.close()

        init_companies = [item for item in re.findall('NYSE: [\w.-]{2,4}|Nasdaq: [\w.-]{2,4}', lines)]
        for i in range(len(init_companies)):
            if "NYSE: " in init_companies[i]:
                init_companies[i] = init_companies[i].replace("NYSE: ", "")
            elif "Nasdaq: " in init_companies[i]:
                init_companies[i] = init_companies[i].replace("Nasdaq: ", "")
        for company in init_companies:
            if "." in company:
                company = company.replace(".", "")
                companies.append(company)
            else:
                companies.append(company)
        return companies


#Main
companies = ["GOOG", "CMI", "TDC", "CL", "SWKS", "BIIB", "AKAM", "LECO", "COST",
             "UA"]
for company in companies:
    lst_trd, change, date, opn, prev_cls = getStockData(company)

    #Format Date
    date = re.findall('[/]?[\d]+[/]?', date)
    for i in range(len(date)):
        date[i] = date[i].replace("/", "")
    the_date = datetime.date(int(date[2]), int(date[0]), int(date[1]))


    #Display info
    display(company, lst_trd, change, the_date, opn, prev_cls)

#Bonus section
print "-"*20 + " Bonus " + "-"*20

url = "http://www.fool.com/the-25-best-companies-in-america/index.aspx"
bonus_companies = get_symbols(url)

for company in bonus_companies:
    lst_trd, change, date, opn, prev_cls = getStockData(company)

    #Format Date
    date = re.findall('[/]?[\d]+[/]?', date)
    for i in range(len(date)):
        date[i] = date[i].replace("/", "")
    the_date = datetime.date(int(date[2]), int(date[0]), int(date[1]))


    #Display info
    display(company, lst_trd, change, the_date, opn, prev_cls)
