from flask import*
import pymsql*

#intilialize the application
app= Flask(__name__)
# define the route/endpoint
@app.route("/api/signup",methods=["POST"])
# define the function 
def sign():
    # get user inputs from the form 
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]
    # connect to database
    connect=pymsql.connect(host="root",username="localhost",password=""database="modcomalfred")








# run the application
app.run(debug=True)