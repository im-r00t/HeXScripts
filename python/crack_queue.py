# CRACK QUEUER #
# GreeTz FrOm SeCrEt SoCiEtY #
# Developed by r00tz and notDLS #
import requests
import sys
from threading import Thread
sessID = input("PHPSESSID >> ")
fileName = input("IP FILE >> ") # FILE CONTAINING A LIST OF IPs
cookies = dict(PHPSESSID=sessID)
ipfile = open(fileName, 'r')
ips = ipfile.readlines()
total = len(ips)

ips_per_thread = len(ips)//50
print ("IPs per thread: " + str(ips_per_thread))
ip_lists = [ips[x:x+ips_per_thread] for x in range(0, len(ips), ips_per_thread)]
threads = []

def scan(ip_list):
	for ip in ip_list:
		url = 'http://legacy.hackerexperience.com/internet?ip=' + ip
		r = requests.get(url, cookies=cookies)
		url2 = 'http://legacy.hackerexperience.com/internet?action=hack&method=bf'
		r = requests.get(url2, cookies=cookies)
		result = r.text
	if "Hacker Experience is a browser-based hacking simulation game" in r.text: # CHECK IF THE SESSION IS VALID
		print ("Error: Invalid PHPSESSID")
		exit()
	elif "Error! Access denied" in r.text: # CHECK IF YOU CAN'T CRACK
		print ("Error: Ip has a higher hasher than your cracker")

for ip_list in ip_lists:
	threads.append(Thread(target=scan, args=(ip_list,)))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()