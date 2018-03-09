#!/usr/bin/python

import sys
import re
import urllib2
from bs4 import BeautifulSoup

# Specify our url to scrape data from
scrape_page = 'http://localhost/cgi-bin/tac.cgi'

# Don't get excited.  The uid/psswd are the defaults ;-)
uid = 'nagiosadmin'
psswd = 'nagios'

# Handle authentication
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, scrape_page, uid, psswd)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

# Dump page contents into variable (page)
page = urllib2.urlopen(scrape_page)

# Parse page data with BeautifulSoup and put in to soup object
soup = BeautifulSoup (page, 'html.parser')

# Find hostHeader, serviceHeader and healthBar data of interest in soup object
host_status = soup.find_all('td', attrs={'class' : 'hostHeader'})
service_status = soup.find_all('td', attrs={'class' : 'serviceHeader'})
health_status = soup.find_all('td', attrs={'class' : 'healthBar'})

# Copy array indices into individual arrays for deeper substring searching
# Copy substrings to vars for injection in to chart.js data

#
# hostHeader data #
#
hD = host_status[0].text.strip()
hostDown = hD[0:-5]
hUn = host_status[1].text.strip()
hostUnreachable = hUn[0:-12]
hUp = host_status[2].text.strip()
hostUp = hUp[0:-3]
hP = host_status[3].text.strip()
hostPending = hP[0:-8]

#
# serviceHeader data #
#
sC = service_status[0].text.strip()
svcCritical = sC[0:-9]
sW = service_status[1].text.strip()
svcWarning = sW[0:-8]
sU = service_status[2].text.strip()
svcUnknown = sU[0:-8]
sO = service_status[3].text.strip()
svcOk = sO[0:-3]
sP = service_status[4].text.strip()
svcPending = sP[0:-8]

# Print to console for debugging
# print 'hostDown ', hostDown
# print 'hostUnreachable ',hostUnreachable
# print 'hostUp ',hostUp
# print 'hostPending ',hostPending

# print 'svcCritical ',svcCritical
# print 'svcWarning ',svcWarning
# print 'svcUnknown ',svcUnknown
# print 'svcOK ',svcOk
# print 'svcPending ',svcPending

#
# healthBar data #
#

# regex info
# r is raw string
# alt=" is literal string of alt="
# \d+. is 1 or more decimal digits (0-9) followed by a .
# \d+% is 1 or more decimal digits (0-9) followed by a %
# string[0] & string[1] searched is converted from unicode to raw string format
match = re.search(r'alt="\d+.\d+%', health_status[0].encode('utf-8'))
if match:
    hostHealth = match.group()[5:-1]

    # Print to console for debugging
    # print 'pattern matched is ', match.group()
    # print 'hostHealth is ', hostHealth
else:
    hostHealth = 'ERROR'

    # Print to console for debugging
    # print 'NO MATCH'

match = re.search(r'alt="\d+.\d+%', health_status[1].encode('utf-8'))
if match:
    serviceHealth = match.group()[5:-1]
    # Print to console for debugging
    # print 'pattern matched is ', match.group()
    # print 'serviceHealth ', serviceHealth
else:
    serviceHealth = 'ERROR'
    # Print to console for debugging
    # print 'NO MATCH'

# Create data file with variable definitions for chart.js
f = open('/opt/nagios/share/js/data1.js', 'w')

# hostHeader values
f.write('var hostDown = ')
f.write(hostDown)
f.write(';')
f.write('\n')

f.write('var hostUnreachable = ')
f.write(hostUnreachable)
f.write(';')
f.write('\n')

f.write('var hostUp = ')
f.write(hostUp)
f.write(';')
f.write('\n')

f.write('var hostPending = ')
f.write(hostPending)
f.write(';')
f.write('\n')

f.write('var hostTotal = ')
f.write(hostDown + hostUnreachable + hostUp + hostPending)
f.write(';')
f.write('\n')

# serviceHeader values
f.write('var svcCritical = ')
f.write(svcCritical)
f.write(';')
f.write('\n')

f.write('var svcWarning = ')
f.write(svcWarning)
f.write(';')
f.write('\n')

f.write('var svcUnknown = ')
f.write(svcUnknown)
f.write(';')
f.write('\n')

f.write('var svcOk = ')
f.write(svcOk)
f.write(';')
f.write('\n')

f.write('var svcPending = ')
f.write(svcPending)
f.write(';')
f.write('\n')

f.write('var svcTotal = ')
f.write(svcCritical + svcWarning + svcUnknown + svcOk + svcPending)
f.write(';')
f.write('\n')

# healthBar values
f.write('var hostHealth = ')
f.write(hostHealth)
f.write(';')
f.write('\n')

f.write('var serviceHealth = ')
f.write(serviceHealth)
f.write(';')
f.write('\n')

f.close()
# Send message to "Status Information:" field of TACSCRAPE service
print 'Successfully Ran'
