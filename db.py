import pymysql
import sys

class Database:
    def __init__(self):
        # host = "127.0.0.1"
        host = "localhost"
        user = "root"
        #password = "root"
        db = "tecuniversity"
        port = 3306

        self.con = pymysql.connect( host=host, 
                                    user=user, 
                                    #password=password, 
                                    db=db, 
                                    port=port, 
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()


    def list_students(self):
        query = '''
	            SELECT * 
	            FROM Students
	            '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        
        return result

    def list_student(self, student_id):
        query = '''
                SELECT *
                FROM Students
                '''
        if student_id != '':
            query += 'WHERE sID = {}'.format(student_id)
            
        query+= '''
                order by sID
                '''

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result
    
    def insert_student(self,sID, sUPRC, sName, sAddress, sPhoneNumber, sSex, sBDate, sDepartment, sMajor):
        query = '''
                INSERT INTO Students (sID, sUPRC, sName, sAddress, sPhoneNumber, sSex, sBDate, sDepartment, sMajor)
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}')
                '''.format(sID, sUPRC, sName, sAddress, sPhoneNumber, sSex, sBDate, sDepartment, sMajor)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_student(self, student_id):
        query = '''
                DELETE FROM Students
                WHERE sID = {}
                '''.format(student_id)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def list_professors(self):
        query = '''
                SELECT *
                FROM Professor
                '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        
        return result

    def list_professor(self, professor_id):
        query = '''
                SELECT *
                FROM Professor
                '''
        if professor_id != '':
            query += 'WHERE pID = {}'.format(professor_id)
        
        query+= '''
                order by pID
                '''

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
            
        return result

    def insert_professor(self,pID, pUPRC, pName, pAddress, pPhoneNumber, pSex, pBDate):
        query = '''
                INSERT INTO Professor (pID, pUPRC, pName, pAddress, pPhoneNumber, pSex, pBDate)
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}')
                '''.format(pID, pUPRC, pName, pAddress, pPhoneNumber, pSex, pBDate)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_professor(self, professor_id):
        query = '''
                DELETE FROM Professor
                WHERE pID = {}
                '''.format(professor_id)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def list_departments(self):
        query = '''
                SELECT *
                FROM Department
                '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
        
        return result

    def list_department(self, department_name):
        query = "SELECT * FROM Department "
        if department_name != '':
            query += "WHERE dName = '{}'".format(department_name)
        
        query+= '''
                order by dId
                '''

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()
            
        return result

    def insert_department(self,dId, dName, dNumber, dPhoneNumber, dOffice):
        query = '''
                INSERT INTO Department (dId, dName, dNumber, dPhoneNumber, dOffice)
                VALUES ('{}', '{}', '{}', '{}', '{}')
                '''.format(dId, dName, dNumber, dPhoneNumber, dOffice)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_department(self, department_id):
        query = '''
                DELETE FROM Department
                WHERE dId = {}
                '''.format(department_id)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()


    def list_coursebysid(self, student_id):
        query = '''
                SELECT c.cName, s.sName 
                FROM students s, takecourse tk, course c, groupp g 
                WHERE s.sID = tk.sID 
                and tk.tcGroupNumber = g.gNumber 
                and g.cNumber = c.cNumber
                '''
        if student_id != '':
            query += 'AND s.sID = {}'.format(student_id)
            
        query+= '''
                order by s.sID
                '''

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_profbyid(self, proffesor_id):
        query = '''
               SELECT p.pID, p.pName, s.hTime
               from schedule s, professorschedule ps, professor p 
               WHERE s.hId = ps.hId
               AND ps.pID = p.pID  
                '''
        if proffesor_id != '':
            query += 'AND p.pID = {}'.format(proffesor_id)

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_ecoasbyid(self, proffesor_id):
        query = '''
             SELECT g.gEcoa,c.cNumber, c.cName, g.gNumber, g.gSemester, g.gYear 
             FROM professor p, groupp g, course c 
             WHERE p.pID = g.pID 
             AND g.cNumber = c.cNumber 
                '''
        if proffesor_id != '':
            query += 'AND p.pID = {}'.format(proffesor_id)

        query+= '''
                ORDER BY g.gYear, g.gSemester, c.cNumber, g.gID
                '''

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_history(self, proffesor_id):
        query = '''
                SELECT p.pID, p.pName, c.cName
                FROM professor p, course c, groupp gp
                WHERE gp.cNumber = c.cNumber
                and gp.pID = p.pID
                '''
        if proffesor_id != '':
            query += 'AND p.pID = {}'.format(proffesor_id)

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result
