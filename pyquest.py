import sys 
sys.path.insert(0, "\request")
import requests

header ="""
\033[5m
   ___       ____               __ 
  / _ \__ __/ __ \__ _____ ___ / /_
 / ___/ // / /_/ / // / -_|_-</ __/
/_/   \_, /\___\_\_,_/\__/___/\__/ 
     /___/                         

\033[0m                                             
"""
from os import name, system 
while True:
	print(header)
	choice = input("""
1 - get 
2 - login
3 - exit

""")
	if choice == "1":
		if name == "nt":
			system("cls")
		elif name == "posix":
			system("clear")
	
		

		url = input("\n\033[1mURL : \033[0m")

		r = requests.get(url)

		list = input("""
what ?

1 - headers
2 - text
3 - json
4 - nothing


""")
		if list == "1":
			print(r.headers)
			input("\n\033[4mPress enter to continue...\033[0m")
		elif list == "2":
			print(r.text)
			input("\n\033[4mPress enter to continue...\033[0m")
		elif list == "3":
			print(r.json)
			input("\n\033[4mPress enter to continue...\033[0m")
		elif list == "4":
			pass
	elif choice == "2":
		url = input("\n\033[1mURL\033[0m : ")
		payload = {
		'username': input("\nusername : "),
		
		'password': input("\npassword : ")
}
		requests.post(url, data=payload)
		choice2 = input("""
what do you want to do now ?	

1 - headers
2 - text
3 - json
4 - nothing

""")
		if choice2 == "1":
			r = requests.get(url)
			print(r.headers)
			input("\n\033[4mPress enter to continue...\033[0m")
		elif choice2 == "2":
			print(r.text)
			input("\n\033[4mPress enter to continue...\033[0m")
		elif choice2 =="3":
			print(r.json)
			input("\n\033[4mPress enter to continue...\033[0m")
		elif choice2 =="4":
			sys.exit()
	elif choice =="3":
		sys.exit()