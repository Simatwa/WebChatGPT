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
from . import __repo__, __version__, __author__, __info__
from .utils import error_handler

getExc = lambda e: e.args[1] if len(e.args) > 1 else str(e)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s : %(message)s ",  # [%(module)s,%(lineno)s]", # for debug purposes
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


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
            t1.join()

    @classmethod
    def stop_spinning(cls):
        """Stop displaying busy-bar"""
        if cls.querying:
            cls.querying = False
            sleep(cls.sleep_time)

    @classmethod
    def run(cls):
        """"""

        def decorator(func):
            def main(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except KeyboardInterrupt:
                    cls.stop_spinning()
                    return
                except EOFError:
                    cls.querying = False
                    exit(logging.info("Stopping program"))
                except Exception as e:
                    cls.stop_spinning()
                    logging.error(getExc(e))

            return main

        return decorator


class InteractiveChatGPT(cmd.Cmd):
    prompt = (
        f"┌─[{getpass.getuser().capitalize()}@WebChatGPT]({__version__})\r\n└──╼ ❯❯❯"
    )

    def __init__(self, cookie_path, model, index, timeout, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = ChatGPT(
            cookie_path, model=model, conversation_index=index, timeout=timeout
        )

    def do_help(self, text):
        """Echoes useful help info
        text (str): Text passed
        """
        rich.print(
            Panel(
                f"""
Greetings {getpass.getuser().capitalize()}.

This is a {__info__}

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


Submit any bug at : {__repo__}/issues/new

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
                if self.prettify:
                    rich.print(Markdown(generated_response))
                else:
                    click.secho(generated_response)

            except (KeyboardInterrupt, EOFError):
                busy_bar.stop_spinning()
                print("")
                return False  # Exit cmd

            except Exception as e:
                busy_bar.stop_spinning()
                logging.error(getExc(e))


@click.group("chat")
def chat():
    """Reverse Engineered ChatGPT Web-Version"""
    pass


@chat.command()
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
    "-I", "--index", help="Conversation index to resume from", type=click.INT, default=1
)
@click.option(
    "-T",
    "--timeout",
    help="Http request timeout",
    type=click.INT,
    default=30,
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
@click.option("--prettify/--raw", default=True, help="Prettify the markdowned response")
def interactive(cookie_path, model, index, timeout, prompt, busy_bar_index, prettify):
    """Chat with ChatGPT interactively"""
    assert isinstance(busy_bar_index, int), "Index must be an integer only"
    busy_bar.spin_index = busy_bar_index
    bot = InteractiveChatGPT(cookie_path, model, index, timeout)
    bot.prettify = prettify
    if prompt:
        bot.default(prompt)
    bot.cmdloop()


@chat.command()
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
    "-I", "--index", help="Conversation index to resume from", type=click.INT, default=1
)
@click.option(
    "-T",
    "--timeout",
    help="Http request timeout",
    type=click.INT,
    default=30,
)
@click.option(
    "-P",
    "--prompt",
    help="Start conversation with this messsage",
    prompt="Enter message",
)
@click.option("--prettify/--raw", default=True, help="Prettify the markdowned response")
def generate(cookie_path, model, index, timeout, prompt, prettify):
    """Generate a quick response with ChatGPT"""

    content = ChatGPT(cookie_path, model, index, timeout=timeout).chat(prompt)

    if prettify:
        rich.print(Markdown(content))
    else:
        click.secho(content)


@error_handler(exit_on_error=True)
def main():
    dotenv.load_dotenv(os.path.join(os.getcwd(), ".env"))
    rich.print(
        Panel(
            f"""
  Repo : {__repo__}
  By : {__author__}
          """,
            title=f"WebChatGPT v{__version__}",
            style=Style(
                color="cyan",
                frame=True,
            ),
        ),
    )

    chat()
