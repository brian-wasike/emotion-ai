"""
A simple Flask application to run the Emotion Detection application.

This application will run a Flask server that will take in a text input and 
return the emotion of the text.

Author: Brian Wasike
"""

from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detection")

def run_app():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def emotion_view():
  
    text_to_detect = request.args.get('textToAnalyze')
    formated_response = emotion_detector(text_to_detect)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

if __name__ == "__main__":
    run_app()