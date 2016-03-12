import json
from os import system
from time import sleep
from colorama import Fore, Style

def bake():
	json_data = open('Bakefile', 'r').read()
	data = json.loads(json_data)
	
	print(Style.BRIGHT + Fore.BLUE + "==> " + Style.RESET_ALL + "Initiating task: " + Style.BRIGHT + data['bake']['task'] + Style.RESET_ALL)
	
	for item in data['bake']['run']:
		print(Style.BRIGHT + Fore.BLUE + "==> " + Style.RESET_ALL + "Running: " + Style.BRIGHT + item + Style.RESET_ALL)
		system(item)
		sleep(1)

try:
	bake()
except:
	print(Fore.RED + 'Error: could not find "Bakefile"!')
	print(Fore.RED + 'Please add a "Bakefile" to your directory...' + Fore.RESET)