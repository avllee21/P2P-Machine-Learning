import socket
import time
import threading
from course import Course
from note import Note


class Server:
    lecture_outline = ""
    connections = []
    peers = []
    peers_with_name = set()

    def __init__(self, name, course, note):
        self.username = name
        self.course = course
        self.note = note


        # bind the server socket to a specific address and a course port
        serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversock.bind(('127.0.0.1', course.course_port))
        serversock.listen(1)


        print(self.username + " is now the acting server of this room!")
        
        # start accepting connections from clientsockets
        while True:
            clientsocket, clientaddress = serversock.accept()
            iThread = threading.Thread(target=self.handlepeer, args=(clientsocket, clientaddress))
            iThread.daemon = True
            iThread.start()
            self.connections.append(clientsocket)
            self.peers.append(clientaddress[0] + ':' + str(clientaddress[1]))
            print(str(clientaddress[0]) + ':' + str(clientaddress[1]), "has connected")
            self.sendPeers()
            

    def handlepeer(self, clientsocket, clientaddress):
        while True:
            data = clientsocket.recv(1024)

            if not data:
                print(str(clientaddress[0]) + ':' + str(clientaddress[1]), "has disconnected")
                
                # TODO: Fix the disconnection logic
                # TODO: Remove the disconnected client from the self.peers_with_name set
                self.connections.remove(clientsocket)
                self.peers.remove(clientaddress[0] + ':' + str(clientaddress[1]))



                clientsocket.close()
                self.sendPeers()
                break
            
            elif data[0:5] == b'User:':
                self.peers_with_name.add(str(clientaddress[0]) + ':' + str(clientaddress[1])+"?"+str(data[5:].decode('UTF-8')))

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
                print(clientaddress, ":", data.decode('UTF-8'))
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


