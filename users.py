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
                time.sleep(randint(1, 20))

                with open('semaphore.txt', 'r') as reader:
                    timelast = int(reader.readlines()[-1])
                

                counter = 0

                while (int(time.time()) - timelast) < 5 and counter<5:
                    time.sleep(randint(5, 10))
                    counter +=1

                print(counter)

                with open("semaphore.txt", "a") as myfile:
                    myfile.write("\n"+str(int(time.time())))

                

                if self.name not in self.ml_node_list and counter ==0:
                    print("Taking over the main node")
                    try:
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
