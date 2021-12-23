import json
import os
from urllib import parse, request
from urllib.error import HTTPError
from dotenv import load_dotenv

load_dotenv()

url = "http://api.giphy.com/v1/gifs/random"

def api_request(message_id, tag):
    '''
    Request a GIF link from GIPHY for a certain tag.

        Parameters:
            message_id (str): Message ID of request
            tag (str): Tag of GIF being requested
        Returns:
            {message_id: url} (dict): Dictionary of message ID and a returned GIF URL

    '''
    params = parse.urlencode({
        'tag': tag,
        'api_key': os.getenv('GIPHY_API_KEY'),
        'limit': '1'
    })

    try:
        with request.urlopen(''.join((url, '?', params))) as response:
            data = json.loads(response.read())
    except HTTPError as http_response:
        print(f'Error when requesting {"".join((url, "?", params))}: {http_response}')
        return -1

    print(json.dumps(data, sort_keys=True, indent=4))
    if data['data']:
        return {message_id: data['data']['url']}
    else:
        return {message_id: None}

print(api_request('2dj9vj', 'chowder'))