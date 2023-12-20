from datetime import datetime, timezone
import json
import logging
import os
from uuid import uuid4

headers = request_headers = {
    "Accept": "text/event-stream",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US",
    "Alt-Used": "chat.openai.com",
    "Authorization": f"Bearer %(value)s",
    "Connection": "keep-alive",
    # "Content-Length": "904",
    "Content-Type": "application/json",
    "Host": "chat.openai.com",
    "Origin": "https://chat.openai.com",
    "Referer": "https://chat.openai.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
}


def error_handler(exit_on_error: bool = False, default=None):
    """Decorator for handling exceptions

    Args:
        exit_on_error (bool, optional): ``. Defaults to False.
        default (_type_, optional): Return this incase of an exception. Defaults to None.
    """

    def decorator(func):
        def main(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(e.args[1] if len(e.args) > 1 else str(e))
                if exit_on_error:
                    exit(1)
                return default

        return main

    return decorator  #


def get_request_headers_and_append_auth(self) -> dict:
    """Generate Http request headers & append OAuth

    Args:
        auth (str): OpenAI's authorization header

    Returns:
        dict: Request headers
    """
    resp = self.session.get(
        "https://chat.openai.com/api/auth/session",
        headers=request_headers,
    )
    if not resp.ok:
        raise Exception("Failed to fetch Auth value, supply path to correct cookies.")
    self.auth = resp.json()
    auth_template = headers["Authorization"]
    headers["Authorization"] = auth_template % {"value": self.auth["accessToken"]}
    return headers


@error_handler(exit_on_error=True)
def get_cookies(path: str) -> dict:
    """Reads cookies and format thems

    Args:
        path (str): Path to cookie file

    Returns:
        dict: Cookies sorted {name :  value}
    """
    resp = {}
    with open(path) as fh:
        for entry in json.load(fh):
            resp[entry["name"]] = entry["value"]
        return resp


def is_json(response: object, info: str = ""):
    """Checks whether the response is application/json formatted

    Args:
        response (object): `requests.get/post response`
        info (str): Data being fetched
    rtype : dict
    """
    content_type = response.headers.get("content-type")
    if not "application/json" in content_type:
        raise Exception(
            f"Failed to fetch {info} - `{content_type}` : \n {response.text}"
        )
    return response.json()


def current_timestamp():
    """Generates current timestamp in UTC
    rtype : str
    """
    current_time = datetime.now(timezone.utc)
    # Format the current time in the desired format with microseconds limited to 3 digits
    return current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def generate_telemetry_payload(self: object):
    """Generates Telemeries - though not implemented in this sript but it's good to be aware of.

    Args:
        self (object): ChatGPT class
    rtype : dict
    """
    headers = self.session.headers
    payload_template = {
        "batch": [
            {
                "timestamp": f"{current_timestamp()}",
                "integrations": {"Segment.io": True},
                "userId": f"{headers.get('ajs_user_id')}",
                "anonymousId": f"{headers.get('ajs_anonymous_id')}",
                "event": "Show Starter Prompts",
                "type": "track",
                "properties": {
                    "prompt_count": 4,
                    "prompt_type": "starter",
                    "titles": [entry["title"] for entry in self.prompt_library()],
                    "origin": "chat",
                    "openai_app": "API",
                },
                "context": {
                    "page": {
                        "path": "/",
                        "referrer": "",
                        "search": "",
                        "title": "ChatGPT",
                        "url": "https://chat.openai.com/",
                    },
                    "userAgent": self.session.headers["User-Agent"],
                    "locale": self.locale,
                    "library": {"name": "analytics.js", "version": "npm:next-1.56.0"},
                },
                # "messageId": "ajs-next-3154852a6626ae6a48a031e2506fexxx",
                "_metadata": {
                    "bundled": ["Segment.io"],
                    "unbundled": [],
                    "bundledIds": [],
                },
            }
        ],
        "sentAt": f"{current_timestamp()}",
    }


def generate_payload(self: object, prompt: str) -> dict:
    """Creates conversation payload

    Args:
        self (object): _

    Returns:
        dict: _description_
    """

    payload_template = {
        "action": "next",
        "messages": [
            {
                # "id": "aaa2921d-d8c9-4516-80bd-ed1eaxxxxx",
                "author": {"role": "user"},
                "content": {"content_type": "text", "parts": [prompt]},
                "metadata": {},
            }
        ],
        # "conversation_id": self.conversation_metadata["id"],
        # "parent_message_id": "5b45a98c-0871-48ed-895b-f36f188cxxxx",
        "model": self.model,
        "timezone_offset_min": -180,
        "suggestions": [],
        "history_and_training_disabled": self.disable_history_and_training,
        "arkose_token": None,
        "conversation_mode": {"kind": "primary_assistant"},
        "force_paragen": False,
        "force_rate_limit": False,
    }
    if self.current_conversation_id:
        # Continuing conversation
        payload_template["conversation_id"] = self.current_conversation_id
    else:
        # Create new conversation
        payload_template["messages"][0]["id"] = str(uuid4())
        payload_template["suggestions"] = [
            prompt["prompt"] for prompt in self.prompt_library()["items"]
        ]

    # print(json.dumps( payload_template,indent=4,))
    return payload_template


def get_message(response: dict) -> str:
    """Extracts generated message from the response

    Args:
        response (dict): `bot.ask` response

    Returns:
        str: Extracted message
    """
    assert isinstance(response, dict), "'response' should be of 'dict' data-type"
    return response["message"]["content"]["parts"][0]
