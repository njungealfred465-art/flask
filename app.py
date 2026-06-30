from flask import*
import pymysql
import os
from flask_cors import CORS

#intilialize the application
app=Flask(__name__)

CORS(app)


app.config['UPLOAD_FOLDER'] = 'static/images'

# Create the folder if it does not exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Create a reusable function for uploading images

def save_image(file):
    filename = file.filename
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(photo_path)
    return filename

 
 

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
    connection = pymysql.connect(host="mysql-alfredg.alwaysdata.net",user="alfredg",password="modcom2026",database="alfredg_sokogarden+-+") 
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
    connection = pymysql.connect(host="mysql-alfredg.alwaysdata.net",user="alfredg",password="modcom2026",database="alfredg_sokogarden")
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



#1. define your route
@app.route("/api/addproduct",methods=["post"])

#2. define the function
def addproduct():

    #3. get user input from the form
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_cost=request.form["product_cost"]
    product_category=request.form["product_category"]
    product_photo=request.files["product_photo"]

    filename= save_image(product_photo)

    # 4.connection to database
    connection = pymysql.connect(host="mysql-alfredg.alwaysdata.net",user="alfredg",password="modcom2026",database="alfredg_sokogarden")

    # 5.define the cursor
    cursor=connection.cursor()

    # 6. define sql to insert products
    sql="insert into product_details(product_name,product_description,product_cost,product_category,product_photo) values(%s,%s,%s,%s,%s)"

    # 7.define u data 
    # NB:coming from step 3
    data=(product_name,product_description,product_cost,product_category,filename)

    # 8. excecute/run querry
    cursor.execute(sql,data)

    # 9.commit /save changes



    connection.commit()


    # 10.
    return jsonify({"message":"product added successfully"})



# fetch products/get products
# define route/endpoint
@app.route("/api/getproducts",methods=["Get"])
# def function
def getproducts():
    # connection to database
    connection = pymysql.connect(host="mysql-alfredg.alwaysdata.net",user="alfredg    ",password="modcom2026",database="alfredg_sokogarden")

    # define the cursor
    
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # define sql to fetch products
    sql="select * from product_details "

    #6.execute/run querry
    cursor.execute(sql)

    # 7. fetch all products
    allproducts=cursor.fetchall()

    # 8.return all products
    return jsonify(allproducts)






# MPESA INTERGRATION

    # Mpesa Payment Route 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
        if request.method == 'POST':
            # Extract POST Values sent
            amount = request.form['amount']
            phone = request.form['phone']

            # Provide consumer_key and consumer_secret provided by safaricom
            consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
            consumer_secret = "amFbAoUByPV2rM5A"

            # Authenticate Yourself using above credentials to Safaricom Services, and Bearer Token this is used by safaricom for security identification purposes - Your are given Access
            api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
            # Provide your consumer_key and consumer_secret 
            response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
            # Get response as Dictionary
            data = response.json()
            # Retrieve the Provide Token
            # Token allows you to proceed with the transaction
            access_token = "Bearer" + ' ' + data['access_token']

            #  GETTING THE PASSWORD
            timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')  # Current Time
            passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  # Passkey(Safaricom Provided)
            business_short_code = "174379"  # Test Paybile (Safaricom Provided)
            # Combine above 3 Strings to get data variable
            data = business_short_code + passkey + timestamp
            # Encode to Base64
            encoded = base64.b64encode(data.encode())
            password = encoded.decode()

            # BODY OR PAYLOAD
            payload = {
                "BusinessShortCode": "174379",
                "Password":password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": "1",  # use 1 when testing
                "PartyA": phone,  # change to your number
                "PartyB": "174379",
                "PhoneNumber": phone,
                "CallBackURL": "https://coding.co.ke/api/confirm.php",
                "AccountReference": "SokoGarden Online",
                "TransactionDesc": "Payments for Products"
            }

            # POPULAING THE HTTP HEADER, PROVIDE THE TOKEN ISSUED EARLIER
            headers = {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }

            # Specify STK Push  Trigger URL
            url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  
            # Create a POST Request to above url, providing headers, payload 
            # Below triggers an STK Push to the phone number indicated in the payload and the amount.
            response = requests.post(url, json=payload, headers=headers)
            print(response.text) # 
            # Give a Response
            return jsonify({"message": "An MPESA Prompt has been sent to Your Phone, Please Check & Complete Payment"})




    







    

















































#run the application
app.run(debug=True)





































































































































# run the application
app.run(debug=True)