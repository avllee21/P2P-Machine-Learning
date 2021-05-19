'''
Libraries used

https://github.com/StorjOld/pyp2p/blob/master/pyp2p/sock.py
https://docs.python.org/3/library/socket.html

'''
import sys
from users import User
from course import Course


# TODO: Add more system info
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

class Application:
    def login(self):
        name = input("What is your name? ")
        if name.strip().lower() not in SystemInfo.users_info:
            print("Your name is not in the system. Please try again.")
            sys.exit(0)

        else:
            if SystemInfo.users_info[name]["role"] == "student":
                course = input("What course is this for? ").upper()
                if course not in SystemInfo.users_info[name]["course"]:
                    print("You are not enrolled in this course. Goodbye")
                    sys.exit(0)
                else:
                    course_to_join = Course(course, SystemInfo.course_info[course])
                    student = User(name, course_to_join)
                    student.startCollab('student', course_to_join)

            elif SystemInfo.users_info[name]["role"] == "ml":
                course = input("What course is this for? ").upper()
                if course not in SystemInfo.users_info[name]["course"]:
                    print("You are not enrolled in this course. Goodbye")
                    sys.exit(0)
                else:
                    course_to_join = Course(course, SystemInfo.course_info[course])
                    student = User(name, course_to_join)
                    student.startCollab('student', course_to_join)

def main():
    app = Application()
    app.login()

if __name__ == '__main__':
    main()
