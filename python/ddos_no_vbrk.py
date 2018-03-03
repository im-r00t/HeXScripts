# DDOS NO VBRK REQUIRED #
# GreeTz FrOm SeCrEt SoCiEtY #
import requests
import time
sessID = input("PHPSESSID >> ")
while True:
	cookies = dict(PHPSESSID=sessID)
	target = input("TARGET IP >> ")
	r = requests.post("https://legacy.hackerexperience.com/DDoS", data = {'ip':target}, cookies=cookies) # SEND POST REQUEST
	if "Hacker Experience is a browser-based hacking simulation game" in r.text: # CHECK IF THE SESSION IS VALID
		print ("Error: Invalid PHPSESSID")
		exit()
	elif "Launch DDoS attack" in r.text: # CHECK IF THERE WAS AN ERROR
		print ("Error: There was an issue launching the DDoS Attack, please make sure the IP is valid and alive")
	else:		
		print ("DDoS Attack Launched Against {} | Waiting 5 minutes...".format(target))
		time.sleep(300)
