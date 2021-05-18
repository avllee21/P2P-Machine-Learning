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
                    print("Trying to connect...")
                    time.sleep(randint(1, 5))
                    
                    peer = '127.0.0.1'
                    #to_connect = sorted(P2P.peer_with_name, key = lambda x : x.split("?")[1])[0].split("?")[0]
                    #for peer in P2P.peers:
                    print(P2P.peers, str(list(P2P.peer_with_name)))
                    try:
                        client = Client(self.name, peer, course, self.note)

                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        pass


                    if self.name not in self.ml_node_list:
                        print(P2P.peer_with_name)
                        if(len(P2P.peers)!=1):
                            print(self.name)    
                            print(sorted(P2P.peer_with_name, key = lambda x : x.split("?")[1])[0].split("?")[1])
                        try:
                            if len(P2P.peers)==1:
                                print('p2p.peers is 1')
                                server = Server(self.name, course, self.note)
                            
                            elif self.name == sorted(P2P.peer_with_name, key = lambda x : x.split("?")[1])[0].split("?")[1]:
                                print('sorting function has been called')
                                server = Server(self.name, course, self.note)

                            # elif client != None and client.p2paddress == P2P.peers[1]:
                            #     server = Server(self.name, course, self.note)    
                            
                            # elif client != None and curr_port!=None:
                            #     print(client.p2paddress +':'+ curr_port)

                            # elif client != None and curr_port!=None and ((client.p2paddress +':'+ curr_port) == P2P.peers[1]):
                            #     server = Server(self.name, course, self.note) 

                
                            # else:
                            #     time.sleep(randint(5, 10))
                            #     client = Client(self.name, peer, course, self.note)
                        
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
