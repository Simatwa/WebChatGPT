import requests
from common_requests import request_cookies, request_payload, request_headers
import sort_dict as dicter

write_resp_to = "resp.html"


class ChatWeb:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(request_headers)
        self.session.cookies.update(request_cookies)
        self.payload_url = "https://chat.openai.com/backend-api/conversation"

    @dicter.error_handler(True)
    def send_payload(self, payload):
        resp = self.session.post(url=self.payload_url, stream=True, json=payload)
        dicter.write_data("stream_headers.json", dict(resp.headers))
        if "application" in resp.headers.get("content-type"):
            dicter.write_data("stream_response.json", resp.json())
        else:
            with open(dicter.abs_path(write_resp_to), "w") as fh:
                fh.write(resp.text)


if __name__ == "__main__":
    gpt = ChatWeb()
    gpt.send_payload(request_payload)
