from flask import*
import pymysql

#intilialize the application
app=Flask(__name__)

# define the route/endpoint
@app.route("/api/signup",methods=["POST"])

# define the function 
def signup():
    # get user inputs from the form 
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]
    # connect to database
    connection = pymysql.connect(host="localhost",user="root",password="",database="modcomalfred") 
    #define the cusor
    cursor=connection.cursor()

    #define SQL to insert user
    sql="insert into users(username,password,email,phone)Value(%s,%s,%s,%s)"
    #define data coming from the form
    data= (username,password,email,phone)

    cursor.execute(sql,data)
    #commit/save  changes
    connection.commit()

    return jsonify({"message":"user registered successfully"})


# member sign in /log in
# define route/endpoint
@app.route("/api/signin",methods=["POST"])
# define the function 
def signin():
    #get the user input from the form
    email=request.form["email"]
    password=request.form["password"]

    # connection to database
    connection = pymysql.connect(host="localhost",user="root",password="",database="modcomalfred")
    # define the cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # select sql to select user 
    sql="select * from users where email= %s and password = %s "
    # define u data
    # NB:its from step 3
    data=(email,password)
    # execute/querry
    cursor.execute(sql,data)
    # wrong email and password
    if cursor.rowcount == 0 :
        return jsonify({"message" : "invalid email or password"})
    #  corect  email and password
    if cursor.rowcount == 1 :
        # fetch  the user 
        user =cursor.fetchone()
    return jsonify({"message":"log in successful", "user":user})

    









#run the application
app.run(debug=True)





































































































































# run the application
app.run(debug=True)