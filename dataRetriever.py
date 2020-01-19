import dbConnection as db

'''
STILL HAVE TO DEAL WITH 'OR' PREREQS, MISSING COURSES
'''

def showPrerequisites(coursecode):
    prereqs = []
    connection = db.create_connection(db.database)
    with connection:
        courselist= db.getPrerequisites(connection, coursecode)
        for c in courselist:
            prereqs.append(str(c[0]))
    return prereqs

def showPrerequisitesFor(prereq):
    prereqsfor = []
    connection = db.create_connection(db.database)
    with connection:
        courselist = db.getPrerequisteFor(connection, prereq)
        for c in courselist:
            prereqsfor.append(str(c[0]))
    return prereqsfor

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
            eligiblefor.append(a)
    return eligiblefor


def main():
    print(showPrerequisites("LE/EECS 2021"))

    print("___________________")
    print(showPrerequisites("LE/EECS 3481"))
    print("___________________")
    l = showPrerequisites("LE/EECS 3101")
    print(l)
    list = canTakeCourse(l)
    for r in list:
        print(r)


if __name__ == '__main__':
    main()