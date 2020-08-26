from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    marsDB = mongo.db.mars_info.find_one()

    return render_template("index.html", marsDB = marsDB)

@app.route("/scrape")
def scraper():
    import scrape_mars
    marsData = scrape_mars.scrape()

    mongo.db.mars_info.update({}, mars_data_scrape, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
