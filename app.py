# Flask is a web microframework that helps developers build a web application. The Pythonic tools and libraries it comes with provide the means to create anything from a small webpage or blog or something large enough for commercial use.

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# database name is mars_app

# tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
mongo = PyMongo(app)
# is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".
# print(f"mongo db: {mongo}")

# set up routes


@app.route("/")
def index():
    # find the collection mars_data in mars_app database
    mars = mongo.db.mars_app.find_one()
    return render_template("index.html", mars=mars)
    # tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars_app
    mars_data = scraping.scrape_all()
    # for data in mars_data.mars_hemispheres:
    #     mars.insert_one(data)
    mars.update({}, mars_data, upsert=True)
    # print(mars_data)
    return redirect('/', code=302)
    # return "Data Scrapping Complete!"


# mongo.update(query_parameter, data, options)

if __name__ == "__main__":
    app.run(debug=True)
    # print(scraping.scrape_all())
