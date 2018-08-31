import socket

 host = "www.facebook.com"
 port = 80

# create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect the client
client.connect((host,port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: facebook.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print response