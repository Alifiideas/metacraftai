from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/demo", methods=["GET", "POST"])
def demo():
    metadata = None
    if request.method == "POST":
        metadata = {
            "title": "Beautiful Sunset Over Mountains",
            "keywords": "sunset, mountains, nature, landscape",
            "description": "A high-quality image of a colorful sunset over mountains."
        }
    return render_template("demo.html", metadata=metadata)

if _name_ == "_main_":
    app.run()
