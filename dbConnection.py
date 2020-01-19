import sqlite3
from sqlite3 import Error

database = r"C:\Users\Harry\PycharmProjects\YORKUVXYZ_DB\coursesDB.db"
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_course(conn, course):
    sql = '''INSERT OR IGNORE INTO course_list(Course_Code, Prerequisite) values(?,?)'''
    curr = conn.cursor()
    curr.execute(sql, course)
    #return cur.lastrowid

def getPrerequisites(conn, coursecode):
    curr = conn.cursor()
    curr.execute("SELECT Prerequisite from course_list WHERE Course_Code=?",[coursecode])
    return curr.fetchall()


def getPrerequisteFor(conn, prereq):
    curr = conn.cursor()
    curr.execute("SELECT Course_Code from course_list WHERE Prerequisite=?",[prereq])
    return curr.fetchall()

def getCoursesOffered(conn):
    curr = conn.cursor()
    curr.execute("SELECT DISTINCT Course_Code from course_list")
    return curr.fetchall()

def main():
    create_course_list_table = '''CREATE TABLE IF NOT EXISTS course_list(id integer PRIMARY KEY, Course_Code text NOT NULL, Prerequisite text,
                                    UNIQUE(Course_Code, Prerequisite))'''
    #create a DB Connection
    conn = create_connection(database)
    #create tables
    if conn is not None:
        create_table(conn, create_course_list_table)
    else:
        print("Error! cannot create the database connection")
    #getPrerequisites(conn,"SC/BIOL 2050" )

if __name__ == '__main__':
    main()