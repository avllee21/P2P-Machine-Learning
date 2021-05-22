'''
Libraries used for P2P

https://github.com/StorjOld/pyp2p/blob/master/pyp2p/sock.py
https://docs.python.org/3/library/socket.html

'''

'''
Takes the user input and authenticates it 
And if successful the nodes can join the room and start collaboration

'''

import sys
from node_details import nodeDetails 
from users import User

class Course:
    def __init__(self, course, course_port):
        self.course_name =  course
        self.course_port = course_port



def main():
    name = input("Enter Name of the node :")
    if name.strip().lower() not in nodeDetails.users_info:
        print("Node is not reqistered")
        sys.exit(0)

    else:
        course = input("Enter Chat room name :")
        if course not in nodeDetails.users_info[name]["course"]:
            print("Node not registered for this chat room")
            sys.exit(0)
        else:
            course_to_join = Course(course, nodeDetails.course_info[course])
            student = User(name, course_to_join)
            student.startCollab('student', course_to_join)


if __name__ == '__main__':
    main()
