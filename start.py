'''
Libraries used

https://github.com/StorjOld/pyp2p/blob/master/pyp2p/sock.py
https://docs.python.org/3/library/socket.html

'''

from users import User
from course import Course
import sys

class SystemInfo:
    users_info = {
    "ishan": {"role": "student", "course": {"SWE"}},
    "richa": {"role": "student", "course": {"SWE"}},
    "adam": {"role": "student", "course": {"SWE"}},
    "harsh": {"role": "student", "course": {"SWE"}},
    "andrew": {"role": "student", "course": {"SWE"}},
    "ml_node": {"role": "ml", "course": {"SWE"}}
    }

    #Port information
    course_info = {
    "SWE": 5000
    }

class NotetakingApp:
    def login(self):
        username = input("Enter name of the node / user ? ")
        if username.lower() not in SystemInfo.users_info:
            print("You are not part of the system. Contact the admin.")
            sys.exit(0)

        else:
            if SystemInfo.users_info[username]["role"] == "student":
                course = input("What course is this for? ").upper()
                if course not in SystemInfo.users_info[username]["course"]:
                    print("You are not enrolled in this course.")
                    sys.exit(0)
                else:
                    join_this_course = Course(course, SystemInfo.course_info[course])
                    student = User(username, join_this_course)
                    student.startCollab('student', join_this_course)

            elif SystemInfo.users_info[username]["role"] == "ml":
                course = input("What course is this for? ").upper()

                join_this_course = Course(course, SystemInfo.course_info[course])
                student = User(username, join_this_course)
                student.startML('ml', join_this_course)

def main():
    app = NotetakingApp()
    app.login()

if __name__ == '__main__':
    main()
