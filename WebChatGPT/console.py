# Work at the terminal

import click
import cmd
import rich
import os
import getpass
from rich.markdown import Markdown
from .main import ChatGPT

import dotenv

dotenv.find_dotenv(".env")


class InteractiveChatGPT(cmd.Cmd):
    # prompt = f"[{getpass.getuser().capitalize()}@WebChatGPT](v0.0.1)\r\n└──╼ ❯❯❯"
    prompt = f"┌─[{getpass.getuser().capitalize()}@WebChatGPT](v0.0.1)\r\n└──╼ ❯❯❯"

    def __init__(self, auth, cookie_path, model, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = ChatGPT(auth, cookie_path, model, index)

    def do_help(self, text):
        """Echoes useful help info
        text (_type_): Text passed
        """
        rich.print(
            Markdown(
                f"""
Greetings **{getpass.getuser().capitalize()}** : 

This is a Reverse Engineered ChatGPT *Web-version*.

Submit any bug at : https://github.com/Simatwa/ChatGPT-Web/issues/new

| command | Action |
--------------------
| help | Show this help info |
| exit | Quits Program |
| ./<command> | Run system command |
| <any other> | Interacts with ChatGPT |

<p align="center"> Have some fun </center>
"""
            )
        )

    def do_exit(self, line):
        print("Okay Goodbye!")
        return True

    def default(self, line):
        if line.startswith("./"):
            os.system(line[2:])
        else:
            rich.print(Markdown(self.bot.chat(line)))


@click.group("chat")
def chat():
    """Reverse Engineered ChatGPT Web-version"""
    pass


@chat.command()
@click.option(
    "-A",
    "--auth",
    help="OpenAI's authorization value",
    envvar="openai_authorization",
    prompt="Enter authorization value for `chat.openai.com`",
)
@click.option(
    "-C",
    "--cookie-path",
    type=click.Path(exists=True),
    help="Path to .json file containing cookies for `chat.openai.com`",
    prompt="Enter path to .json file containing cookies for `chat.openai.com`",
    envvar="openai_cookie_file",
)
@click.option(
    "-M",
    "--model",
    help="ChatGPT's model to be used",
    envvar="chatgpt_model",
    default="text-davinci-002-render-sha",
)
@click.option(
    "-I", "--index", help="Conversation index to resume from", type=click.INT, default=0
)
@click.option(
    "-P",
    "--prompt",
    help="Start conversation with this messsage",
)
def interactive(auth, cookie_path, model, index, prompt):
    """Chat with ChatGPT interactively"""
    bot = InteractiveChatGPT(auth, cookie_path, model, index)
    if prompt:
        bot.default(prompt)
    bot.cmdloop()


@chat.command()
@click.option(
    "-A",
    "--auth",
    help="OpenAI's authorization value",
    envvar="openai_authorization",
    prompt="Enter authorization value for `chat.openai.com`",
)
@click.option(
    "-C",
    "--cookie-path",
    type=click.Path(exists=True),
    help="Path to .json file containing cookies for `chat.openai.com`",
    prompt="Enter path to .json file containing cookies for `chat.openai.com`",
    envvar="openai_cookie_file",
)
@click.option(
    "-M",
    "--model",
    help="ChatGPT's model to be used",
    envvar="chatgpt_model",
    default="text-davinci-002-render-sha",
)
@click.option(
    "-I", "--index", help="Conversation index to resume from", type=click.INT, default=0
)
@click.option(
    "-P",
    "--prompt",
    help="Start conversation with this messsage",
    prompt="Enter message",
)
def generate(auth, cookie_path, model, index, prompt):
    """Generate a quick response with ChatGPT"""

    content = ChatGPT(auth, cookie_path, model, index).chat(prompt)

    rich.print(Markdown(content))


def main():
    print(
        """
  Repo : https://github.com/Simatwa/WebChatGPT
    By : Smartwa
          """
    )
    chat()
