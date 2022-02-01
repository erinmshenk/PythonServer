import os
import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
server.bind((host, port))
server.listen(10)

x = 0
while True:
	client, addr = server.accept()
	x+= 1
	print('Servicing client at %s'%addr[0])
	res = client.recv(4096)
	print('Data received')
	client.close()
	a = json.loads(res)
	cwd = os.getcwd()
	dname = a["UID"]
	fname = a["File"]
	fdata = a["Data"]

	account = os.path.join(cwd,dname)

	istrue = os.path.isdir(account)
	
	if istrue == True:
		os.chdir(account)
		ncwd = os.getcwd()
	else:
		os.mkdir(account)
		os.chdir(account)
		ncwd = os.getcwd()
	
	fpath = os.path.join(ncwd, fname)
	file = open(fpath, 'w')
	file.write(fdata)
	file.close()
	print("Success")

server.close()



