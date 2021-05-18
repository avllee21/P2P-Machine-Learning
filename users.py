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
            curr_port = None
            while True:
                try:
                    print("Trying to connect...")
                    time.sleep(randint(1, 5))
                    for peer in P2P.peers:
                        print(P2P.peers, str(list(P2P.peer_with_name)))
                        try:
                            client = Client(self.name, peer, course, self.note)

                        except KeyboardInterrupt:
                            sys.exit(0)
                        except:
                            pass
                        
                        print("current port ----------------> ", curr_port)

                        if client != None and client.port!=None:
                            curr_port = client.port

                        if self.name not in self.ml_node_list:
                            try:
                                if client !=None:
                                    print(client.p2paddress, P2P.peers)

                                if len(P2P.peers)==1:
                                    server = Server(self.name, course, self.note)

                                elif client != None and client.p2paddress == P2P.peers[1]:
                                    server = Server(self.name, course, self.note)    
                                
                                elif client != None and curr_port!=None:
                                    print(client.p2paddress +':'+ curr_port)

                                elif client != None and curr_port!=None and ((client.p2paddress +':'+ curr_port) == P2P.peers[1]):
                                    server = Server(self.name, course, self.note) 
                            
                                else:
                                    time.sleep(randint(5, 10))
                                    client = Client(self.name, peer, course, self.note)
                            
                            except KeyboardInterrupt:
                                sys.exit(0)

                            # # first person to enter the network
                            # except:
                            #     try:
                            #         print("First node becomes server")
                            #         server = Server(self.name, course, self.note)

                            #     except KeyboardInterrupt:
                            #         sys.exit(0)
                            #     except:
                            #         print("Couldn't start the server...")
                except KeyboardInterrupt:
                    # break
                    sys.exit(0)


class MachineLearning:

    def __init__(self, name):
        self.name = name

    def maintainSystem(self):
        print("Make some changes to database")
