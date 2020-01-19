from flask import Flask, render_template, request, jsonify
import dataRetriever as dr
import json
from models import degreeTreeInputForm as dtform

app = Flask(__name__)
allcourses = dr.listCoursesOffered()
allc = json.dumps(allcourses)

@app.route("/")
def home():
        return render_template('home.html', courses = allc)

@app.route("/courses", methods=['GET', 'POST'])
def courses():
    if request.method == 'GET':
        results = []
        userinput = request.args.get('courseinput')
        print(userinput)
        resultprereqs = dr.showPrerequisites(userinput)
        resultprereqsfor = dr.showPrerequisitesFor(userinput)
        results.append(" ".join(resultprereqs))
        results.append(" ".join(resultprereqsfor))
        return render_template('courses.html', results=results, courses = allc)

@app.route("/degreetree", methods=['GET'])
def degreetree():
    form = dtform(request.form)
    return render_template('degreetree.html',form=form, courses = allc)

@app.route("/degreetree", methods=['GET','POST'])
def buildDegreeTree():
    form = dtform(request.form)
    takenalready = request.form.getlist("x[]")
    cantake = dr.canTakeCourse(takenalready)
    cho = [(c, c) for c in takenalready]
    form.cantakecourse.choices = cho
    print(takenalready)
    print(cho)

    return render_template('degreetree.html', form=form, courses=allc)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)