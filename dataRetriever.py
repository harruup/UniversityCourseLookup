#This script used db connection to fetch data and represent it in user friendly manner
import dbConnection as db
import re

def showPrerequisites(coursecode):
    prereqs = []
    connection = db.create_connection(db.database)
    with connection:
        courselist= db.getPrerequisites(connection, coursecode)
        if not courselist:
            prereqs.append("No Prerequisites required for this course")
        for c in courselist:
            prereqs.append(str(c[0]))
    return prereqs

def showPrerequisitesFor(coursecode):
    prereqsfor = []
    connection = db.create_connection(db.database)
    with connection:
        courselist = db.getPrerequisteFor(connection, coursecode)
        if not courselist:
            prereqsfor.append("This course is not a pre-requisite for any course")
        for c in courselist:
            prereqsfor.append(str(c[0]))
    return prereqsfor

def showCourseDesc(coursecode):

    connection = db.create_connection(db.database)
    with connection:
        coursedesc = db.getCourseDesc(connection, coursecode)
        for c in coursedesc:
            description = str(c[0])
    return description


def listCoursesOffered():
    allcourses = []
    connection = db.create_connection(db.database)
    with connection:
        courselist = db.getCoursesOffered(connection)
        for c in courselist:
            allcourses.append(str(c[0]))
    return allcourses

def canTakeCourse(takenalready):
    allPrereqfor=[]
    eligiblefor = []
    for ta in takenalready:
        allPrereqfor.extend(showPrerequisitesFor(ta))
    allPrereqforSet = set(allPrereqfor)
    for a in allPrereqforSet:
        if(set(showPrerequisites(a)).issubset(set(takenalready))):
            eligiblefor.append(str(a))
    return list(set(eligiblefor) - set(takenalready))


def createPreReqs(coursecode):
    courses = []
    prereqs = []
    coursedesc = showCourseDesc(coursecode)
    if re.search("Corequisite:|Corequisites:", coursedesc):
        descsplit = re.split("(Corequisite:|Corequisites:)(?i)", coursedesc)
    else:
        descsplit = re.split("(Course Credit (Exclusion:|Exclusions:))(?i)", coursedesc)
    if re.search("Integrated with: [A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0]):
        descsplit = re.split("Integrated with: [A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0])
        prereq = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[1])
    elif re.search("(Prerequisite:|Prerequisites:)", descsplit[0]):
        prereq = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0])
    else:
        prereq = "X"
    for p in prereq:
        if p in listCoursesOffered():
            courses.append(coursecode)
            prereqs.append(str(p))
    courselist = zip(courses, prereqs)
    return courselist

def addCourseAndPrereqs(courselist):
    connection = db.create_connection(db.database)
    with connection:
        for course in courselist:
            db.create_coursePrereqs(connection, course)
        connection.commit()

def main():
    '''allcourses = listCoursesOffered()
    for course in allcourses:
        courseandPrereqs = createPreReqs(course)
        addCourseAndPrereqs(courseandPrereqs)'''
    print(createPreReqs('LE/EECS 4101'))
if __name__ == '__main__':
    main()