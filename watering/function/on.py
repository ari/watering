#!/usr/bin/python2.7

import subprocess
import cgi

print "Content-type: text/html"
print

cmd = ['sudo', '/usr/bin/python2.7', '/var/www/localhost/htdocs/watering/function/water.py']

proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in proc.stdout:
    print "<p>" + line + "<p/>"
