import sys
import time
from chat_node import ChatNode
from client import Client, P2P
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
        client = None
        chat_node_instance = None

        if role == 'student':
            
            while True:
                try:
                    print("Starting collaboration!")
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
                                chat_node_instance = ChatNode(self.name, course, self.note)
                            
                            # Finding the next main chat node instance via name - sorted in lexiographic order
                            elif self.name == sorted(P2P.peer_with_name, key = lambda x : x.split("?")[1])[0].split("?")[1]:
                                chat_node_instance = ChatNode(self.name, course, self.note)
                        
                        except KeyboardInterrupt:
                            sys.exit(0)
                
                # Exit if end-user interrupts
                except KeyboardInterrupt:
                    sys.exit(0)

# TODO: Add professor.py file with the professor class in it