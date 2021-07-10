from bcolors import *
import os

os.system('color')

# print(f"{bcolors.BG_YELLOW}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
# print("Normal")
# print(f"{bcolors.BG_CYAN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

# print('Enter your name:')
# x = input()
# print('Hello, ' + x)

exit = True
all_msg = []

def print_msg():
	os.system('cls')
	print("===================================================================")
	print("")
	print("===================================================================")
	for mm in all_msg:
		print(f"({mm['color']}{mm['usr']}{bcolors.ENDC}): {mm['msg']}")
	print("---------------------------")

def server_say(msg):
	all_msg.append({"usr":"Server", "msg":msg, "color":bcolors.OKGREEN})

def valid(name, msg):
	all_msg.append({"usr":name, "msg":msg, "color":bcolors.CYAN})
	if msg == "info":
		server_say("this is simple!")
		server_say("just type something")
		server_say("and press enter!")
	elif  msg == "hallo":
		server_say("hy!")
	

all_msg.append({"usr":"Server", "msg":"Welcome! please type something,", "color":bcolors.OKGREEN})
print("your name is : ", end=" ")
name  = input()
while exit:
	print_msg()
	msg = input()
	if msg != "quit":
		valid(name, msg)
		# all_msg.append({"usr":"me", "msg":msg, "color":bcolors.CYAN})
		# server_say(msg)
	else:
		print("Thank!")
		break