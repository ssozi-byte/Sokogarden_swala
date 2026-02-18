from flask import *
# imported pymysql after installing it in the terminal
import pymysql
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
if __name__=='__main__':
    app.run(debug=True)