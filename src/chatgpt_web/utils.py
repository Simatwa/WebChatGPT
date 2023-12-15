from datetime import datetime, timezone

def is_json(response:object, info:str=''):
    """Checks whether the response is application/json formatted

    Args:
        response (object): `requests.get/post response`
        info (str): Data being fetched
    rtype : dict
    """
    content_type = response.headers.get('content-type')
    if not 'application/json' in content_type:
        raise Exception(f'Failed to fetch {info} - `{content_type}` : \n {response.text}')
    return response.json()

def current_timestamp():
    """Generates current timestamp in UTC
    rtype : str
    """
    current_time = datetime.now(timezone.utc)
    # Format the current time in the desired format with microseconds limited to 3 digits
    return current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

def generate_init_payload(self:object):
    """Creates payload for creating new conversation

    Args:
        self (object): ChatGPT class
    rtype : dict
    """
    headers = self.session.headers
    payload_template =  {
        "batch": [
        {
            "timestamp": f"{current_timestamp()}",
            "integrations": {
                "Segment.io": True
            },
            "userId": f"{headers.get('ajs_user_id')}",
            "anonymousId": f"{headers.get('ajs_anonymous_id')}",
            "event": "Show Starter Prompts",
            "type": "track",
            "properties": {
                "prompt_count": 4,
                "prompt_type": "starter",
                "titles": [ entry['title'] for entry in self.prompt_library()],
                "origin": "chat",
                "openai_app": "API"
            },
            "context": {
                "page": {
                    "path": "/",
                    "referrer": "",
                    "search": "",
                    "title": "ChatGPT",
                    "url": "https://chat.openai.com/"
                },
                "userAgent": f"{self.user_agent}",
                "locale": f"{self.locale}",
                "library": {
                    "name": "analytics.js",
                    "version": "npm:next-1.56.0"
                }
            },
            #"messageId": "ajs-next-3154852a6626ae6a48a031e2506fe59d",
                               #1a50c897d53bfb315eb7270979e9726e
            "_metadata": {
                "bundled": [
                    "Segment.io"
                ],
                "unbundled": [],
                "bundledIds": []
            }
        }
    ],
    "sentAt": f"{current_timestamp()}"
}
    
def generate_payload(self:object,prompt:str) -> dict:
    """Creates payload

    Args:
        self (object): _

    Returns:
        dict: _description_
    """

    payload_template = {
    "action": "next",
    "messages": [
        {
            #"id": "aaa2921d-d8c9-4516-80bd-ed1eaxxxxx",
            "author": {
                "role": "user"
            },
            "content": {
                "content_type": "text",
                "parts": [
                    prompt
                ]
            },
            "metadata": {}
        }
    ],
    "conversation_id": self.conversation_metadata['id'],
    #"parent_message_id": "5b45a98c-0871-48ed-895b-f36f188cxxxx",
    "model": self.model,
    "timezone_offset_min": -180,
    "suggestions": []+self.suggestions,
    "history_and_training_disabled": False,
    "arkose_token": None,
    "conversation_mode": {
        "kind": "primary_assistant"
    },
    "force_paragen": False,
    "force_rate_limit": False
    }
    return payload_template