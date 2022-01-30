#creating a server...! 
import socket

s=socket.socket()
print('socket created')
s.bind(('<IP_host>',9999))

s.listen(3)
print('waiting for client')
while True:
	c, addr =s.accept()
	print('client connected:' )
	
	c.send(bytes('Hello dear,have cub!'))
	c.close()

#connecting to other server.. 

import socket
c=socket.socket()
c.connect(('<IP_client>',9999))
print(c.recv(1024).decode())
	
