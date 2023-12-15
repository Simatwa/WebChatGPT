import requests
import utils
import logging
from common_requests import request_headers, request_payload, request_cookies 

class ChatGPT:

    def __init__(self,locale:str='en-US'):
        self.session = requests.Session()
        self.locale=locale
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
        self.session.headers.update(request_headers)
        self.session.cookies.update(request_cookies)
        self.conversation_endpoint = "https://chat.openai.com/backend-api/conversation"
        self.account_detail_endpoint = "https://chat.openai.com/backend-api/accounts/check"
        self.account_details_endpoint=self.account_detail_endpoint+'/v4-2023-04-27'
        self.prompt_library_endpoint ="https://chat.openai.com/backend-api/prompt_library"
        self.previous_conversations_endpoint = "https://chat.openai.com/backend-api/conversations"
        self.session.headers['User-Agent'] = self.user_agent

    def __generate_payload(self,messsage:str):
        """Generates payload in JSON

        Args:
            messsage (str): Message to be send
        """
    
    def ask(self,message:str,stream:bool=True):
        """Chat with ChatGPT

        Args:
            message (str): message to be send
            stream (bool, optional): Flag to stream response. Defaults to True.
        """
        response = self.session.post(url=self.conversation_endpoint, json=)
    
    def account_details(self,in_details:bool=True) -> dict:
        """Returns various information concerning the user

        Args:
            in_details (bool, optional): Return detailed info. Defaults to False.
        returns:
            dict : {}
        """
        resp = self.session.get(
            self.account_details_endpoint if in_details else self.account_detail_endpoint
        )
        return utils.is_json(resp,'account data')
    
    def prompt_library(self,limit:int=4,offset:int=0) -> list:
        """Generates random prompts

        Args:
            limit (int, optional): Limit suggestions. Defaults to 4.
            offset (int, optional): Offset. Defaults to 0.
        returns:
            list : []
        """
        resp = self.session.get(
            self.prompt_libray_endpoint, 
            params={'limit':limit, "offset" : offset},
        )
        return  utils.is_json(resp,'prompts').get("items")
    
    def previous_conversations(self, limit:int=28, offset:int=0,order:str="updated") -> list:
        """Loads previous conversations

        Args:
            limit (int, optional): Fetch this specific amount of chats. Defaults to 28.
            offset (int, optional): ``. Defaults to 0.
            order (str, optional): Sort order. Defaults to "updated".

        Returns:
            list: Previous conversations contained in dict
        """
        resp = self.session.get(
            self.previous_conversations_endpoint,
            params={
                'limit' : limit,
                'offset' : offset,
                'order' : order
            }
        )
        return utils.is_json(resp,'conversation history')
    
