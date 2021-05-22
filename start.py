'''
Libraries used for P2P

https://github.com/StorjOld/pyp2p/blob/master/pyp2p/sock.py
https://docs.python.org/3/library/socket.html

'''
import sys
from users import User

class Course:
    def __init__(self, course, course_port):
        self.course_name =  course
        self.course_port = course_port

# Node details for the application
class nodeDetails:
    # Add new users with their roles and corresponding course here
    users_info = {
        "ishan": {"role": "student", "course": {"SWE"}},
        "richa": {"role": "student", "course": {"SWE"}},
        "adam": {"role": "student", "course": {"SWE"}},
        "harsh": {"role": "student", "course": {"SWE"}},
        "andrew": {"role": "student", "course": {"SWE"}},
        "ml_node": {"role": "ml", "course": {"SWE"}}
    }

    # Port information for the course
    # Add courses and specify non classing port numbers to be used
    course_info = {
        "SWE": 5000
    }


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
