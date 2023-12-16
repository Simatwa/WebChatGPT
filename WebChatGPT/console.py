# Work at the terminal

import click
import cmd
import rich
import getpass

from .main import ChatGPT


class InteractiveChatGPT(cmd.Cmd):
    prompt= "[ChatGPT-Web](v0.0.1)\r\n└──╼ ❯❯❯"

    def __init__(self, *args, **kwargs):
        self.bot = ChatGPT(*args, **kwargs)


    def do_help(self,text):
        """Echoes useful help info
            text (_type_): Text passed
        """
        rich.print(
            rich.markdown.Markdown(f"""
Greetings **{getpass.getuser()}** : 
This is a Reverse Engineered ChatGPT *Web-version*.
Submit any bug at : https://github.com/Simatwa/ChatGPT-Web/issues/new

| command | Action |
--------------------
| help | Show this help info |
| exit | Quits Program|
| <any other> | Interacts with ChatGPT |

<p align="center"> Have some fun </center>
"""
            )
        )

    def do_exit(self,line):
        print('Okay Goodbye!')
        exit(0)

    def do_default(self, line):
        rich.print(
            rich.markdown.Markdown(
                self.bot.chat(
                    line
                )
            )
        )

@click.group('chat')
def chat():
    pass

@chat.command()
@click.option(
    '-A','--auth',
    help="OpenAI's authorization value",
    envar='openai_authorization',
    prompt="Enter authorization value for `chat.openai.com`",
)
@click.option(
    '-C',
    '--cookie-path',
    type = click.Choice([click.Path(exists=True)]),
    help="Path to .json file containing cookies for `chat.openai.com`",
    prompt="Enter path to .json file containing cookies for `chat.openai.com`",
    envar='openai_cookie_file',
)
@click.option(
    '-M',
    '--model',
    help="ChatGPT's model to be used",
    envar="chatgpt_model",
    default='text-davinci-002-render-sha',
)
@click.option(
    '-I',
    '--index',
    help="Conversation index to resume from",
    type=click.Choice([click.INT]),
    default=0
)
@click.option(
    "-P",
    "--prompt",
    help="Start conversation with this messsage",
)
def interactive(
    auth, cookie_path, model, index, prompt
):
    """Chat with ChatGPT interactively
    """
    bot = ChatGPT(
        auth,
        cookie_path,
        model,
        index

    )
    def output(
            md_format_text:str
    ):
        bot = InteractiveChatGPT(auth,cookie_path,model,index)
        if prompt:
            bot.do_default(
                prompt
            )
        bot.cmdloop()


@chat.command()
@click.option(
    '-A','--auth',
    help="OpenAI's authorization value",
    envar='openai_authorization',
    prompt="Enter authorization value for `chat.openai.com`",
)
@click.option(
    '-C',
    '--cookie-path',
    type = click.Choice([click.Path(exists=True)]),
    help="Path to .json file containing cookies for `chat.openai.com`",
    prompt="Enter path to .json file containing cookies for `chat.openai.com`",
    envar='openai_cookie_file',
)
@click.option(
    '-M',
    '--model',
    help="ChatGPT's model to be used",
    envar="chatgpt_model",
    default='text-davinci-002-render-sha',
)
@click.option(
    '-I',
    '--index',
    help="Conversation index to resume from",
    type=click.Choice([click.INT]),
    default=0
)
@click.option(
    "-P",
    "--prompt",
    help="Start conversation with this messsage",
)
def generate(
    auth, cookie_path, model, index, prompt
):
    """Generate a quick response with ChatGPT
    """
    
    content = ChatGPT(
        auth, cookie_path, model, index
    ).chat(
        prompt
    )

    rich.print(
        rich.markdown.Markdown(
            content
        )
    )

def main():
    chat()