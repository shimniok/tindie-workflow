Makes use of the tindie.com Orders API and integrates with Endicia DAZzle, creating XML file.

# Installation
Install these files in your web root under directory ```tindie```.
Make sure you have your Design tab set up exactly as you want it ahead of time.
Create an xml file that the web server can write to.
Use the config.template to create a config.txt with user, api key, and directory.

# How To Use

## Print Postage
  
  * Browse to ```/orders.py``` on your web server
  * Click the ```postage``` link to create the DAZzle XML file.
  * From the DAZzle design page, click ```File > Print From > External File...```
  * Select ```Text, XML Format``` from the Files of type combo box to see your XML files
  * Find the XML file with the order # you want to print postage for.
  * Once selected it should print postage for you.
  
## Notify Buyer
  
  * It should also pop up an email to the buyer with the tracking number. Copy this.
  * On the new page, click the order # link, e.g., ```#22492``` to open that order on the Tindie site.
  * On the Tindie site, paste the tracking number into the Tindie site.
  * Click the print button to print the order slip.
