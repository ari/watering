# Automated watering system

Watering system for Raspberry Pi

This simple project has been watering my garden for several years. The hardware is simple enough:

1. Raspberry Pi (any model should be fine)
2. USB Relay Module Board
3. Solenoid
4. Power supply for solenoid
 
## Hardware setup

Get the Raspberry Pi working and connected to the internet. We'll need that internet connection later to get weather data from the bureau of metereology.

Connect the USB relay board to the Raspberry Pi.

Install all the software bits. You can trigger the on.py and off.py by hand (they are just scripts you can execute) and test that the relay is triggered.

Connect the relay output to your solenoid in your garden. The solenoid I got required a 24V power supply capable of 250mA which was a little uncommon, but I found one on eBay.


## Configuring the software

I set up the system to provide a simple user interface through a web page. I can then click a link and the watering system turns on. Because I have VPN access, I could in theory do this from anywhere on earth. Use watering.conf as a guide for configuring a virtual host in Apache httpd.

The contents of *watering* then goes into /var/www/localhost/htdocs/watering/function

I also added the following lines to /etc/crontab

    0 22 * * *      root    /var/www/localhost/htdocs/watering/function/on.py

    # an extra watering run in summer
    0 15 * 11,12,1,2 *      root    /var/www/localhost/htdocs/watering/function/on.py
    
This gives me a watering at 10pm every day and another at 3pm but only in November to February when the weather is hottest.

If you aren't in Sydney, you'll also want to adjust the script to pull data from wherever you want to get weather data from. You may also want to tweak my settings for how much the temperature and rainful adjust the watering cycle.
