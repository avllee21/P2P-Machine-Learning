'''
Main node responsible for broadcasting messages between peers
Keeps track of all the connected nodes
'''

import socket
import time
import threading


class ChatNode:
    def __init__(self, name, course, note):
        self.name = name
        self.course = course
        self.note = note

        self.connections = []
        self.peer_addresses = []
        self.peers_with_name = set()


        # bind the server socket to a specific address and a course port
        serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversock.bind(('127.0.0.1', self.course.course_port))
        serversock.listen(1)

        print(self.name + " is now the chat node of this room.")
        
        # start accepting connections from clientsockets
        while True:
            clientsocket, clientaddress = serversock.accept()
            iThread = threading.Thread(target=self.handlepeer, args=(clientsocket, clientaddress))
            iThread.daemon = True
            iThread.start()

            self.connections.append(clientsocket)
            self.peer_addresses.append(clientaddress[0] + ':' + str(clientaddress[1]))
            self.send_peer_addresses()

            print(str(clientaddress[0]) + ':' + str(clientaddress[1]), "has connected")
            

    def handlepeer(self, clientsocket, clientaddress):
        while True:
            data = clientsocket.recv(1024)

            if not data:
                print(str(clientaddress[0]) + ':' + str(clientaddress[1]), "has disconnected")
                
                # TODO: Fix the disconnection logic
                # TODO: Remove the disconnected client from the self.peers_with_name set
                self.connections.remove(clientsocket)
                self.peer_addresses.remove(clientaddress[0] + ':' + str(clientaddress[1]))
                clientsocket.close()
                self.send_peer_addresses()
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
                data_to_send = "[ML IMG -> TXT] \n".encode('UTF-8') + data[4:]
                self.send_data(data_to_send)


            elif data[0:4] == b'[ML]':
                print("Sending ML data from server")
                self.send_data(data)

            elif data[0:13] == b'savehistory()':
                data_to_send = "[save]" + self.note.body
                clientsocket.send(bytes(data_to_send.encode('UTF-8')))

            else:
                print(clientaddress, ":", data.decode('UTF-8'))
                self.note.body = self.note.body + data.decode('UTF-8') + "\n"
                self.send_data(data)


    def send_peer_addresses(self):
        p = ""
        for peer in self.peer_addresses:
            p = p + peer + ","

        for connection in self.connections:
            connection.send(b'\x11' + bytes(p, 'utf-8'))


    def send_data(self, data_to_send):
        for connection in self.connections:
            connection.send(bytes(data_to_send))