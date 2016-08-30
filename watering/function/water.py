#!/usr/bin/python
import json
import urllib
import time, sys, getopt, subprocess
from decimal import *
from simpleusbrelay import simpleusbrelay

def main(argv):
   # set all decimal math to 4 sig fig
   getcontext().prec = 4

   try:
      opts, args = getopt.getopt(argv,"o",["off"])
   except getopt.GetoptError:
      print "water.py [-o]"
      sys.exit(2)

   for opt, arg in opts:
      if opt == "-o":
         print "Turning everything off."
         off('all')
         sys.exit()


   # Base duration in minutes
   duration = Decimal(10)
   bom_url = "http://www.bom.gov.au/fwo/IDN60901/IDN60901.94768.json"

   # Fetch the rainfall measurement
   weather_json = json.loads ( urllib.urlopen(bom_url).read() )

   # rain since 9am
   rainfall = Decimal(weather_json["observations"]["data"][0]["rain_trace"])
   temperature = 0 + Decimal(weather_json["observations"]["data"][0]["air_temp"])

   print "%smm of rain fell since 9am." % rainfall
   print "It is %s degrees Celsius now." % temperature

   # Reduce watering duration by 2 minutes for every mm of rain
   duration = duration - ( rainfall * 2 )

   # And reduce it if it is cold
   if temperature < 20:
       duration = duration - ( 20 - temperature)/2

   if duration < 5:
       print "Watering will not run today."

   else:
       print "Watering will run for %s minutes." % duration

       on(1)
       on(2)

       cmd = 'echo "/usr/bin/python2.7 /var/www/localhost/htdocs/watering/function/off.py" | at now + ' + str(int(duration)) + ' minutes'
       proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


# Turn off one of the relays
def off(relay):
   relaycontroller = simpleusbrelay(Vendor = 0x16c0, Product = 0x05df)
   relaycontroller.array_off(relay)

# Turn on one of the relays
def on(relay):
   relaycontroller = simpleusbrelay(Vendor = 0x16c0, Product = 0x05df)
   relaycontroller.array_on(relay)


if __name__ == "__main__":
   main(sys.argv[1:])
