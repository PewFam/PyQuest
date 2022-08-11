import requests

header="""\033[4m                                                           
,------.           ,-----.                          ,--.   
|  .--. ',--. ,--.'  .-.  '  ,--.,--. ,---.  ,---.,-'  '-. 
|  '--' | \  '  / |  | |  |  |  ||  || .-. :(  .-''-.  .-' 
|  | --'   \   '  '  '-'  '-.'  ''  '\   --..-'  `) |  |   
`--'     .-'  /    `-----'--' `----'  `----'`----'  `--'   
         `---'
\033[0m                                             
"""
from os import name, system 
if name == "nt":
	system("cls")
elif name == "posix":
	system("clear")
	
print(header)

url = input("\n\033[1mURL : \033[0m")

r = request.get(url)

list = """

"""