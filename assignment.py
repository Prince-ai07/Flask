# import the flask framework
from flask import *
import os

# Import the pymysql module - It helps us create a connection between python flask and mysql database
import pymysql


# Below we create a web server based application
app = Flask(__name__)

# configure the location to where your product images will be saved on your applcation
app.config["UPLOAD_FOLDER"] = "static/images"

# Below is the route for adding products
@app.route("/api/add_smartphone", methods = ["POST"])
def Addproducts():
    if request.method == "POST":
        # extract the data entered on the form
        name = request.form["name"]
        brand = request.form["brand"]
        model = request.form["model"]
        storage = request.form["storage"]
        ram = request.form["ram"]
        battery = request.form["battery"]
        price = request.form["price"]
        stock = request.form["stock"]

        # for the product photo we shall fetch it from files as shown below
        photo = request.files["photo"]

        # extract the filename of the product photo
        filename = photo.filename

        # by use of the os module(operating system) we can extract the file path where the image is currently saved
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # save the product photo image into the new location
        photo.save( photo_path)

        # print them out to test whether you are receiving the details sent with the request.
        # print(product_name, product_description, product_cost, product_photo)

        # establish a connection
        connection = pymysql.connect(host="localhost", user="root", password="", database="online")

        # create a cursor
        cursor = connection.cursor()

        # structure the sql query that will insert the product details to the database
        sql = "INSERT INTO smartphones(name, brand, model, storage, ram, battery, price, stock, photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # create a tuple that will hold the data from which are currently held onto the different variables declared

        data = (name, brand, model, storage, ram, battery, price, stock, filename)

        # use the cursor to execute the sql as you replace placeholders with the actual data
        cursor.execute(sql,data)

        # commit tha changes to the database
        connection.commit()



        return jsonify({"message" : "Product added successfully"})
        




# below we run the application
app.run(debug = True)

