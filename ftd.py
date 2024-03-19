import logging
from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, Text, HorizontalAlignment
from webexteamssdk.models.cards.actions import Submit
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

log = logging.getLogger(__name__)

class FTDCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="ftd",
            help_message="Information about FTD (Firepower Threat Defense)",
            )

    def execute(self, message, attachment_actions, activity):
        text1 = TextBlock("FTD (Firepower Threat Defense)", weight=FontWeight.BOLDER, wrap=True, size=FontSize.MEDIUM, color=Colors.DARK)
        text2 = TextBlock("FTD provides advanced threat protection across the entire attack continuum, detects malware and automatically takes measures to stop threats.", wrap=True, color=Colors.DARK)
        text3 = TextBlock("Additional Resources", weight=FontWeight.BOLDER, size=FontSize.MEDIUM, color=Colors.DARK)


        link1 = TextBlock("- [FTD Documentation](https://www.cisco.com/c/en/us/td/docs/security/secure-firewall/landing-page/threat-defense/threatdefense-71-docs.html)", wrap=True, color=Colors.DARK)
        link2 = TextBlock("- [Firepower Threat Defense](https://wiki.cisco.com/display/ELEV8/Firepower+Threat+Defense)", wrap=True, color=Colors.DARK)
        link3 = TextBlock("- [FirePower NewHire Trainings](https://wiki.cisco.com/display/DRAMBUIE/UM+New+Hire+Trainings)", wrap=True, color=Colors.DARK)
        link4 = TextBlock("- [FTD On-Box Management](https://confluence-eng-rtp2.cisco.com/conf/display/IFT/FTD+On-Box+Management)", wrap=True, color=Colors.DARK)
        link5 = TextBlock("- [FTD Roadmap](https://wiki.cisco.com/display/KRTACSEC/%5BFTD%5D+Roadmap)", wrap=True, color=Colors.DARK)
        
        card = AdaptiveCard(
            body=[
                ColumnSet(columns=[Column(items=[text1])]),
                ColumnSet(columns=[Column(items=[text2])]),
                ColumnSet(columns=[Column(items=[text3, link1, link2, link3,link4,link5])]),
            ]
        )

        return response_from_adaptive_card(card)
