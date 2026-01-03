from flask import Flask, render_template, request
import os

app = Flask(__name__)

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

# IMPORTANT: Render uses gunicorn, not app.run()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

