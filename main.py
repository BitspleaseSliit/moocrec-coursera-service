from scrapper.coursera_dl import ( scrapper )
from db.coursedb import ( Courses )



if __name__ == '__main__':
    # scrapper()
    courses = Courses()
    print(courses.getDownloadCoursesPaths())