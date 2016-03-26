import argparse
import csv
import io
import json
import urllib2
import sys
import os

if len(sys.argv) == 1:
	subreddit = "todayilearned"
else:
	subreddit = sys.argv[1]

#TODO: change user agent string
hdr = { 'User-Agent' : 'test user agent...' }

req = urllib2.Request('https://www.reddit.com/r/%s.json' % (subreddit,), headers=hdr)

try:
	html = urllib2.urlopen(req).read()
except Exception:
	print subreddit + " doesn't seem to be a real subreddit"
	sys.exit(0)

fileName = subreddit + "_headlines.txt"

outputFile = io.open(fileName, 'w', encoding='utf8')

data = json.loads(html)
data2 = data['data']
data3 = data2['children']
for d in data3:
	toPrint = d['data']['title']
	#if "TIL" in toPrint:
	outputFile.write(toPrint + '\n')

#outputFile.close()

command = "cat " + fileName 

print "Printing Now..."
os.system(command)
