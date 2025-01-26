import requests
import json

def analyze_text(transcription):
    # Define the API endpoint
    url = "http://localhost:4891/v1/chat/completions"

    # Create the payload for the request
    payload = {
        "model": "Llama 3 8B Instruct",
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Analyze the following call transcription between an agent and a customer:\n\n"
                    f"{transcription}\n\n"
                    f"Provide the analysis in clear JSON format with the following fields:\n"
                    f"- topic: the conversation's topic.\n"
                    f"- resolution_status: 'Yes' or 'No', and a brief explanation.\n"
                    f"- communication_modes: the tone or style of communication for both customer and agent.\n"
                    f"- improvement_suggestions: Suggest how the call can be improved by Agent."
                )
            }
        ],
        "max_tokens": 500,
        "temperature": 0.3
    }


    # Send the POST request
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

    # Process and print the response
    if response.status_code == 200:
        response_data = response.json()
        return(json.dumps(response_data, indent=4))
    else:
        return(f"Error: {response.status_code}")
        
