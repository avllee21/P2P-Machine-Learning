import socket
#import threading
import multiprocessing
from course import Course
from note import Note
from datetime import datetime
from img2txt import img2txt
import sys

class Client:

    def __init__(self, name, address, course, note):
        print('hello! new client.')
        self.namebroadcaseted = False
        self.username = name
        self.note = note
        self.course = course
        self.ml_node_list = ["ml_node"]
        self.p2paddress = '127.0.0.1'
        self.port = None

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.connect((address, course.course_port))
        except:
            return

        
        '''
        iThread = threading.Thread(target = self.sendMsg, args=(sock, ))
        iThread.daemon = True
        iThread.start()
        for thread in threading.enumerate(): 
            print(thread.name)
        '''
        iThread = multiprocessing.Process(target = self.sendMsg, args=(sock, ))
        iThread.daemon = True
        iThread.start()
        

        print("You are now connected as one of the Notetakers in this classroom.")

        sock.send(b"User:" +bytes(name, 'utf-8'))

        while True:
            data = sock.recv(1024)
            if not data:
                print('the server disappeared!')
                #iThread.join()
                #print('thread gone')
                iThread.terminate()
                break

            if data[0:1] == b'\x11' and self.p2paddress == '127.0.0.1':
                print(P2P.peers)
                self.peersUpdated(data[1:])
                self.p2paddress = P2P.peers[-1]
                self.port = self.p2paddress.split(":")[-1]
                print(P2P.peers)

            elif data[0:1] == b'\x11':
                print(P2P.peers)
                self.peersUpdated(data[1:])
                print(P2P.peers)
            
            elif data[0:5] == b'User:':
                P2P.peer_with_name.add(str(data[5:].decode('UTF-8')))

                #Bloadcast all the users till now
                u = ""
                for user in P2P.peer_with_name:
                    u = u + user + ","

                print()
                sock.send(b"All_Users:" + bytes(u, 'utf-8'))


            elif data[0:10] == b'All_Users:':
                print("HEre is the data")
                print(data)
                print("-------------")
                temp_Data = data[10:-1].decode('UTF-8').replace('All_Users:', '')
                for name in temp_Data.split(","):
                    P2P.peer_with_name.add(name)

 
            elif data[0:4] == b'[ML]' and name in self.ml_node_list:
                print("Broadcasting ML data")
                file_name = data[4:].strip()
                img2txt_instance = img2txt()
                data_to_broadcast = '::ml ' + img2txt_instance.convert(file_name)
                sock.send(bytes(data_to_broadcast, 'utf-8'))

            elif data[0:6] == b'[sync]':
                self.syncNote(data[6:].decode('UTF-8'))

            elif data[0:9] == b'[lecture]':
                print(str(data[9:], "utf-8"))

            elif data[0:9] == b'[addnote]':
                print(str(data[9:], "utf-8"))

            elif data[0:6] == b'[chat]':
                print(str(data, "utf-8"))
            else:
                self.note.body = self.note.body + data.decode('UTF-8') + "\n"
                print("[note] " + str(data, "utf-8"))

    def peersUpdated(self, peerData):
        P2P.peers = str(peerData, "utf-8").split(",")[:-1]

    

    def sendMsg(self, sock):
        sys.stdin = open(0)
        while True:
            try:
                user_input = input("")
            except:
                user_input = "NULL"
            if user_input == "::seenote()":
                self.seeNote()
            elif user_input == "::exportnote()":
                self.exportNote()
            elif user_input!="NULL":
                try:
                    sock.send(bytes(user_input, 'utf-8'))
                except:
                    pass

    def seeNote(self):
        print("------------ Current Version of Note for " + self.course.course_name+ " ----------")
        print(self.note.body)
        print("-------------------- End of Note ---------------------")

    def exportNote(self):
        fname = self.course.course_name + "-note-" + str(datetime.now().date())
        with open(fname, 'w') as f:
            f.write(self.note.body)
        f.close()
        print("The note is exported to your local directory...")

    def syncNote(self, updated_note):
        self.note.body = updated_note
        print("You now have the latest version of note from the server...")

class P2P:
    peers = ['127.0.0.1']
    peer_with_name = set()
