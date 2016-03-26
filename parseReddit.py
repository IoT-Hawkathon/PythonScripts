import argparse
import csv
import io
import json
import urllib2

#TODO: change user agent string
hdr = { 'User-Agent' : 'test user agent...' }
req = urllib2.Request('https://www.reddit.com/r/todayilearned.json', headers=hdr)
html = urllib2.urlopen(req).read()

outputFile = io.open('TIL_OUTPUT.txt', 'w', encoding='utf8')

#toParse = open("todayilearned.txt", 'rb')

data = json.loads(html)
data2 = data['data']
data3 = data2['children']
for d in data3:
	toPrint = d['data']['title']
	if "TIL" in toPrint:
		outputFile.write(toPrint + '\n')
