from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import re
import dbConnection as db
from selenium.common.exceptions import NoSuchElementException

courses = []
prereqs = []
course_code = []
course_title = []
course_desc = []
course_credits = []
optionsnum = 204

def courseselection():
    driver = webdriver.Chrome("C:\Windows\chromedriver")
    driver.maximize_window()
    driver.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')

    driver.find_element_by_link_text("Subject").click()
    return driver

def getLinks(driver, i):
    pathh = "//select/option[@value='"+str(i)+"']"
    driver.find_element_by_xpath(pathh).click()
    driver.find_element_by_xpath("//td/input[@value='Search Courses']").click()
    pagesource = driver.page_source
    soup = bs(pagesource, "html.parser")
    links = soup.find_all('a', text="Fall/Winter 2019-2020 Course Schedule")
    return links

#this doesn't take care of 'or' cases hence we get more prerqs than desired
def getPrereqs(driver, links):
    for link in links:
        driver.get('https://w2prod.sis.yorku.ca/'+link['href'])
        coursepagesource = driver.page_source
        coursepagesoup = bs(coursepagesource, "html.parser")
        paratags = coursepagesoup.find_all('p')
        coursecode = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]",paratags.pop(0).get_text()).pop(0)
        coursedesc = paratags.pop(2).get_text()
        if re.search("Corequisite:|Corequisites:", coursedesc):
            descsplit = re.split("(Corequisite:|Corequisites:)(?i)", coursedesc)
        else:
            descsplit = re.split("(Course Credit (Exclusion:|Exclusions:))(?i)", coursedesc)
        if re.search("(Prerequisite:|Prerequisites:)", descsplit[0]):
            prereq = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]", descsplit[0])
        else:
            prereq = "X"
        for p in prereq:
            courses.append(coursecode)
            prereqs.append(str(p))
    courselist = zip(courses, prereqs)
    return courselist

def getCourseInfo(driver, links):
    for link in links:
        driver.get('https://w2prod.sis.yorku.ca/' + link['href'])
        coursepagesource = driver.page_source
        coursepagesoup = bs(coursepagesource, "html.parser")
        paratags = coursepagesoup.find_all('p')
        coursedesc = paratags.pop(3).get_text()
        course_desc.append(coursedesc)
        paraheading = coursepagesoup.find('p', {"class": "heading"}).get_text()
        code = re.findall("[A-Z][A-Z]/[A-Z][A-Z][A-Z]* *[0-9][0-9][0-9][0-9]",paraheading).pop(0)
        course_code.append(code)
        credits = re.findall("[0-9]\.[0-9]+", paraheading).pop(0)
        course_credits.append(credits)
        stitle = re.split("[0-9]\.[0-9]+", paraheading)
        title = (stitle.pop(len(stitle) - 1)).strip()
        course_title.append(title)
        courselist = zip(course_code, course_title, course_desc, course_credits)

    return courselist

def addCoursestoDB(courselist):
    connection = db.create_connection(db.database)
    with connection:
        for course in courselist:
            db.create_courses_main(connection, course)
        connection.commit()

def main():
    driver = courseselection()
    for i in range(1):
        print("Currently on option# "+str(i))
        links = getLinks(driver, i)
        courselist = getCourseInfo(driver, links)
        addCoursestoDB(courselist)
        driver.quit()
        driver = courseselection()

if __name__ == '__main__':
    main()