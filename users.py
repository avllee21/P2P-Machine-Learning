import sys
from server import Server
from client import Client, P2P
from course import Course
import time
from random import randint
from note import Note
from img2txt import ClientML

class User:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.note = Note(course)

    def startCollab(self, role, course):

        if role == 'student':
            while True:
                try:
                    print("Trying to connect...")
                    time.sleep(randint(1, 5))
                    for peer in P2P.peers:
                        try:
                            client = Client(self.name, peer, course, self.note)

                        except KeyboardInterrupt:
                            sys.exit(0)
                        except:
                            pass

                        try:
                            server = Server(self.name, course, self.note)

                        except KeyboardInterrupt:
                            sys.exit(0)
                        except:
                            print("Couldn't start the server...")
                except KeyboardInterrupt:
                    # break
                    sys.exit(0)

# TODO: Modify the code below to include the function from ml-img2txt.py
# If the stream contains the command <ML2IMG> then invoke the below function
# This will convert the give image location to text and display it on the screen

    def startML(self, role, course):

        if role == 'ml':
            while True:
                try:
                    print("Trying to connect...")
                    time.sleep(randint(1, 5))
                    for peer in P2P.peers:
                        try:
                            client = ClientML(self.name, peer, course, self.note)

                        except KeyboardInterrupt:
                            sys.exit(0)
                        except:
                            pass

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
