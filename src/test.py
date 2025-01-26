
import json
import json5
def extractData(response):
    # Check if response is already a dictionary
    if isinstance(response, str):
        # Parse the response string into a dictionary
        response_dict = json.loads(response)
    elif isinstance(response, dict):
        # If it's already a dictionary, use it directly
        response_dict = response
    else:
        raise TypeError("The response must be a JSON string or a dictionary")

    # Access the required field
    message_content = response_dict["choices"][0]["message"]["content"]
    print(type(message_content))


    print("Message Content:", message_content)
    # You can process `message_content` further as needed

# Example Usage
response={
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": 0,
            "message": {
                "content": "Here is the analysis in JSON format:\n\n{\n\"topic\": \"School-related inquiry\",\n\"resolution_status\": \"No\", // No resolution was reached as there seems to be a language barrier and unclear question\n\"communication_modes\":\n{\n\"customer\": {\n\"type\": \"Formal\",\n\"tone\": \"Polite\"\n},\n\"agent\": {\n\"type\": null,\n\"tone\": null\n}\n},\n\"improvement_suggestions\":\n[\n{\n\"suggestion\": \"Verify the customer's understanding of English or offer language assistance if needed.\",\n\"value\": 1.0\n},\n{\n\"suggestion\": \"Ask for clarification on what 'school se kya bola' means to better understand the customer's inquiry.\"\n}\n]\n}",
                "role": "assistant"
            },
            "references": 0
        }
    ],
    "created": 1737764653,
    "id": "placeholder",
    "model": "Llama 3 8B Instruct",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 143,
        "prompt_tokens": 121,
        "total_tokens": 264
    }
}

# Call the function with a dictionary
extractData(response)


Data = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": 0,
            "message": {
                "content": "{\n\"topic\": \"Greetings and Introduction\",\n\"resolution_status\": \"No\",\n\"communication_modes\": {\n\"customer\": {\"tone\": \"Formal\", \"style\": \"Polite\"},\n\"agent\": {\"tone\": \"Friendly\", \"style\": \"Welcoming\"}\n},\n\"improvement_suggestions\": [\n{\" suggestion\": \"Verify customer's language preference at the start of the call to ensure accurate communication.\"}\n]",
                "role": "assistant"
            },
            "references": 0
        }
    ],
    "created": 1737909833,
    "id": "placeholder",
    "model": "Llama 3 8B Instruct",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 85,
        "prompt_tokens": 126,
        "total_tokens": 211
    }
}