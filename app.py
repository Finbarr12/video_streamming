from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:

        success, frame = camera.read()
        if not success:
            break
    else:
        ret, buffer = cv2.imdecode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(generate_frames, mimetype='multipart/x-mixed-replace;boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
