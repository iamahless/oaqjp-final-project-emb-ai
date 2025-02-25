'''Deploy a Flask application that enables users to input
a text string for analysis, identifying the most likely
emotion from a set of five possible emotions.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    '''Get the text input from the user, analyze it using the emotion detector,
    and return a response showing the confidence scores for all emotions
    along with the dominant emotion.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again"
    response_str = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response_str

@app.route("/")
def render_index_page():
    '''Display the index page where users can input a text string for
    analysis and view the results.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
