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

    def startCollab(self, role, course):
      
        if role == 'student':
            while True:
                try:
                    print("Trying to connect...")
                    time.sleep(randint(2, 10))
                    for peer in P2P.peers:
                        try:
                            client = Client(self.name, peer, course, self.note)

                        except KeyboardInterrupt:
                            sys.exit(0)
                        except:
                            pass
                        
                        if self.name not in self.ml_node_list:
                            try:
                                server = Server(self.name, course, self.note)

                            except KeyboardInterrupt:
                                sys.exit(0)
                            except:
                                print("Couldn't start the server...")
                except KeyboardInterrupt:
                    # break
                    sys.exit(0)


class MachineLearning:
    def __init__(self, name):
        self.name = name

    def maintainSystem(self):
        print("Make some changes to database")
