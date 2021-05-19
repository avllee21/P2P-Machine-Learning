import sys
from server import Server
from client import Client, P2P
from course import Course
import time
from random import randint
from note import Note

class User:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.note = Note(course)
        self.ml_node_list = ["ml_node"]
        self.curr_port = None

    def startCollab(self, role, course):
      
        if role == 'student':
            client = None
            while True:
                try:
                    print("Connecting to the server ...")
                    time.sleep(randint(1, 5))
                    
                    peer = '127.0.0.1'
                    #print(P2P.peers, str(list(P2P.peer_with_name)))
                    try:
                        client = Client(self.name, peer, course, self.note)

                    # Exit if end-user interrupts
                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        pass


                    if self.name not in self.ml_node_list:

                        try:
                            if len(P2P.peers)==1:
                                server = Server(self.name, course, self.note)
                            
                            elif self.name == sorted(P2P.peer_with_name, key = lambda x : x.split("?")[1])[0].split("?")[1]:
                                server = Server(self.name, course, self.note)
                        
                        except KeyboardInterrupt:
                            sys.exit(0)
                
                # Exit if end-user interrupts
                except KeyboardInterrupt:
                    sys.exit(0)
