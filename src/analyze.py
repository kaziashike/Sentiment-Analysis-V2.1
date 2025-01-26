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
                f"Respond **strictly** with valid JSON. No extra comments, explanations, or text outside of the JSON structure.\n\n"
                f"JSON format:\n"
                f"{{\n"
                f"  \"topic\": \"string\",\n"
                f"  \"resolution_status\": \"string\",\n"
                f"  \"communication_modes\": {{\n"
                f"    \"customer\": {{\"tone\": \"string\", \"style\": \"string\"}},\n"
                f"    \"agent\": {{\"tone\": \"string\", \"style\": \"string\"}}\n"
                f"  }},\n"
                f"  \"improvement_suggestions\": [\n"
                f"    {{\"suggestion\": \"string\", \"reason\": \"string\"}}\n"
                f"  ]\n"
                f"}}"
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
        
