# Import Flask, render_template, request from the flask pramework package : 
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created: 
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : 
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments in mywebscript.js
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    emotions = emotion_detector(text_to_analyze)
    # Extract emotions from response
    if emotions is None:
        return "Invalid input! Try again."  
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = emotions["dominant_emotion"]
    
    return (
        "For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )   
    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)