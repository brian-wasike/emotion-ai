import requests

def emotion_detector(text_to_analyze):
    """
    This function takes in a string and returns the emotion of the text.
    """

    # URL for the API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input json for the API
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url=url, headers=headers, json=input_json, timeout=60)

    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
    
    response_data = response.json()

    emotions = response_data['emotionPredictions'][0]['emotion']

    output_emotions = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }

    return output_emotions