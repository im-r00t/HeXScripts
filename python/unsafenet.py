# UNSAFENET #
# BRUTE FORCES AN IP GIVEN THE FIRST 2 OCTETS + THE LENGTH OF THE REMAINING TWO #
# GreeTz FrOm SeCrEt SoCiEtY #
import requests
import threading
from threading import Thread
sessID = input("PHPSESSID >> ")
cookies = dict(PHPSESSID=sessID) #enter your PHPSESSID
def generateIPs():
	num1 = int(input("First Number >> ")) #first number of their IP (E.g. 123)
	num2 = int(input("Second Number >> ")) #second number of their IP (E.g. 27)
	oct3 = int(input("Length of third number >> ")) #the length of the third number (E.g. X = 1, XX = 2, XXX = 3)
	oct4 = int(input("Length of fourth number >> ")) #the length of the fourth number (E.g. X = 1, XX = 2, XXX = 3)
	num3List = [];
	num4List = [];
	possibleIPs = [];
	if (oct3 == 3):
		i = 100
		while (i <= 255):
			num3List.append(i)
			i = i + 1
	elif (oct3 == 2):
		i = 10
		while (i <= 99):
			num3List.append(i)
			i = i + 1
	elif (oct3 == 1):
		i = 0
		while (i <= 9):
			num3List.append(i)
			i = i + 1
	
	if (oct4 == 3):
		i = 100
		while (i <= 255):
			num4List.append(i)
			i = i + 1
	elif (oct4 == 2):
		i = 10
		while (i <= 99):
			num4List.append(i)
			i = i + 1
	elif (oct4 == 1):
		i = 0
		while (i <= 9):
			num4List.append(i)
			i = i + 1
	for num3 in num3List:
		for num4 in num4List:
			possibleIPs.append("{0}.{1}.{2}.{3}".format(num1, num2, num3, num4))

	print ("Possible IPs: {0}".format(len(possibleIPs)))
	return possibleIPs

def scan(ip_list):
	for ip in ip_list:
		url = 'http://legacy.hackerexperience.com/internet?ip=' + ip
		r = requests.get(url, cookies=cookies)
		result = r.text
		if "Hacker Experience is a browser-based hacking simulation game" not in result:
			if "NPC" in result:
				print ("NPC FOUND @ {}".format(ip))
				npc.append(ip)
			elif "VPC" in result:
				print ("VPC FOUND @ {}".format(ip))
				vpc.append(ip)
			elif "Clan Server" in result:
				print ("CLAN SERVER FOUND @ ".foramt(ip))
				clans.append(ip)
		else:
			print ("Error: Not logged in")

possibleIPs = generateIPs()

npc = [];
vpc = [];
clans = [];

iplists = [[]];
ips_per_thread = len(possibleIPs)//100
print ("IPs per thread: {0}".format(str(ips_per_thread)))
ip_lists = [possibleIPs[x:x+ips_per_thread] for x in range(0, len(possibleIPs), ips_per_thread)];
threads = [];
print ("Searching...")
for ip_list in ip_lists:
	threads.append(Thread(target=scan, args=(ip_list,)))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

print ("Possible IPs:")

for item in vpc:
	print (item)

print ("Other IPs Found:")

for item in npc:
	print (item)
	
for item in clans:
	print (item)