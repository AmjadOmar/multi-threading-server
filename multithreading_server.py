# Add your code here to run in your startup task
#!/usr/bin/env python

import socket
from threading import Thread
from SocketServer import ThreadingMixIn

class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for " + ip + ": " + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print("received data: " % data)
            conn.send(data) # echo

TCP_IP = '0.0.0.0'
TCP_PORT = 62
BUFFER_SIZE = 30

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    s.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip,port)) = s.accept()
    new_thread = ClientThread(ip, port)
    new_thread.start()
    threads.append(new_thread)

for t in threads:
    t.join()

