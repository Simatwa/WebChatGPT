import unittest
from WebChatGPT import ChatGPT


class TestChatGPT(unittest.TestCase):
    @unittest.expectedFailure
    def SetUp(self):
        self.bot = ChatGPT("", "")

    @unittest.expectedFailure
    def test_bot(self):
        """Testing bot"""
        self.assertIsInstance(self.bot.ask("hello world"), dict)

    @unittest.expectedFailure
    def test_chat(self):
        """Testing chat"""
        self.assertIs(self.bot.chat("hello there"), str)

    @unittest.expectedFailure
    def test_user_details(self):
        self.assertIs(self.bot.user_details(), dict)
        self.assertIs(self.bot.user_details(in_details=True), dict)

    @unittest.expectedFailure
    def test_prompt_library(self):
        self.assertIs(self.bot.prompt_library(), dict)

    @unittest.expectedFailure
    def test_previous_conversations(self):
        self.assertIs(self.bot.previous_conversations(), dict)

    @unittest.expectedFailure
    def test_gen_title(self):
        self.assertIs(self.bot.gen_title("", ""), dict)


if __name__ == "__main__":
    unittest.main()
