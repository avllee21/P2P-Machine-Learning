import socket
import threading
from course import Course
from note import Note
from datetime import datetime

class Client:

    def __init__(self, name, address, course, note):
        self.username = name
        self.note = note
        self.course = course
        self.ml_node_list = ["ml_node"]

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((address, course.course_port))
        iThread = threading.Thread(target = self.sendMsg, args=(sock, ))
        iThread.daemon = True
        iThread.start()
        print("You are now connected as one of the Notetakers in this classroom.")

        while True:
            data = sock.recv(1024)
            if not data:
                break
            if data[0:1] == b'\x11':
                self.peersUpdated(data[1:])
            elif data[0:4] == b'[ML]' and name in self.ml_node_list:
                print("Broadcasting ML data")
                data_to_broadcast = 'testML'
                # TODO: send 
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
        while True:
            user_input = input("")
            if user_input == "::seenote()":
                self.seeNote()
            elif user_input == "::exportnote()":
                self.exportNote()
            else:
                sock.send(bytes(user_input, 'utf-8'))

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
