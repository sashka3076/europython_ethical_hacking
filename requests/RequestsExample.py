# -*- encoding: utf-8 -*-

import requests, json

print "Requests Library tests."
response = requests.get("https://ep2016.europython.eu/",timeout=5)

print "Status code: "+str(response.status_code)

print "Headers response: "
for header, value in response.headers.items():
  print(header, '-->', value)
  
print "Headers request : "
for header, value in response.request.headers.items():
  print(header, '-->', value)