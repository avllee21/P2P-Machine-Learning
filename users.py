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

        while True:
            try:
                for peer in P2P.peers:
                    print("Connecting...")
                    time.sleep(randint(2, 10))
                    try:
                        client = Client(self.name, peer, course, self.note)

                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        pass
                status = ""
                time.sleep(randint(10, 20))
                with open('semaphore.txt', 'r') as reader:
                    status = reader.readlines()
                    
                if self.name not in self.ml_node_list and status!="locked":
                    print("Taking over the main node")
                    try:
                        with open('semaphore.txt', 'w') as writer:
                            writer.write("locked")

                        server = Server(self.name, course, self.note)

                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        print("Couldn't start the server...")
                else:
                    try:
                        for peer in P2P.peers:
                            print("Connecting...")
                            time.sleep(randint(2, 10))
                            try:
                                client = Client(self.name, peer, course, self.note)

                            except KeyboardInterrupt:
                                sys.exit(0)
                            except:
                                pass
                    except KeyboardInterrupt:
                        # break
                        sys.exit(0)

            except KeyboardInterrupt:
                # break
                sys.exit(0)


class MachineLearning:
    def __init__(self, name):
        self.name = name

    def maintainSystem(self):
        print("Make some changes to database")
