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
import datetime
import json
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
        self.cookie_path = cookie_path
        self.model = model
        self.conversation_index = index
        self.timeout = timeout
        self.bot = ChatGPT(
            cookie_path, model=model, conversation_index=index, timeout=timeout
        )

    def output_bond(
        self,
        title: str,
        text: str,
        color: str = "cyan",
        frame: bool = True,
        is_json: bool = False,
    ):
        """Print prettified output

        Args:
            title (str): Title
            text (str): Info to be printed
            color (str, optional): Output color. Defaults to "cyan".
            frame (bool, optional): Add frame. Defaults to True.
        """
        if is_json:
            text = f"""
```json
{json.dumps(text,indent=4)}
```
"""
        rich.print(
            Panel(
                Markdown(text),
                title=title.title(),
                style=Style(
                    color=color,
                    frame=frame,
                ),
            ),
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

╒════╤════════════════════════╤═════════════════════════════════════╕
│    │ Command                │ Action                              │
╞════╪════════════════════════╪═════════════════════════════════════╡
│  0 │ help                   │ Show this help info                 │
├────┼────────────────────────┼─────────────────────────────────────┤
│  1 │ history                │ Show conversation history           │
├────┼────────────────────────┼─────────────────────────────────────┤
│  2 │ share                  │ Share conversation by link          │
├────┼────────────────────────┼─────────────────────────────────────┤
│  3 │ stop_share             │ Revoke shared conversation link     │
├────┼────────────────────────┼─────────────────────────────────────┤
│  4 │ rename                 │ Renames conversation title          │
├────┼────────────────────────┼─────────────────────────────────────┤
│  5 │ archive                │ Archive or unarchive a conversation │
├────┼────────────────────────┼─────────────────────────────────────┤
│  6 │ shared_conversations   │ Show shared conversations           │
├────┼────────────────────────┼─────────────────────────────────────┤
│  7 │ previous_conversations │ Show previous conversations         │
├────┼────────────────────────┼─────────────────────────────────────┤
│  8 │ delete_conversations   │ Delete a particular conversation    │
├────┼────────────────────────┼─────────────────────────────────────┤
│  9 │ prompts                │ Generate random prompts             │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 10 │ account_info           │ ChatGPT account info/setings        │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 11 │ ask                    │ Show raw response from ChatGPT      │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 12 │ auth                   │ Show current user auth info         │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 13 │ migrate                │ Shift to another conversation       │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 14 │ ./<command>            │ Run system command                  │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 15 │ <any other>            │ Interacts with ChatGPT              │
├────┼────────────────────────┼─────────────────────────────────────┤
│ 16 │ exit                   │ Quits Program                       │
╘════╧════════════════════════╧═════════════════════════════════════╛
Submit any bug at : {__repo__}/issues/new

Have some fun!
""",
                title="Help Info",
                style=Style(
                    color="cyan",
                    frame="double",
                ),
            )
        )

    def do_history(self, line):
        """Show conversation history"""
        history = self.bot.chat_history(
            conversation_id=click.prompt(
                "Conversation ID", default=self.bot.current_conversation_id
            )
        )
        formatted_chats = []
        format_datetime = (
            lambda timestamp: datetime.datetime.fromtimestamp(timestamp)
            .today()
            .strftime("%H:%M:%S %d-%b-%Y")
        )

        for entry in history.get("content"):
            formatted_chats.append(
                f"""
### {entry['author']} (**{format_datetime(entry['create_time'])}**)

{entry['text']}
"""
            )
        self.output_bond(
            history.get("title"),
            "\n\n".join(formatted_chats),
        )
        if click.confirm("Do you wish to save this"):
            path = click.prompt(
                "Enter path to save to", default=history.get("title") + ".json"
            )
            with open(path, "w") as fh:
                json.dump(
                    history,
                    fh,
                    indent=click.prompt(
                        "Json Indentantion level",
                        default=4,
                        type=int,
                    ),
                )
            click.secho(f"Saved successfully to `{path}`")

    def do_share(self, line):
        """Share a conversation by link"""
        share_info = self.bot.share_conversation(
            conversation_id=click.prompt(
                "Conversation ID", default=self.bot.current_conversation_id
            ),
            is_anonymous=click.confirm("Is anonymous", default=True),
            is_public=click.confirm("Is public", default=True),
            is_visible=True,
        )
        self.output_bond(
            share_info.get("title"), f"Url : **{share_info.get('share_url')}**"
        )

    def do_stop_share(self, line):
        """Revoke shared conversation link"""
        success_report = self.bot.stop_sharing_conversation(
            self.bot.share_conversation(
                conversation_id=click.prompt(
                    "Conversation ID", default=self.bot.current_conversation_id
                ),
            ).get("share_id")
        )
        self.output_bond("Success Report", success_report, is_json=True)

    def do_rename(self, line):
        """Renames conversation title"""
        new_title = click.prompt("New title", default=line)
        if click.confirm("Are you sure to change conversation title"):
            response = self.bot.rename_conversation(
                conversation_id=click.prompt(
                    "Conversation ID", default=self.bot.current_conversation_id
                ),
                title=new_title,
            )
            self.output_bond("Change Convo Title", response, is_json=True)
        else:
            click.secho("Conversation title retained", fg="yellow")

    def do_archive(self, line):
        """Archives or unarchive a conversation"""
        conversation_id = (
            click.prompt("Conversation ID", default=self.bot.current_conversation_id),
        )
        is_archive = click.confirm(
            "Is archive",
            default=True,
        )
        if click.confirm("Are you sure to perform this operation"):
            response = self.bot.archive_conversation(
                conversation_id,
                is_archived=is_archive,
            )
            self.output_bond("Archive Report", response, is_json=True)

    def do_shared_conversations(self, line):
        """Shows shared conversations"""
        shared = self.bot.shared_conversations()
        self.output_bond("Shared Conversations", shared, is_json=True)

    def do_previous_conversations(self, line):
        """Shows previous conversations"""
        previous_convos = self.bot.previous_conversations(
            limit=click.prompt("Convesation limit", type=int, default=28),
            offset=click.prompt("Conversation offset", type=int, default=0),
            all=True,
        )
        self.output_bond("Previous Conversations", previous_convos, is_json=True)

    def do_delete_conversations(self, line):
        """Deletes a particular conversation"""
        conversation_id = (
            click.prompt("Conversation ID", default=self.bot.current_conversation_id),
        )
        if click.confirm("Are you sure to delete this conversation"):
            response = self.bot.delete_conversation(
                conversation_id,
            )
            self.output_bond("Deletion Report", response, is_json=True)

    def do_prompts(self, line):
        """Generate random prompts"""
        prompts = self.bot.prompt_library(
            limit=click.prompt("Total prompts", type=int, default=4),
        )
        self.output_bond("Random Prompts", prompts, is_json=True)

    def do_account_info(self, line):
        """Shows information related to current account at ChatGPT"""
        details = self.bot.user_details(
            in_details=click.confirm("Show in details", default=True),
        )
        self.output_bond("Account Info", details, is_json=True)

    def do_ask(self, line):
        """Show raw response from ChatGPT"""
        response = self.bot.ask(
            prompt=line if bool(line.strip()) else click.prompt("Prompt")
        )
        self.output_bond("Raw Response", response, is_json=True)

    def do_auth(self, line):
        """Show current user auth info"""
        if click.confirm(
            "Contents to be displayed contains sensitive data. Are you sure to continue",
        ):
            self.output_bond("Current Auth info", self.bot.auth, is_json=True)

    def do_migrate(self, line):
        """Shift to another conversation"""
        if click.confirm(
            "Are you sure to shift to new conversation",
        ):
            sort_var = lambda val: val[0] if isinstance(val, tuple) else val
            self.model = (click.prompt("ChatGPT model", default=sort_var(self.model)),)
            self.conversation_index = (
                click.prompt(
                    "Conversation Index",
                    default=sort_var(self.conversation_index),
                ),
            )
            self.timeout = (
                click.prompt(
                    "Request timeout", type=int, default=sort_var(self.timeout)
                ),
            )
            self.bot = ChatGPT(
                self.cookie_path,
                model=sort_var(self.model),
                conversation_index=sort_var(self.conversation_index),
                timeout=sort_var(self.timeout),
            )

    def do_exit(self, line):
        if click.confirm("Are you sure to exit"):
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
