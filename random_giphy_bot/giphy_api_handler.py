import json
import os
import asyncio
import aiohttp
from aioconsole import ainput, aprint
from urllib import parse, request
from urllib.error import HTTPError
from dotenv import load_dotenv

load_dotenv()

url = "http://api.giphy.com/v1/gifs/random"

def api_request(tag):
    """
    Request a GIF link from GIPHY for a certain one-word tag.

        Parameters:
            tag (str): Tag of GIF being requested
        Returns:
            url (str, int, or None): URL of requested GIF. May be -1 or None if nothing is sent.
    
    """
    assert type(tag) is str, "Tag must be a string"
    assert len(tag.split()) == 1, "Tag must be exactly one word"

    params = parse.urlencode({
        'tag': tag,
        'api_key': os.getenv('GIPHY_API_KEY'),
        'limit': '1'
    })

    try:
        with request.urlopen(''.join((url, '?', params))) as response:
            data = json.loads(response.read())
    except HTTPError as http_response:
        aprint(f'Error when requesting {"".join((url, "?", params))}: {http_response}')
        return -1
    
    if data['data']:
        return data['data']['url']
    else:
        return None

async def batch_request(tag, request_tries=5):
    """
    Request a GIF from GIPHY, but try a certain amount of times if there is any failure.

    Parameters:
        tag (str): Tag of GIF being requested
        request_tries (int): Amount of times to try requesting GIF again after failure. 5 on default.
    Returns:
        response (str): URL of GIF being requested. May be -1 or None if nothing is sent. 

    """
    assert type(tag) is str, "Tag must be a string"
    assert len(tag.split()) == 1, "Tag must be exactly one word"
    assert type(request_tries) is int, "Number of tries must be an int"
    assert request_tries > 1, "Number of tries must be more than one"

    for request_try in range(request_tries):
        response = api_request(tag)
        if response != -1:
            return response
        await asyncio.sleep(1)
    return response
