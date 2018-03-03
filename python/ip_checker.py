# MULTI-THREADED IP CHECKER #
# GreeTz FrOm SeCrEt SoCiEtY #
import requests
import sys
from threading import Thread
sessID = input("PHPSESSID >> ")
fileName = input("IP FILE >> ") # FILE CONTAINING A LIST OF IPs
cookies = dict(PHPSESSID=sessID)
ipfile = open(fileName, 'r')
ips = ipfile.readlines()
npc = []
vpc = []
clans = []
total = len(ips)

ips_per_thread = len(ips)//50
print ("IPs per thread: " + str(ips_per_thread))
ip_lists = [ips[x:x+ips_per_thread] for x in range(0, len(ips), ips_per_thread)]
threads = []

def scan(ip_list):
	for ip in ip_list:
		url = 'http://legacy.hackerexperience.com/internet?ip=' + ip
		r = requests.get(url, cookies=cookies)
		result = r.text
		if "NPC" in result:
			print ("NPC server found")
			npc.append(ip)
		elif "VPC" in result:
			print ("VPC server found")
			vpc.append(ip)
		elif "Clan Server" in result:
			print ("Clan Server found")
			clans.append(ip)
		elif "Hacker Experience is a browser-based hacking simulation game" in result:
			print ("Invalid PHPSESSID")
		else:
			print ("Dead IP found")

for ip_list in ip_lists:
	threads.append(Thread(target=scan, args=(ip_list,)))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()
	
print ("All alive IPs will be saved into valid.txt")
output = open('valid.txt', 'w')
output.write("VPC " + "(" + str(len(vpc)) + ")\n")
for item in vpc:
    output.write(item)
output.write("\nNPC " + "(" + str(len(npc)) + ")\n")
for item in npc:
    output.write(item)
output.write("\nClan Servers" + "(" + str(len(clans)) + ")\n")
for item in clans:
    output.write(item)
print ("\n" + str(len(npc)) + " NPCs found, " + str(len(vpc)) + " VPCs found and " + str(len(clans)) + " Clans found")
print (str(len(npc) + len(vpc) + len(clans)) + "/" + str(total) + " IPs were alive.")