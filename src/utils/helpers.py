def format_api_request(transcription):
    return {
        "transcription": transcription,
        "language": "bn"
    }

def handle_api_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API call failed with status code: {}".format(response.status_code))