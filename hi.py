import json
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webex_bot.formatting import quote_info

with open("./hi_rply_card.json", "r") as card:
    INPUT_CARD = json.load(card)


class HICommand(Command):
    class HICallback(Command):
        def __init__(self):
            super().__init__(
                card_callback_keyword="hi_callback", delete_previous_message=True
            )

        def execute(self, message, attachment_actions, activity):
            return quote_info(attachment_actions.inputs.get("message_typed"))

    def __init__(self):
        super().__init__(
            command_keyword="hi",  # Set command_keyword as a string
            help_message=None,
            chained_commands=[self.HICallback()],
            card=INPUT_CARD,
        )

    def execute(self, message, attachment_actions, activity):
        # Check if the message contains either "hi" or "hello"
        if "hi" in message.lower() or "hello" in message.lower():
            return f"Hi there.. How you doing.. need help.."
        else:
            return None  # If neither "hi" nor "hello" is found, return None
