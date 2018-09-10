import pymongo
from dbConnection import ( db )

courses = db["test_courses"]

def getAll():
    courses_array = []
    for course in courses.find():
        # print(course["name"])
        courses_array.append(course)

    return courses_array

def getDownlodCourses():
    download_courses_array = []
    for course in courses.find({"processed": False, "download": True}):
        download_courses_array.append(course)
    print(download_courses_array)

    return download_courses_array

# def updateVideoStyle(video_style, course):
