#!/usr/bin/python

import requests
import locale
import cgitb
import datetime

# enable debugging
cgitb.enable()

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

url = 'https://www.tindie.com/api/v1/order/?format=json&shipped=false'
user = 'bot_thoughts'
key = '6d0dd255f06d4f28d36cdda4f899b78c04b34536'
r = ''

print("Content-Type: text/html\r\n\r\n")
print

try:
    r = requests.get(url+'&username='+user+'&api_key='+key)
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

    for o in orders:
        paid = "PAID"
        for i in o['items']:
            if i['status'] == 'pending':
                paid = "PENDING"
                break

        print("<tr>")
        print("<td class=\"center\"><a href=\"https://www.tindie.com/orders/{0}/\">{0}</a></td>".format(o['number']))
        d = datetime.datetime.strptime(o["date"], "%Y-%m-%dT%H:%M:%S.%f")
        print("<td class=\"center\">{0}</td>".format(paid))
        print("<td class=\"center\">{0}</td>".format(d.strftime('%b %d, %Y %H:%M')))
        print("<td class=\"left\"><a href=\"mailto:{0}?subject=Tindie%20Order%20#{1}\">{0}</a>".format(o['email'], o['number']))
        name = o['shipping_name']
        print("<td class=\"left\">{0}</td>".format(name[:20] + (name[20:] and '..')))
        print("<td class=\"center\"><a href=\"dazzle.py?order={0}\" target=\"_blank\">postage</a>".format(o['number']))
        print("<td class=\"center\"><a href=\"slip.py?order={0}\" target=\"_blank\">packing slip</a>".format(o['number']))
        print("</tr>")

    print("</tbody></table>")
    print("<br/>")
    print("<a href='{0}&username={1}&api_key={2}'>Link to JSON data</a>".format(url, user, key))
    print("</body>")
    print("</html>")