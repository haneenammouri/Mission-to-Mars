# from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
# import scrape_mars

# # Create an instance of Flask
# app = Flask(__name__)

# # Use PyMongo to establish Mongo connection

# mongo = PyMongo(app, uri="mongodb://localhost:27017/mar_app")

# # Route to render index.html template using data from Mongo
# @app.route("/scrape")
# def scrape():
#     # look up upsert
#     mars = mongo.db.mars
#     mars_data = scrape_mars.scrape()
#     mars.update({}, mars_data, upsert=True)
#     return redirect("/", code=302)
# # i can try to call each funtion alone but if i do id need to increase my collections as in below and make each dictionar/function in its own mongo db
# #Create a root route / that will query your 
# # #Mongo database and pass the mars data into an HTML template to display the data.

# @app.route("/")
# def home():
# #Find one record of data from the mongo database
#     destination_data = mongo.db.collection.find_one()
#     Return render_template("index.html", MARS=destination_data)
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import selenium 

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017")

@app.route("/")
def index():
    mars = mongo.db
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db
    mars_data = scrape_mars.scrape()
    mars.update({}, mars, upsert=True)
    mars.update({}, mars_data, upsert=True)

    return redirect("http://localhost:27017/", code=302)

# @app.route("/get_news")
# def get_news():
#     mars = mongo.db.mars 
#     mars_data1 = scrape_mars.get_news()
#     mars.update({}, mars_data1, upsert=True)
#     return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
