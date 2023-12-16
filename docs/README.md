<h1 align="center"> WebChatGPT </h1>

<p align="center">

[Reverse engineered](https://en.wikipedia.org/wiki/Reverse_engineering) ChatGPT in Python.

</p> 

## Prerequisites

- [x] Python>=3.10 Installed
- [x] Chrome or Firefox browser
- [x] [Http-Tracker](https://github.com/venukbh/http-tracker) extension installed.
- [x] [export-cookie-for-puppeteer](https://github.com/ktty1220/export-cookie-for-puppeteer) extension installed.

## Installation & usage

### Installation

Either of the following ways will get you ready :

1. From pypi:
  
  ```
  pip install --upgrade webchatgpt
  ```

2. From source

```
git clone https://github.com/Simatwa/WebChatGPT.git
cd WebChatGPT
pip install .
```

## Usage

The script utilizes [HTTP Cookies](https://en.wikipedia.org/wiki/HTTP_cookie) and [OAuth](https://en.wikipedia.org/wiki/OAuth) to justify the REST-API requests at [Openai](https://openai.com). 

In order to do that, we will use the [Http-Tracker](https://github.com/venukbh/http-tracker) extension to harvest the `Oauth` and 
[export-cookie-for-puppeteer](https://github.com/ktty1220/export-cookie-for-puppeteer) extension to extract the cookies.

### Procedure

1. Login to https://chat.openai.com
2. Upon successfull login, use **Export cookie JSON File Puppeteer** to download cookies.
3. Launch the **Http-Tracker** extension.
4. Back to ChatGPT, make a new conversation and then have a chat with it.
5. Back to Http-Tracker window, locate and click on the url row having `https://chat.openai.com/backend-api/conversation` to toggle a dropdown showing the http requests details. 
6. On  the *Request Details Table*, locate a Header having key `Authorization` and then copy it's corresponding value without the `Bearer` string and then paste it somewhere.
7. On your current directory create a [`.env`](https://github.com/Simatwa/WebChatGPT/blob/main/env) file and then save the contents in the format :

```
openai_authorization=<authorization_value>
openai_cookie_file=<path-to-cookie-file>
```

By doing that you are good to go.


- Converse Interactively:

```
webchatgpt interactive -P "<your startup prompt though not a must>"
```

- Have a quick response

```
webchatgpt generate -P "<your prompt here>"
```

<details>

<summary>

For more info; append `--help` to the command

</summary>

<details>

<summary>

`$ webchatgpt --help`

</summary>


```
Usage: webchatgpt [OPTIONS] COMMAND [ARGS]...

  Reverse Engineered ChatGPT Web-version

Options:
  --help  Show this message and exit.

Commands:
  generate     Generate a quick response with ChatGPT
  interactive  Chat with ChatGPT interactively
```

</details>


<details>

<summary>

` $ webchatgpt generate --help`

</summary>


```
Usage: webchatgpt generate [OPTIONS]

  Generate a quick response with ChatGPT

Options:
  -A, --auth TEXT         OpenAI's authorization value
  -C, --cookie-path PATH  Path to .json file containing cookies for
                          `chat.openai.com`
  -M, --model TEXT        ChatGPT's model to be used
  -I, --index INTEGER     Conversation index to resume from
  -P, --prompt TEXT       Start conversation with this messsage
  --help                  Show this message and exit.
```

</details>


<details>

<summary>

` $ webchatgpt interactive --help`

</summary>

```
Usage: webchatgpt interactive [OPTIONS]

  Chat with ChatGPT interactively

Options:
  -A, --auth TEXT                 OpenAI's authorization value
  -C, --cookie-path PATH          Path to .json file containing cookies for
                                  `chat.openai.com`
  -M, --model TEXT                ChatGPT's model to be used
  -I, --index INTEGER             Conversation index to resume from
  -P, --prompt TEXT               Start conversation with this messsage
  -B, --busy-bar-index INTEGER RANGE
                                  Busy bar index [0:/, 1:■█■■■]  [0<=x<=1]
  --help                          Show this message and exit.
```

Running `help` while in interactive prompt:

| command | Action |
| ------- | --------- |
| help | Show this help info |
| exit | Quits Program |
| .`/<command>` | Run system command |
| `<any other>` | Interacts with ChatGPT |



</details>


</details>

## ToDo

- [] Stream Response
- [] Implement Your idea
- [] Fix my bad code.

## Contributions

Anyone is free to [fork](https://github.com/Simatwa/WebChatGPT/fork), submit [pull request](https://github.com/Simatwa/WebChatGPT/pulls/new) as well as submitting [issues](https://github.com/Simatwa/WebChatGPT/issues/new).

Consider taking a look at the [flow of events info](https://github.com/Simatwa/WebChatGPT/blob/main/docs/operations_flow.md) for the case of a [pull request](https://github.com/Simatwa/WebChatGPT/pulls).

## Acknowledgements

1. [x] [Http-Tracker](https://github.com/venukbh/http-tracker).
2. [x] [export-cookie-for-puppeteer](https://github.com/ktty1220/export-cookie-for-puppeteer)

## Special Thanks

- [x] You

## Disclaimer

This project is a reverse-engineered implementation of the ChatGPT web version and is intended for educational and research purposes only. It is not affiliated with or endorsed by OpenAI. The code in this repository is based on reverse engineering efforts and may not perfectly replicate the functionalities or behavior of the original ChatGPT web version. Usage of this code is at your own risk, and the maintainers of this repository are not responsible for any misuse or unintended use of the generated content. Please refer to OpenAI's policies and terms of service regarding the use of their services and models. By using this repository, you agree to comply with all relevant laws and OpenAI's terms of service.
