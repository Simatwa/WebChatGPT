### Payloads

- On opening new chat, the following happens:

1. GET [https://chat.openai.com/backend-api/prompt_library/?limit=4&offset=0](https://chat.openai.com/backend-api/prompt_library/?limit=4&offset=0) - *Generates Random prompts*
  
2. POST : [https://chat.openai.com/ces/v1/b](https://chat.openai.com/ces/v1/b) - *Sends telemetrics*
  
  Payload:

```json
    {
    "batch": [
        {
            "timestamp": "2023-12-15T13:33:20.691Z",
            "integrations": {
                "Segment.io": true
            },
            "userId": "user-IUW2uKHQ6bwv4bdiI8IYtjqA",
            "anonymousId": "a0b59320-c342-4c9c-bb24-a99471552968",
            "event": "Show Starter Prompts",
            "type": "track",
            "properties": {
                "prompt_count": 4,
                "prompt_type": "starter",
                "titles": [
                    "Tell me a fun fact",
                    "Explain superconductors",
                    "Make up a story",
                    "Give me ideas"
                ],
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
                "userAgent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
                "locale": "en-US",
                "library": {
                    "name": "analytics.js",
                    "version": "npm:next-1.56.0"
                }
            },
            "messageId": "ajs-next-4088ee126f46655b371bdddb9ac5b78f",
            "_metadata": {
                "bundled": [
                    "Segment.io"
                ],
                "unbundled": [],
                "bundledIds": []
            }
        }
    ],
    "sentAt": "2023-12-15T13:33:26.745Z"
}
```
  
- Upon sending a text the following happens:

3. GET : [https://chat.openai.com/backend-api/accounts/check/v4-2023-04-27](https://chat.openai.com/backend-api/accounts/check/v4-2023-04-27) - *Fetches user data*

4. POST : [https://chat.openai.com/backend-api/conversation](https://chat.openai.com/backend-api/conversation) - *Generate Conversation*

 payload :
   ```json
   {
    "action": "next",
    "messages": [
        {
            "id": "aaa27fdc-adfc-4e97-8383-7be26db9a472",
            "author": {
                "role": "user"
            },
            "content": {
                "content_type": "text",
                "parts": [
                    "Tell me a random fun fact about the Roman Empire"
                ]
            }
        }
    ],
    "parent_message_id": "aaa1625d-8249-4412-9825-004c3144c609",
    "model": "text-davinci-002-render-sha",
    "timezone_offset_min": -180,
    "suggestions": [
        "Tell me a random fun fact about the Roman Empire",
        "Explain superconductors like I'm five years old.",
        "Make up a 5-sentence story about \"Sharky\", a tooth-brushing shark superhero. Make each sentence a bullet point.",
        "Give me 3 ideas about how to plan good New Years resolutions. Give me some that are personal, family, and professionally-oriented."
    ],
    "history_and_training_disabled": false,
    "arkose_token": null,
    "conversation_mode": {
        "kind": "primary_assistant"
    },
    "force_paragen": false,
    "force_rate_limit": false
}
   ```
   
5. GET : [https://chat.openai.com/backend-api/conversations?offset=0&limit=28&order=updated](https://chat.openai.com/backend-api/conversations?offset=0&limit=28&order=updated) - *Fetches conversation history* 

Response 

```json
{
    "items": [
        {
            "id": "b3779121-8767-4202-9527-3058f40e94e9",
            "title": "Helpful User, Assistant",
            "create_time": "2023-12-15T12:03:30.596706+00:00",
            "update_time": "2023-12-15T12:03:32.675791+00:00",
            "mapping": null,
            "current_node": null,
            "conversation_template_id": null,
            "gizmo_id": null,
            "is_archived": false,
            "workspace_id": null
        },
        {
            "id": "3bec216c-e007-4cb2-8edc-6397e8910238",
            "title": "Generate ISO 8601 Timestamp",
            "create_time": "2023-12-15T11:21:29.241216+00:00",
            "update_time": "2023-12-15T11:29:04.660939+00:00",
            "mapping": null,
            "current_node": null,
            "conversation_template_id": null,
            "gizmo_id": null,
            "is_archived": false,
            "workspace_id": null
        },
        {
            "id": "e656ee83-acdd-4a0a-aa6e-1c298c5f3404",
            "title": "Hello Summary: Keep Short",
            "create_time": "2023-12-15T10:08:41.904885+00:00",
            "update_time": "2023-12-15T10:08:44.315228+00:00",
            "mapping": null,
            "current_node": null,
            "conversation_template_id": null,
            "gizmo_id": null,
            "is_archived": false,
            "workspace_id": null
        },
    ],
    "total": 107,
    "limit": 3,
    "offset": 0,
    "has_missing_conversations": false
}
```
6. POST : [https://chat.openai.com/backend-api/lat/r](https://chat.openai.com/backend-api/lat/r)
  Payload :
  ```json
  {
    "server_request_id": "835f17ad7df465eb-MBA",
    "model": "text-davinci-002-render-sha",
    "preflight_time_ms": 1,
    "count_tokens": 74,
    "ts_first_token_ms": 2082,
    "ts_max_token_time_ms": 626,
    "ts_mean_token_without_first_ms": 20.589041095890412,
    "ts_median_token_without_first_ms": 0,
    "ts_min_token_time_ms": 1,
    "ts_p95_token_without_first_ms": 131.5999999999987,
    "ts_p99_token_without_first_ms": 379.7600000000004,
    "ts_std_dev_token_ms": 87.66355916759152,
    "ts_total_request_ms": 3585
}
  ```

7. POST : [	https://chat.openai.com/backend-api/conversation/gen_title/86f73b54-0f51-47ba-84a3-07c1e25dce81](https://chat.openai.com/backend-api/conversation/gen_title/86f73b54-0f51-47ba-84a3-07c1e25dce81) - *Generate title*