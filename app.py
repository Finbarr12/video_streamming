from flask import Flask,render_template
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 