from flask import Flask, render_template, request
import logging
import sys

import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# example!
@app.route('/students', methods=['GET', 'POST'])
def students():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            sID = request.form["sID"]
            sUPRC = request.form["sUPRC"]
            sName = request.form["sName"]
            sAddress = request.form["sAddress"]
            sPhoneNumber = request.form["sPhoneNumber"]
            sSex = request.form["sSex"]
            sBDate = request.form["sBDate"]
            sDepartment = request.form["sDepartment"]
            sMajor = request.form["sMajor"]
            _db.insert_student(sID, sUPRC, sName, sAddress, sPhoneNumber, sSex, sBDate, sDepartment, sMajor)
            print('Student inserted', file=sys.stdout)
            
            studs = _db.list_students()
            print('Listing all the students', file=sys.stdout)

            return studs

        else:
            if request.method == "GET":
                student_id = request.values.get('sID', '')
                studs = _db.list_student(student_id)
                print('Listing student given info ' + student_id , file=sys.stdout)
                return studs

    res = db_query()

    return render_template('students.html', result=res, content_type='application/json')

@app.route('/del_students', methods=["POST"])
def del_students():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                student_id = request.form["sID"]
                studs = _db.delete_student(student_id)
        studs = _db.list_students()
        print('Listing all students from normal query', file=sys.stdout)
        return studs

    res = db_query()

    return render_template('students.html', result=res, content_type='application/json')


@app.route('/professor', methods=['GET', 'POST'])
def professor():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            pID = request.form["pID"]
            pUPRC = request.form["pUPRC"]
            pName = request.form["pName"]
            pAddress = request.form["pAddress"]
            pPhoneNumber = request.form["pPhoneNumber"]
            pSex = request.form["pSex"]
            pBDate = request.form["pBDate"]
            _db.insert_professor(pID, pUPRC, pName, pAddress, pPhoneNumber, pSex, pBDate)
            print('Professor inserted', file=sys.stdout)

            profs = _db.list_professors()
            print('Listing all the professors', file=sys.stdout)

            return profs

        else:
            if request.method == "GET":
                professor_id = request.values.get('pID', '')
                profs = _db.list_professor(professor_id)
                print('Listing professor given info ' + professor_id , file=sys.stdout)
                return profs

    res = db_query()

    return render_template('professor.html', result=res, content_type='application/json')


@app.route('/del_proffesors', methods=["POST"])
def del_proffesors():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                professor_id = request.form["pID"]
                profs = _db.delete_professor(professor_id)
        profs = _db.list_professors()
        print('Listing all Proffesors from normal query', file=sys.stdout)
        return profs

    res = db_query()

    return render_template('professor.html', result=res, content_type='application/json')


@app.route('/department', methods=['GET', 'POST'])
def department():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            dId = request.form["dId"]
            dName = request.form["dName"]
            dNumber = request.form["dNumber"]
            dPhoneNumber = request.form["dPhoneNumber"]
            dOffice = request.form["dOffice"]
            _db.insert_department(dId, dName, dNumber, dPhoneNumber, dOffice)
            print('Department inserted', file=sys.stdout)

            deps = _db.list_departments()
            print('Listing all the departments', file=sys.stdout)

            return deps

        else:
            if request.method == "GET":
                department_name = request.values.get('dName', '')
                deps = _db.list_department(department_name)
                print('Listing department given info ' + department_name , file=sys.stdout)
                return deps

    res = db_query()

    return render_template('department.html', result=res, content_type='application/json')


@app.route('/del_departments', methods=["POST"])
def del_departments():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                department_id = request.form["dId"]
                deps = _db.delete_department(department_id)
        deps = _db.list_departments()
        print('Listing all Departments from normal query', file=sys.stdout)
        return deps

    res = db_query()

    return render_template('department.html', result=res, content_type='application/json')


@app.route('/CourseBySID', methods=['GET','POST'])
def CourseBySID():
    def db_query():
        _db = db.Database()
   
        if request.method == "GET":
            student_id = request.values.get('sID', '')
            cbySid = _db.list_coursebysid(student_id)
            print('Listing Course Name of Given Student', file=sys.stdout)

            return cbySid

    res = db_query()

    return render_template('CourseBySID.html', result=res, content_type='application/json')


@app.route('/TiemNomyNom', methods=['GET','POST'])
def TiemNomyNom():
    def db_query():
        _db = db.Database()
   
        if request.method == "GET":
            professor_id = request.values.get('pID', '')
            TiNoyNo = _db.list_profbyid(professor_id)
            print('Listing Proffesor Name, Id and available time of Given Professor', file=sys.stdout)

            return TiNoyNo

    res = db_query()

    return render_template('TiemNomyNom.html', result=res, content_type='application/json')


@app.route('/Ecoas', methods=['GET','POST'])
def Ecoas():
    def db_query():
        _db = db.Database()
   
        if request.method == "GET":
            professor_id = request.values.get('pID', '')
            ecos = _db.list_ecoasbyid(professor_id)
            print('Listing course ecoa grade and more data by given professor', file=sys.stdout)

            return ecos

    res = db_query()

    return render_template('Ecoas.html', result=res, content_type='application/json')

@app.route('/Phistory', methods=['GET','POST'])
def Phistory():
    def db_query():
        _db = db.Database()
   
        if request.method == "GET":
            professor_id = request.values.get('pID', '')
            pHis = _db.list_history(professor_id)
            print('Listing Professor History', file=sys.stdout)

            return pHis

    res = db_query()

    return render_template('Phistory.html', result=res, content_type='application/json')