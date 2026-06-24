from flask import *
# initialize the application 
app=Flask(__name__)
# Defineroute/endpoint
@app.route("/api/home")
# Define the function 
def home ():
    return jsonify({"message":"welcome home"})

@app.route("/api/services")
def sevices():
    return jsonify({"message":"welcome to services"})

@app.route("/api/about")
def about():
    return jsonify({"message":"welcome about"})


@app.route("/api/contact")
def contact():
    return jsonify({"message":"Cnotact us for more information"})

@app.route("/api/products")
def products():
    return jsonify({"message":"products available"})

@app.route("/api/students")
def students():
    return jsonify({"message":"list of students"})

@app.route("/api/courses")
def courses():
    return jsonify({"message":"courses offerd"})

@app.route("/api/teachers")
def teachers():
    return jsonify({"message":"list of teachers"})

@app.route("/api/news")
def news():
    return jsonify({"message":"latest news update"})

@app.route("/api/gallery")
def gallery():
    return jsonify({"message":"gallary images"})

@app.route("/api/faq")
def faq():
    return jsonify({"message":"frequently asked qn"})

@app.route("/api/profile")
def profile():
    return jsonify({"mesage":"Student profile information"})
@app.route("/api/events")
def event():
    return jsonify({"message":"Upcoming events"})
@app.route("/api/library")
def library():
    return jsonify({"message":"library resourses available"})
@app.route("/api/addition", methods=["post"])
def addition():
    number1=request.form ["number1"]
    number2=request.form["number2"]
    answer =int(number1)+int(number2)
    return jsonify({"answer":answer})
@app.route("/api/subtract", methods=["post"] )
def subtract():
    number1=request.form ["number1"]
    number2= request.form["number2"]
    answer=int(number1)-int(number2)
    return jsonify({"answer":answer})

@app.route("/api/division", methods=["post"]) 
def divison():
    number1=request.form ["number1"]
    number2=request.form ["number2"]
    answer=(number1)/(number2)
    return jsonify({"answer":answer})
@app.route("/api/multiplication", methods=["post"])
def multplication():
    number1=request.form ["number1"]
    number2=request.form["number2"]
    answer=int(number1)*int(number2)
    return jsonify({"amswer":answer})







# run the application
app.run(debug=True)

