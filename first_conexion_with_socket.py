# client code: 
import socket
from time import time

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


addr = ("192.168.0.109", 8005)
msg_sent = "Hello server".encode()

sent_time = time()
print ("the sent time is: ", sent_time)

client.sendto(msg_sent, addr)

msg_recv, addres = client.recvfrom(1024)

recv_time = time()
print ( "the recv time is: ", recv_time)

print("response from server {} is {}".format(addres, msg_recv))
print("in time: ", recv_time - sent_time, "seconds")

client.close()


#server code:
import socket
from time import time

sServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sServer.bind(("0.0.0.0",8005))
recvtime = time()
msg = "hello to you, to".encode()
addr = ("192.168.0.110", 8005)



data, addr = sServer.recvfrom(1024)
print ("message: " + data.decode())
sServer.sendto( msg, addr)
sServer.close()

