import requests, json

def emotion_detector(text_to_analyse) :
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    top_score = 0;
    top_emotion = 'None';
    for emotion in emotions.keys():
        if emotions[emotion] > top_score:
            top_emotion = emotion
            top_score = emotions[emotion]
    emotions["dominant_emotion"] = top_emotion
    return emotions