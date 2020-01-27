#This script runs queries on database and then used by dataRetriever

import sqlite3
from sqlite3 import Error

#PATH TO LOCAL SQLITE APP: C:\Users\NAME\Downloads\SQLiteDatabaseBrowserPortable
database = r"C:\Users\Harry\PycharmProjects\YORKUVXYZ_DB\coursesDB.db"
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#for course_prereqs table
def create_coursePrereqs(conn, course):
    sql = '''INSERT OR IGNORE INTO course_prereqs(Course_Code, Prerequisite) values(?,?)'''
    curr = conn.cursor()
    curr.execute(sql, course)

def getPrerequisites(conn, coursecode):
    curr = conn.cursor()
    curr.execute("SELECT Prerequisite from course_prereqs WHERE Course_Code=?",[coursecode])
    return curr.fetchall()

def getPrerequisteFor(conn, coursecode):
    curr = conn.cursor()
    curr.execute("SELECT Course_Code from course_prereqs WHERE Prerequisite=?",[coursecode])
    return curr.fetchall()

#for courses table
def create_courses_main(conn, course):
    sql = '''INSERT OR IGNORE INTO courses(Course_Code_Main, Course_Title, Course_Desc, Course_Credits) values(?,?,?,?)'''
    curr = conn.cursor()
    curr.execute(sql, course)

def getCoursesOffered(conn):
    curr = conn.cursor()
    curr.execute("SELECT Course_Code_Main from courses")
    return curr.fetchall()

def getCourseTitle(conn, coursecode):
    curr = conn.cursor()
    curr.execute("SELECT Course_Title from courses WHERE Course_Code_Main=?",[coursecode])
    return curr.fetchall()

def getCourseDesc(conn, coursecode):
    curr = conn.cursor()
    curr.execute("SELECT Course_Desc from courses WHERE Course_Code_Main=?",[coursecode])
    return curr.fetchall()

def main():
    create_course_prereqs_table = '''CREATE TABLE IF NOT EXISTS course_prereqs(id integer PRIMARY KEY, Course_Code text NOT NULL, Prerequisite text,
                                    UNIQUE(Course_Code, Prerequisite))'''

    create_courses_table = '''CREATE TABLE IF NOT EXISTS courses(id integer PRIMARY KEY, Course_Code_Main text NOT NULL, Course_Title text, Course_Desc text, Course_Credits integer,
                                    UNIQUE(Course_Code_Main))'''
    #create a DB Connection
    conn = create_connection(database)
    #create tables
    if conn is not None:
        create_table(conn, create_courses_table)
    else:
        print("Error! cannot create the database connection")


if __name__ == '__main__':
    main()