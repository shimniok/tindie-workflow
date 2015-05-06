#!/usr/bin/python

import requests
import locale
import cgitb
import datetime
from Config import Config
import sys
import codecs

# enable debugging
cgitb.enable()

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

url = 'https://www.tindie.com/api/v1/order/?format=json&shipped=false'
c = Config()

print("Content-Type: text/html\r\n\r\n")
print

try:
    r = requests.get(url+'&username='+c.user+'&api_key='+c.key)
except requests.exceptions.ConnectionError:
    print("<html><head/><body>ConnectionError</body></html>")
else:
    data = r.json()
    count = data['meta']['total_count']
    orders = data['orders']

    print('<head><LINK href="tindie.css" rel="stylesheet" type="text/css"></head><body>')

    print("<table><thead><tr>")
    print("<th class=\"center\">Order</th>")
    print("<th class=\"center\">Status</th>")
    print("<th class=\"center\">Date</th>")
    print("<th class=\"left\">Email</th>")
    print("<th class=\"left\">Name</th>")
    print("<th class=\"center\">Postage</th>")
    print("<th class=\"center\">Slip</th>")

    with open('hide.txt', 'r') as f:
        hide_list = f.read().splitlines()

    count = 0

    for o in orders:

        if str(o['number']) in hide_list:
            continue

        paid = "PAID"
        for i in o['items']:
            if i['status'] == 'pending':
                paid = "PENDING"
                break

        print("<tr>")
        print("<td class=\"center\"><a href=\"https://www.tindie.com/orders/{0}/\" target=\"_blank\">{0}</a></td>".format(o['number']))
        d = datetime.datetime.strptime(o["date"], "%Y-%m-%dT%H:%M:%S.%f")
        print("<td class=\"center\">{0}</td>".format(paid))
        print("<td class=\"center\">{0}</td>".format(d.strftime('%b %d, %Y %H:%M')))
        print("<td class=\"left\"><a href=\"mailto:{0}?subject=Tindie%20Order%20#{1}\">{0}</a>".format(o['email'], o['number']))
        name = o['shipping_name'].encode('utf-8')
        print("<td class=\"left\">{0}</td>".format(name[:20] + (name[20:] and '..')))
        print("<td class=\"center\"><a href=\"dazzle.py?order={0}\" target=\"_blank\">postage</a>".format(o['number']))
        print("<td class=\"center\"><a href=\"slip.py?order={0}\" target=\"_blank\">packing slip</a>".format(o['number']))
        print("</tr>")

        count += 1

    print("</tbody></table>")

    if count == 0:
        print("List is empty.<br/>")

    print("<br/>")
    print("<a href='{0}&username={1}&api_key={2}'>Link to JSON data</a>".format(url, c.user, c.key))
    print("</body>")
    print("</html>")
