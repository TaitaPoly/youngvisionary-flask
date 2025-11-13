# Importing flask 
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Path to carousel images
    carousel_folder = os.path.join(app.static_folder, "images/carousel")
    carousel_images = [f"images/carousel/{img}" for img in os.listdir(carousel_folder) if img.endswith((".jpg", ".png", ".jpeg"))]
    
    return render_template("index.html", carousel_images=carousel_images)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

