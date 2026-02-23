from flask import *
# imported pymysql after installing it in the terminal
import pymysql
import pymysql.cursors
import os#it aloows python code to talk / communicate with the operating system (linux,windows,macos)
app=Flask (__name__)
# configure our upload folder 
app.config['UPLOAD_FOLDER'] = 'static/images'
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

# sign in route
@app.route('/api/add_product',methods=['POST'])
def add_product():
    # extract product data
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    product_cost = request.form['product_cost']
    product_photo = request.files['product_photo']
    # extract the file name
    filename=product_photo.filename
    # specify computer path whjere the image will be saved (STATIC/IMAGES)
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    product_photo.save(photo_path)
    # connect database
    connection=pymysql.connect(host='localhost',user='root',password='',database='dailyyoughurts_Swala')
    # create cursor
    cursor = connection.cursor()
      # do the sql querry
    sql = "insert into Products_details(product_name,product_description,product_cost,product_photo)values(%s,%s,%s,%s)"
    data=(product_name,product_description,product_cost,filename)
    # execute the data
    cursor.execute(sql,data)
    # save the images
    connection.commit()
    return jsonify({'message':'product added successfully'})
# sign in route
@app.route('/api/get_Products_details',methods=['GET'])
def get_products():
    connection=pymysql.connect(host='localhost',user='root',password='',database='dailyyoughurts_Swala')
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    sql="select * from Products_details"
    cursor.execute(sql)
    # fetch alll the records in a dictionary format
    Products_details=cursor.fetchall()
    return jsonify(Products_details)
if __name__=='__main__':
    app.run(debug=True)
