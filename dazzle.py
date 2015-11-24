#!/usr/bin/python

from __future__ import print_function

import requests
import locale
import cgi
from Config import Config

# enable debugging
#cgitb.enable()

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Create instance of FieldStorage
form = cgi.FieldStorage()

url = 'https://www.tindie.com/api/v1/order/?format=json'
c = Config()
r = ''

print("Content-Type: text/html\r\n\r\n")
print()
print("<html><head></head><body><frameset>")

if form.getvalue('order'):
    all = False
else:
    all = True

try:
    r = requests.get(url + '&username=' + c.user + '&api_key=' + c.key)
except requests.exceptions.ConnectionError as e:
    print("ConnectionError: %s" % e)
else:
    data = r.json()
    count = data['meta']['total_count']
    orders = data['orders']

    for o in orders:

        if all or form.getvalue('order') == str(o['number']):

            paid = True
            for i in o['items']:
                if o.get('status', '') == 'pending':
                    paid = False
                    break

            if paid:
                if o['shipping_country'] != 'United States':
                    print("INTERNATIONAL: %s" % o['shipping_country'])
                else:
                    try:
                        with open("%s/%s.xml" % (c.dir, o['number']), 'w') as f:
                            f.write("<DAZzle>\n")
                            f.write("\t<Prompt>No</Prompt>\n")
                            f.write("\t<Test>YES</Test>\n")
                            f.write("\t<Start>DAZ</Start>\n")
                            f.write("\t<OutputFile>%s-output.xml</OutputFile>\n" % o['number'])
                            f.write("\t<Package>\n")
                            f.write("\t\t<MailClass>FIRST</MailClass>\n")
                            f.write("\t\t<PackageType>RECTPARCEL</PackageType>\n")
                            f.write("\t\t<WeightOz>2.0</WeightOz>\n")
                            f.write("\t\t<Width>6.0</Width>\n")
                            f.write("\t\t<Length>9.0</Length>\n")
                            f.write("\t\t<Depth>1.0</Depth>\n")
                            f.write("\t\t<Stealth>TRUE</Stealth>\n")
                            f.write("\t\t<USPSTracking>ON</USPSTracking>\n")
                            f.write("\t\t<ToName>%s</ToName>\n" % o['shipping_name'])
                            i = 1
                            for a in o['shipping_street'].split('\n'):
                                if a != '':
                                    f.write("\t\t<ToAddress%d>%s</ToAddress%d>\n" % (i, a, i))
                                i += 1
                                if i > 6:
                                    break
                            f.write("\t\t<ToCity>%s</ToCity>\n" % o['shipping_city'])
                            f.write("\t\t<ToState>%s</ToState>\n" % o['shipping_state'])
                            f.write("\t\t<ToPostalCode>%s</ToPostalCode>\n" % o['shipping_postcode'])
                            f.write("\t\t<ToEMail>%s</ToEMail>\n" % o['email'])
                            f.write("\t\t<ReturnAddress1>Bot Thoughts</ReturnAddress1>\n")
                            f.write("\t\t<ReturnAddress2>6557 S Dexter St</ReturnAddress2>\n")
                            f.write("\t\t<ReturnAddress3>Centennial, CO 80121-3220</ReturnAddress3>\n")
                            f.write("\t</Package>\n")
                            f.write("</DAZzle>\n")
                    except IOError as e:
                        print("Error writing file - %s" % e)
                    else:
                        print("<script>window.location.replace(\"https://www.tindie.com/orders/%s/\");</script>" % o['number'])

print("</frameset></body></html>")
