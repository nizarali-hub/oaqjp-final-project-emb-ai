import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of a given text using the Watson NLP service.
    
    Args:
        text_to_analyze (str): The text string to be analyzed.
        
    Returns:
        str: The raw text response from the Emotion Detection service.
    """
    # Define the URL for the Watson Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required by the Watson NLP model
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the input text
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Execute the POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Return the text attribute of the response object
    return response.text
