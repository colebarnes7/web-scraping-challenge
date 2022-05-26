# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create flask app
app = Flask(__name__)

# Set up Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Create a collection
mars_collection = mongo.db.mars


@app.route("/")
def index():
    # find one document from our mongo db and return it.
    mars_results = mars_collection.find_one()
    # pass those results to render_template
    return render_template("index.html", mars=mars_results)

@app.route("/scrape")
def scraper():
    # Call scrape function in scrape_mars file
    mars_data = scrape_mars.scrape()
    # Update collection with data being scraped or create and insert if collection doesn't exist
    mars_collection.update_one({}, {"$set": mars_data}, upsert=True)
    # return a message to our page so we know it was successful.
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)