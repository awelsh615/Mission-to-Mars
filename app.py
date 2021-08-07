from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)

# Define the first route
@app.route("/")
def index():
    # Uses pymongo to find the mars collection in our database
    mars = mongo.db.mars.find_one()
    # Tells Flask to return an HTML template using an index.html file (mars = mars tells python to use the mars collection in MongoDB)
    return render_template('index.html', mars = mars)

# Define the scrape route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == '__main__':
    app.run()