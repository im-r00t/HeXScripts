# LOG WATCHER #
# GreeTz FrOm SeCrEt SoCiEtY #
import requests
import re
import time
import os
from time import sleep


def checkLogs():
	url = 'http://legacy.hackerexperience.com/log'
	loginRegex = '[\[][0-9]+\.[0-9]+\.[0-9]+\.[0-9]+[\]]\slogged\sin'
	ddosRegex = '\[[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\]\slaunched\sa\sDDoS\sattack\sagainst\slocalhost'
	r = requests.get(url, cookies=cookies)
	result = r.text
	if "Hacker Experience is a browser-based hacking simulation game" not in result:
		p = re.findall(loginRegex, result)
		d = re.findall(ddosRegex, result)
		for match in p:
			detectedIPs.append(match)
		for match in d:
			detectedIPs.append(match)
		removeDupes(detectedIPs)
	else:
		print ("Error: Account not logged in")

	
def removeDupes(values):
	output = []
	seen = set()
	for value in values:
		if value not in seen:
			output.append(value)
			seen.add(value)
	outputIPs(output)
	
def outputIPs(values):
	os.system('cls') # If you're using linux change 'cls' to 'clear'
	print ("IPs Found:\n")
	for ip in values:
		print (ip, "\n")


detectedIPs = [];
sessID = input("PHPSESSID >> ")
cookies = dict(PHPSESSID=sessID)

while True:
		try:
			checkLogs()
		except KeyboardInterrupt:
			break