import pymongo
from bson.objectid import ObjectId
from dbConnection import ( db )

courses = db["test_courses"]

def getAll():
    courses_array = []
    try:
        for course in courses.find():
            # print(course["_id"])
            courses_array.append(course)
        return courses_array
    except pymongo.errors.PyMongoError as e:
        print(e)
        return []
    

def getDownlodCourses():
    download_courses_array = []
    try:
        for course in courses.find({"processed": False, "download": True}):
            download_courses_array.append(course)
            # print(download_courses_array)
        return download_courses_array
    except pymongo.errors.PyMongoError as e:
        print(e)
        return []
    

def updateVideoStyle(video_style, course):
    try:
        select_query = { "_id": ObjectId(course["_id"])}
        insert_value = { "$set": { "videoStyle": video_style} }
        result = courses.update_one(select_query, insert_value)
        return result.matched_count > 0 
    except pymongo.errors.PyMongoError as e:
        print(e)
        return False

def updateAbstractTopics(abstract_topics, course):
    try:
        select_query = { "_id": ObjectId(course["_id"])}
        insert_value = { "$set": { "abstractTopics": abstract_topics} }
        result = courses.update_one(select_query, insert_value)
        return result.matched_count > 0 
    except pymongo.errors.PyMongoError as e:
        print(e)
        return False  

def updateLinguisticComplexity(linguistic_complexity, course):
    try:
        select_query = { "_id": ObjectId(course["_id"])}
        insert_value = { "$set": { "linguisticComplexity": linguistic_complexity} }
        result = courses.update_one(select_query, insert_value)
        return result.matched_count > 0 
    except pymongo.errors.PyMongoError as e:
        print(e)
        return False

def updateProcessedTrue(course):
    try:
        select_query = { "_id": ObjectId(course["_id"])}
        insert_value = { "$set": { "processed": True } }
        result = courses.update_one(select_query, insert_value)
        return result.matched_count > 0 
    except pymongo.errors.PyMongoError as e:
        print(e)
        return False

def updateProcessedFalse(course):
    try:
        select_query = { "_id": ObjectId(course["_id"])}
        insert_value = { "$set": { "processed": False } }
        result = courses.update_one(select_query, insert_value)
        return result.matched_count > 0 
    except pymongo.errors.PyMongoError as e:
        print(e)
        return False

# mycourse = getAll()[0]
# print(mycourse)
# videoStyle = {}
# videoStyle["talkingHead"] = 30
# videoStyle["slide"] = 10
# videoStyle["code"] = 60
# videoStyle["conversation"] = 0
# videoStyle["animation"] = 0
# videoStyle["whiteboard"] = 0
# print(videoStyle)
# updateVideoStyle(videoStyle, mycourse)