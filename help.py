import logging
from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

log = logging.getLogger(__name__)

class HelpCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="help",
            help_message="Show help options.",
            )

    def execute(self, message, attachment_actions, activity):
        title = TextBlock("Need Some Help 🚀", weight=FontWeight.BOLDER, size=FontSize.LARGE, color=Colors.DARK)
        description = TextBlock("Here are some options to get started:\n\n"
                               "🔹 FMC - Firewall Management Center\n"
                               "🔹 FTD - Firepower Threat Defense\n"
                               "🔹 CDFMC - Cloud Defense Management Center\n"
                               "🔹 pcloud - Cloud Storage Service\n"
                               "🔹 perforce - Version Control System\n"
                               "🔹 confluence page - Deails of Product\n"
                               "🔹 backdraft - UI part of FMC\n"
                               "🔹 HA - High Availability of FMC\n"
                               "🔹 backup & restore - Data Backup and Restore of FMC Infra", 
                               wrap=True, color=Colors.DEFAULT)
        
        card = AdaptiveCard(
            body=[
                ColumnSet(columns=[Column(items=[title])]),
                ColumnSet(columns=[Column(items=[description])])
            ]
        )

        return response_from_adaptive_card(card)
