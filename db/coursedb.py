import pymongo
from dbConnection import ( db )

courses = db["test_courses"]

def getAll():
    courses_array = []
    for course in courses.find():
        # print(course["name"])
        courses_array.append(course)

    return courses_array

