import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

os.makedirs("uploads", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/demo", methods=["GET", "POST"])
def demo():
    metadata = None
    image_url = None

    if request.method == "POST":
        image = request.files["image"]
        if image:
            path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(path)

            image_url = path

            # 🔹 DEMO metadata (fake AI)
            metadata = {
                "title": "High quality stock photo",
                "keywords": "business, technology, modern, professional, clean",
                "description": "A professional high resolution image suitable for commercial use."
            }

    return render_template("demo.html", metadata=metadata, image=image_url)

if __name__ == "__main__":
    app.run()
