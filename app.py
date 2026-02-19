from flask import *
# imported pymysql after installing it in the terminal
import pymysql
import pymysql.cursors
app=Flask (__name__)
@app.route('/api/signup',methods=['POST'])
def signup():
    # extract values posted in the request and store them in a variable
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    # connection to database
    connection = pymysql.connect(host='localhost',user='root',password='',database='dailyyoughurts_Swala')

    # cursor object = initialize connection/manipulation of the database
    cursor = connection.cursor()
    # sql querry to insert
    sql = 'INSERT INTO users(username,password,email,phone) VALUES(%s,%s,%s,%s)'
    # prepare data to replace the placeholders
    data = (username,email,password,phone)
    # we use the cursor to execute the sql and the data
    cursor.execute(sql,data)
    # save the changes
    connection.commit()
    return jsonify({'success':'thanks for joining'})
# sign in route
@app.route('/api/signin')
def signin():
    # extract host data
    username=request.form['username']
    password=request.form['password']
    # connect database
    connection = pymysql.connect(host='localhost',user='root',password='',database='dailyyoughurts_Swala')
    # create cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # do the sql querry
    sql ='select * from users where username = %s and password = %s'
    # preapare data to replace placeholders
    data = (username,password)
    # execute data
    cursor.execute(sql,data)
    # check if there were rows found
    count=cursor.rowcount
    if count ==0:# if the rows is zero == invalid cridentials
        return jsonify({'message':'Log in failed'})
    else:
         # if the cursor has returned a valid user or atleast a row
        user = cursor.fetchone()
    
    return jsonify({'message':'log in successful','user':user})
if __name__=='__main__':
    app.run(debug=True)
