#!/usr/bin/python

import requests
import locale
import cgi
import cgitb
import datetime

# enable debugging
cgitb.enable()

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Create instance of FieldStorage 
form = cgi.FieldStorage()

url = 'https://www.tindie.com/api/v1/order/?format=json&shipped=false'
user = 'bot_thoughts'
key = '6d0dd255f06d4f28d36cdda4f899b78c04b34536'
r = ''

print("Content-Type: text/html\r\n\r\n")
print

try:
    r = requests.get(url + '&username=' + user + '&api_key=' + key)
except requests.exceptions.ConnectionError:
    print "<html><head/><body>ConnectionError</body></html>"
else:
    data = r.json()
    count = data['meta']['total_count']
    orders = data['orders']

    #   print("<pre>")
    #   print(json.dumps(data, indent=4))
    #   print("</pre>")

    print('<html><head><LINK href="tindie.css" rel="stylesheet" type="text/css"></head><body>')

    for o in orders:
        if form.getvalue('order') == repr(o['number']):
            print('<div class="header">')
            print('<img class="logo" src="images/BTLogo2.png"/>')
            print('<span><p class="title">Bot Thoughts Order #%d</p>' % (o['number']))
            d = datetime.datetime.strptime(o['date'], '%Y-%m-%dT%H:%M:%S.%f')

        # print('<p class="date">{0}</p>'.format(d.strftime('%A %B %d, %Y %H:%M')))
        # print("</span></div>")

            print('<p class="subtitle">Shipping</p>')
            print('<table class="addr"><thead><tr>')
            print('<th class="left">To Address</th>')
            print('<th class="left">From Address</th>')
            print('</thead><tbody>')
            print('<tr><td>')
            print("{}<br/>".format(o['shipping_name']))
            print("{}<br/>".format(o['shipping_street'].rstrip()))
            print("{}, {} {}<br/>".format(o['shipping_city'], o['shipping_state'], o['shipping_postcode']))
            if o['shipping_country'] != 'United States':
                print("{}<br/>".format(o['shipping_country']))
            print("</td>")
            print("<td>Bot Thoughts<br/>6557 S. Dexter St.<br/>Centennial, CO 80121</td></tr>")
            print("<tr><td><strong>{0}</strong></td><td><strong>mes@bot-thoughts.com</td></tr></strong>".format(o['email']))
            print("</tbody></table>")

            print("<p class=\"subtitle\">Order Items</p>")
            print("<table class=\"items\"><thead><tr>")
            print("<th class=\"left\">Product</th>")
            print("<th class=\"center\">Each</th>")
            print("<th class=\"center\">Qty</th>")
            print("<th class=\"center\">Total</th></tr>")
            print("</thead><tbody>")
            for i in o['items']:
                print("<tr>")
                print("<td class=\"left\">{0}".format(i['product']))
                if i['options'] != '':
                    print("<br/><span class=\"options\">{0}</span></td>".format(i['options']))
                print("<td class=\"center\">{0}</td>".format(locale.currency(i['price_unit'])))
                print("<td class=\"center\">{0}</td>".format(i['quantity']))
                print("<td class=\"center\">{0}</td>".format(locale.currency(i['price_total'])))
                print("</tr>")
            print("<tr><td colspan=3 class=\"right\">Shipping</td><td class=\"center\">{0}</td></tr>".format(locale.currency(o['total_shipping'])))
            print("<tr><td colspan=3 class=\"right\">Discount</td><td class=\"center\">{0}</td></tr>".format(locale.currency(o['total_discount'])))
            print("<tr><td colspan=3 class=\"right\">Total</td><td class=\"center\">{0}</td></tr>".format(locale.currency(o['total_subtotal'])))
            print("</tbody></table>")
            print("<p class=\"subtitle\">Return Policy</p>")
            print("If it doesn't work, I'll replace it, fix it, or refund your money. I'll do whatever I can to make sure you're successful and satisfied.")

        #print '<p class="break" />'
        #print '<div class="fromaddress">'
        #print '<img src="images/BTLogo2.png"/>'
        #print 'Bot Thoughts<br/>6557 S. Dexter St.<br/>Centennial, CO 80121'
        #print '</div>'

        #print '<div class="toaddress">'
        #print o['shipping_name'],"<br/>"
        #print o['shipping_street'].rstrip(),"<br/>"
        #print o['shipping_city']+', '+o['shipping_state']+' '+o['shipping_postcode'],"<br/>"
        #if o['shipping_country'] != 'United States':
        #	print o['shipping_country'],"<br/>"
        #print '</div>'

# print '</body></html>'

