import pymysql
import sys

class Database:
    def __init__(self):
        # host = "127.0.0.1"
        host = "localhost"
        user = "root"
        #password = "root"
        db = "residence"
        port = 3306

        self.con = pymysql.connect( host=host, 
                                    user=user, 
                                    #password=password, 
                                    db=db, 
                                    port=port, 
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def login(self, sId, sPass):
        query = '''
            SELECT *
            FROM usuario
            '''
        if sId != '':
            query += 'WHERE sID = {}'.format(sId)
            query += 'AND sPass = {}'.format(sPass)

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

# SELECT * FROM login_details WHERE username = ? AND password = ?