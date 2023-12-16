# Works at the terminal

import click
import cmd
import rich
import os
import getpass
from rich.panel import Panel
from rich.style import Style
from rich.markdown import Markdown
from .main import ChatGPT
from time import sleep
import logging
import dotenv
from threading import Thread as thr
from . import __repo__, __version__, getExc


dotenv.find_dotenv(".env")
from_env = lambda key : os.environ.get(key)

class busy_bar:
    querying = None
    __spinner = (("-", "\\", "|", "/"), ("█■■■■", "■█■■■", "■■█■■", "■■■█■", "■■■■█"))
    spin_index = 0
    sleep_time = 0.1

    @classmethod
    def __action(
        cls,
    ):
        while cls.querying:
            for spin in cls.__spinner[cls.spin_index]:
                print(" " + spin, end="\r", flush=True)
                if not cls.querying:
                    break
                sleep(cls.sleep_time)

    @classmethod
    def start_spinning(
        cls,
    ):
        try:
            cls.querying = True
            t1 = thr(
                target=cls.__action,
                args=(),
            )
            t1.start()
        except Exception as e:
            cls.querying = False
            logging.debug(getExc(e))

    @classmethod
    def stop_spinning(cls):
        """Stop displaying busy-bar"""
        if cls.querying:
            cls.querying = False
            sleep(cls.sleep_time)


class InteractiveChatGPT(cmd.Cmd):
    prompt = f"┌─[{getpass.getuser().capitalize()}@WebChatGPT](v0.0.1)\r\n└──╼ ❯❯❯"

    def __init__(self, auth, cookie_path, model, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = ChatGPT(auth, cookie_path, model, index)

    def do_help(self, text):
        """Echoes useful help info
        text (str): Text passed
        """
        rich.print(
            Panel(
                f"""
Greetings {getpass.getuser().capitalize()}.

This is a Reverse Engineered ChatGPT Web-version.

╒════╤═════════════╤════════════════════════╕
│    │ Command     │ Action                 │
╞════╪═════════════╪════════════════════════╡
│  0 │ help        │ Show this help info    │
├────┼─────────────┼────────────────────────┤
│  1 │ exit        │ Quits Program          │
├────┼─────────────┼────────────────────────┤
│  2 │ ./<command> │ Run system command     │
├────┼─────────────┼────────────────────────┤
│  3 │ <any other> │ Interacts with ChatGPT │
╘════╧═════════════╧════════════════════════╛


Submit any bug at : https://github.com/Simatwa/WebChatGPT/issues/new

Have some fun!
""",
                title="Help info",
                style=Style(
                    color="cyan",
                    frame="double",
                ),
            )
        )

    def do_exit(self, line):
        print("Okay Goodbye!")
        return True

    def default(self, line):
        if line.startswith("./"):
            os.system(line[2:])
        else:
            try:
                busy_bar.start_spinning()
                generated_response = self.bot.chat(line)
                busy_bar.stop_spinning()
                rich.print(Markdown(generated_response))

            except (KeyboardInterrupt, EOFError):
                busy_bar.stop_spinning()
                print("")
                return False

            except Exception as e:
                logging.error(getExc(e))


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
    default=from_env('openai_authorization'),
    prompt="Enter authorization value for `chat.openai.com`",
)
@click.option(
    "-C",
    "--cookie-path",
    type=click.Path(exists=True),
    help="Path to .json file containing cookies for `chat.openai.com`",
    prompt="Enter path to .json file containing cookies for `chat.openai.com`",
    envvar="openai_cookie_file",
    default=from_env('openai_cookie_file')
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
@click.option(
    "-B",
    "--busy-bar-index",
    help="Busy bar index [0:/, 1:■█■■■]",
    type=click.IntRange(0, 1),
    default=1,
    envvar="busy_bar_index",
)
def interactive(auth, cookie_path, model, index, prompt, busy_bar_index):
    """Chat with ChatGPT interactively"""
    assert isinstance(busy_bar_index, int), "Index must be an integer only"
    busy_bar.spin_index = busy_bar_index
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
    rich.print(
        Panel(
            """
  Repo : https://github.com/Simatwa/WebChatGPT
  By : Smartwa
          """,
            title="WebChatGPT v0.0.1",
            style=Style(
                color="cyan",
                frame=True,
            ),
        ),
    )

    chat()
