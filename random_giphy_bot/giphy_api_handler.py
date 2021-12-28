import asyncio
import aiohttp
from aioconsole import ainput, aprint
from urllib import parse

class GiphyHandler:
    """
    A class to handle GIPHY API requests asynchonously. Must be started before any methods are used.

    Attributes:
        url (str): URL to look up for requests
        api_key (str): API key to use for requests
        is_closed (bool): Boolean that represents when GiphyHandler is closed.
        is_started (bool): Boolean that represents when GiphyHandler is started.
    Methods:
        reload(api_key):
            Close GiphyHandler temporarily, stop any current requests, input a new API key, and start it again.
        close():
            Stop any current requests, and set GiphyHandler as closed.
        random_request(tag, request_tries=5):
            Request a GIPHY URL with a certain tag. If a try fails, then it starts again.
        request_handler(tag):
            Handle a GIPHY URL request, and process the results.
        start(api_key):
            Start GiphyHandler, and input a new API key.
    
    """

    url = "http://api.giphy.com/v1/gifs/random"
    api_key = None
    is_closed = False
    is_started = False

    async def reload(self, api_key):
        assert self.is_started is True, "Giphy handler must be started first"
        assert type(api_key) is str, "Giphy API key must be a string"
        assert len(api_key) > 0, "Giphy API key must be longer than 0"

        await aprint("Reloading GIPHY handler...")

        self.is_closed = True
        self.is_started = False

        await asyncio.sleep(2)
        self.api_key = api_key

        self.is_closed = False
        self.is_started = True

    async def close(self):
        assert self.is_started is True, "Giphy handler must be started first"

        await aprint("Closing GIPHY handler...")

        self.is_closed = True
        self.is_started = False

    async def random_request(self, tag, request_tries=5):
        assert request_tries > 0, "Number of attempts must be more than 0"
        assert self.is_started is True, "Giphy handler must be started first"

        response = None
        for attempt in range(request_tries):
            if not self.is_closed:
                response = await self.request_handler(tag=tag)
            if response != -1:
                return response
            if self.is_closed:
                return -1
        
        return response

    async def request_handler(self, tag):
        params = parse.urlencode({
            'tag': tag,
            'api_key': self.api_key,
            'limit': '1'
        })

        async with aiohttp.ClientSession() as session:
            if not self.is_closed:
                async with session.get(''.join((self.url, '?', params))) as response:
                    if not self.is_closed:
                        data = await response.json()

        if 'data' in data and data['data']: # If data is passed and there is content
            return data['data']['url']
        elif 'data' in data: # If data is passed but there is no content
            return None
        else: # If no data is passed
            return -1

    def __init__(self):
        pass

    def start(self, api_key):
        assert type(api_key) is str, "Giphy API key must be a string"
        assert len(api_key) > 0, "Giphy API key must be longer than 0"

        if not self.is_started:
            print("Starting GIPHY handler...")

            self.api_key = api_key
            self.is_started = True
            self.is_closed = False
        else:
            print("GIPHY handler is already started!")
