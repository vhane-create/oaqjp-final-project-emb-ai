"""Serve the emotion detector through the supplied Flask interface."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the starter application's home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Return emotion scores for text supplied by the web interface."""
    result = emotion_detector(request.args.get("textToAnalyze", ""))
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
