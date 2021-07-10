import socket, threading
from bcolors import *
import os
import re

os.system('color')

all_msg = []

def print_msg():
    os.system('cls')
    print("===================================================================")
    print("")
    print("===================================================================")
    for mm in all_msg:
        print(f"({mm['color']}{mm['usr']}{bcolors.ENDC}): {mm['msg']}")
    print("---------------------------")

def handle_messages(connection: socket.socket):
    '''
        Receive messages sent by the server and display them to user
    '''

    while True:
        try:
            msg = connection.recv(1024)

            # If there is no message, there is a chance that connection has closed
            # so the connection will be closed and an error will be displayed.
            # If not, it will try to decode message in order to show to user.
            if msg:
                # print(msg.decode())
                msga = msg.decode()
                regx = re.split(" - ",msga)
                print(regx)
                if len(regx) > 1: 
                    all_msg.append({"usr":regx[0], "msg":regx[1], "color":bcolors.WARNING})
                else:
                    server_say(msga)
                    # all_msg.append({"usr":"Sev", "msg":msga, "color":bcolors.WARNING})
                print_msg()
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break

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

def client() -> None:
    '''
        Main process that start client connection to the server 
        and handle it's input messages
    '''

    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000
    all_msg.append({"usr":"Server", "msg":"Welcome! please type something,", "color":bcolors.OKGREEN})
    print("your name is : ", end=" ")
    name  = input()
    try:
        # Instantiate socket and start connection with server
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        # Create a thread in order to handle messages sent by server
        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        logi = "login "+name
        socket_instance.send(logi.encode())

        print('Connected to chat!')
        # print_msg()

        # Read user's input until it quit from chat and close connection
        while True:
            print_msg()
            msg = input()

            if msg == 'quit':
                break

            valid(name, msg)
            # Parse message to utf-8
            socket_instance.send(msg.encode())

        # Close connection with the server
        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()