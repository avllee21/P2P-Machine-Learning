import socket
import threading
from note import Note
from course import Course
import time


class Server:
    lecture_outline = ""
    connections = []
    peers = []
    peers_with_name = set()

    def __init__(self, name, course, note):
        self.username = name
        self.course = course
        self.note = note
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('127.0.0.1', course.course_port))
        sock.listen(1)

        print(self.username + " is now the acting server of this room!")

        while True:
            c, a = sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            self.peers.append(a[0] + ':' + str(a[1]))
            print(str(a[0]) + ':' + str(a[1]), "has connected")
            self.sendPeers()
            

    def handler(self, c, a):
        while True:
            data = c.recv(1024)

            if not data:
                print(str(a[0]) + ':' + str(a[1]), "has disconnected")
                
                # TODO: Fix the disconnection logic
                # TODO: Remove the disconnected client from the self.peers_with_name set
                self.connections.remove(c)
                self.peers.remove(a[0] + ':' + str(a[1]))



                c.close()
                self.sendPeers()
                break
            
            elif data[0:5] == b'User:':
                self.peers_with_name.add(str(a[0]) + ':' + str(a[1])+"?"+str(data[5:].decode('UTF-8')))

                #Broadcast all the users till now
                u = ""
                for user in self.peers_with_name:
                    u = u + user + ","

                for connection in self.connections:
                    connection.send(b"All_Users:" + bytes(u, 'utf-8'))

            elif data[0:4] == b'::ml':
                data_to_send = "[ML IMG -> TXT] \n -*10 \n".encode('UTF-8') + data[4:]
                self.broadcast(data_to_send)

            elif data[0:2] == b'::':
                data_to_send = "[chat] ".encode('UTF-8') + data[2:]
                self.broadcast(data_to_send)

            elif data[0:4] == b'[ML]':
                print("Broadcasting ML data from server")
                self.broadcast(data)



            else:
                print(a, ":", data.decode('UTF-8'))
                self.note.body = self.note.body + data.decode('UTF-8') + "\n"
                self.broadcast(data)

    def sendPeers(self):
        p = ""
        for peer in self.peers:
            p = p + peer + ","

        for connection in self.connections:
            connection.send(b'\x11' + bytes(p, 'utf-8'))


    def broadcast(self, data_to_broadcast):
        for connection in self.connections:
            connection.send(bytes(data_to_broadcast))


