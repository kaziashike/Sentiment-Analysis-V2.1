import json


def extractData(response):
    # Parse the response string into a dictionary
    response_dict = json.loads(response)

    # Access the required field
    message_content = response_dict["choices"][0]["message"]["content"]

    print("Message Content:", message_content)
    # You can process `message_content` further as needed
