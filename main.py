import os, stat
import shutil
from scrapper.coursera_dl import ( scrapper )
from db.coursedb import ( Courses )
import topics_complexity
from predict import ( getVideoStyleValues )


def deleteDownloadContent(course):
    print("deleting files ....... ")

    jsonFile = course["path"] + "-syllabus-parsed.json"

    if os.path.exists(jsonFile):
        os.remove(jsonFile)
    else:
        print("The file does not exist")
        return False

    if os.path.exists(course["path"]):
        shutil.rmtree(course["path"])
    else:
        print("The file does not exist")
        return False


if __name__ == '__main__':
    
    courses = Courses()
    print(courses.getDownloadCoursesPaths())
    download_courses = courses.getDownlodCourses()

    for course in download_courses:
        if scrapper(course["path"]):

            topicResult = topics_complexity.generate_topics_complexity(course["path"])
            courses.updateAbstractTopics(topicResult["topics"], course)
            courses.updateComplexityLevel(topicResult["level"], course)

            video_styles = getVideoStyleValues(course["path"])
            courses.updateVideoStyle(video_styles, course)

            courses.updateProcessedTrue(course)
            print("course download successfull")
            deleteDownloadContent(download_courses[0])
        else:
            courses.updateProcessedFalse(course)
            print("course download Fail")
        