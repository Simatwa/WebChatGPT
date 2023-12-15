import requests

session = requests.Session()

endpoint = "https://chat.openai.com/backend-api/conversation"

from common_requests import request_cookies, request_headers, request_payload

session.headers.update(request_headers)
session.cookies.update(request_cookies)

resp = session.post(endpoint, json=request_payload)

from sort_dict import write_data

write_data('convo_test.json',dict(resp.json()))

write_data('convo_test_headers.json',dict(resp.headers))