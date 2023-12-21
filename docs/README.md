<h1 align="center"> WebChatGPT </h1>

<p align="center">
<a href="https://github.com/Simatwa/WebChatGPT/actions/workflows/python-test.yml"><img src="https://github.com/Simatwa/WebChatGPT/actions/workflows/python-test.yml/badge.svg" alt="Python Test"/></a>
<a href="LICENSE"><img alt="License" src="https://img.shields.io/static/v1?logo=GPL&color=Blue&message=GNUv3&label=License"/></a>
<a href="https://pypi.org/project/webchatgpt"><img alt="PyPi" src="https://img.shields.io/static/v1?logo=pypi&label=Pypi&message=v0.1.1&color=green"/></a>
<a href="https://github.com/psf/black"><img alt="Black" src="https://img.shields.io/static/v1?logo=Black&label=Code-style&message=Black"/></a>
<a href="#"><img alt="Passing" src="https://img.shields.io/static/v1?logo=Docs&label=Docs&message=Passing&color=green"/></a>
<a href="#"><img alt="coverage" src="https://img.shields.io/static/v1?logo=Coverage&label=Coverage&message=90%&color=yellowgreen"/></a>
<a href="#" alt="progress"><img alt="Progress" src="https://img.shields.io/static/v1?logo=Progress&label=Progress&message=95%&color=green"/></a>
<a href="https://pepy.tech/project/webchatgpt"><img src="https://static.pepy.tech/personalized-badge/webchatgpt?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads" alt="Downloads"></a>
<!--<a href="https://github.com/Simatwa/WebChatGPT/releases"><img src="https://img.shields.io/github/downloads/Simatwa/WebChatGPT/total?label=Downloads&color=success" alt="Downloads"></img></a> -->
<a href="https://github.com/Simatwa/WebChatGPT/releases"><img src="https://img.shields.io/github/v/release/Simatwa/WebChatGPT?color=success&label=Release&logo=github" alt="Latest release"></img></a>
<a href="https://github.com/Simatwa/WebChatGPT/releases"><img src="https://img.shields.io/github/release-date/Simatwa/WebChatGPT?label=Release date&logo=github" alt="release date"></img></a>
<a href="https://wakatime.com/badge/github/Simatwa/WebChatGPT"><img src="https://wakatime.com/badge/github/Simatwa/WebChatGPT.svg" alt="wakatime"></a>
</p>

<p align="center">
<a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse Engineering</a> of ChatGPT in Python.
</p> 

Unlike the [official Openai library](https://github.com/openai/openai-python), this library makes REST-API calls to [ChatGPT](https://chat.openai.com) via the **browser** endpoints. *No API-KEY required*


```python
from WebChatGPT import ChatGPT
bot = ChatGPT(
    "<path-to-openai-cookies.json>"
)
response = bot.chat('<Your prompt'>)

print(response)
#Ouput : What can I do for you today?
```

<details>

```
$ python -m WebChatGPT interactive                        
╭────────────────────────────── WebChatGPT v0.0.1 ──────────────────────────────╮
│                                                                               │
│   Repo : https://github.com/Simatwa/WebChatGPT                                │
│   By : Smartwa                                                                │
│                                                                               │
╰───────────────────────────────────────────────────────────────────────────────╯
┌─[Smartwa@WebChatGPT](v0.0.1)
└──╼ ❯❯❯Hello there
General Kenobi! You've activated my nostalgia circuits. What can I do for you    
today?  
```

<summary>

In terminal:

</summary>

</details>

## Prerequisites

- [x] Python>=3.10 Installed
- [x] Chrome or Firefox browser
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

In order to do that, we will use the [export-cookie-for-puppeteer](https://github.com/ktty1220/export-cookie-for-puppeteer) extension to extract the cookies which will later on used to retrieve the OAuth.

### Procedure

1. Login to https://chat.openai.com
2. Upon successfull login, use **Export cookie JSON File Puppeteer** to export cookies.

By doing that you are good to go.


- Converse Interactively:

```
$ webchatgpt interactive -C <path-to-openai-cookie-file.json> -P "<your startup prompt though not a must>"
```

- Have a quick response

```
$ webchatgpt generate -C <path-to-openai-cookie-file.json> -P "<your prompt here>"
```

Alternatives to `-C <path-to-openai-cookie-file.json>` :

On the current directory of your **terminal**,create a [`.env`](https://github.com/Simatwa/WebChatGPT/blob/main/env) file and save path to the cookie-file in the format :

```
openai_cookie_file=<path-to-cookie-file>
```

Or simply run `$ webchatgpt <generate/interactive>` and then fill the prompt.

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

If `$ webchatgpt` doesn't look cool on you, there's this workaround `python -m WebChatGPT`

## [Developer Documentation](DEVELOPER.md)

## ToDo

- [ ] Stream Response
- [ ] Implement Your idea
- [ ] Fix my bad code.

## Contributions

Anyone is free to [fork](https://github.com/Simatwa/WebChatGPT/fork), submit [pull request](https://github.com/Simatwa/WebChatGPT/pulls/new) as well as submitting [issues](https://github.com/Simatwa/WebChatGPT/issues/new).

Consider taking a look at the [flow of events info](https://github.com/Simatwa/WebChatGPT/blob/main/docs/operations_flow.md) for the case of a [pull request](https://github.com/Simatwa/WebChatGPT/pulls).

## Acknowledgements

1. [x] [Http-Tracker](https://github.com/venukbh/http-tracker).
2. [x] [export-cookie-for-puppeteer](https://github.com/ktty1220/export-cookie-for-puppeteer)

## Special Thanks

- [x] You

To those wishing to use the Official Openai API endpoints + GoogleBard at console environment; purpose to check out [GPT-CLI](https://github.com/Simatwa/GPT-CLI)

## Disclaimer

This project is a reverse-engineered implementation of the ChatGPT web version and is intended for educational and research purposes only. It is not affiliated with or endorsed by OpenAI. The code in this repository is based on reverse engineering efforts and may not perfectly replicate the functionalities or behavior of the original ChatGPT web version. Usage of this code is at your own risk, and the maintainers of this repository are not responsible for any misuse or unintended use of the generated content. Please refer to OpenAI's policies and terms of service regarding the use of their services and models. By using this repository, you agree to comply with all relevant laws and OpenAI's terms of service.
