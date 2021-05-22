'''
Contains the information regarding the nodes and their roles
Additionally, they have info regarding the rooms that they are allowed to join
'''


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