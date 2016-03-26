import argparse
import csv
import io
import json
import urllib2
import sys
import os

# Check for command line arguments, if none provided, default to todayilearned
if len(sys.argv) == 1:
	subreddit = "todayilearned"
else:
	subreddit = sys.argv[1]


# Set custom user agent, then request JSON file from Reddit
hdr = { 'User-Agent' : 'test user agent...' }
req = urllib2.Request('https://www.reddit.com/r/%s.json' % (subreddit,), headers=hdr)

# Attempt to read the recieved content
try:
	html = urllib2.urlopen(req).read()
except Exception:
	print subreddit + " doesn't seem to be a real subreddit"
	sys.exit(0)

# Open the file
fileName = subreddit + "_headlines.txt"
outputFile = io.open(fileName, 'w', encoding='utf8')

# Load the JSON file and parse its' contents
data = json.loads(html)
data2 = data['data']
data3 = data2['children']
for d in data3:
	toPrint = d['data']['title']
	#if "TIL" in toPrint:
	outputFile.write(toPrint + '\n')

# Close the file
outputFile.close()

# Print out the contents of the newly created file in the terminal
command = "cat " + fileName 
os.system(command)
