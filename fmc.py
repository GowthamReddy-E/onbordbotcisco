"""from webexteamssdk.models.cards import CardAction, ActionType
from webexteamssdk.models.cards.actions import ShowCard
from webexteamssdk.models.cards import CardElementType
from webexteamssdk.models.cards import Fact
from webexteamssdk.models.cards import Section
from webexteamssdk.models.cards import InputChoiceSet
from webexteamssdk.models.cards import InputText
from webexteamssdk.models.cards import MessageCard

from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, Text, HorizontalAlignment
from webexteamssdk.models.cards.actions import Submit
from webex_bot.formatting import quote_info
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

class FMCCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="fmc",
            help_message="fmc",
        )
    
    def execute(self, message, attachment_actions, activity):
        text1 = TextBlock("FMC (Firepower Management Center)", weight=FontWeight.BOLDER, wrap=True, size=FontSize.MEDIUM, color=Colors.DARK)
        text2 = TextBlock("FMC manages the network security, detects and prevents intrusion attempts. FMC has a robust architecture for managing security policies and network events.", wrap=True, color=Colors.DARK)
        text3 = TextBlock("Additional Resources", weight=FontWeight.BOLDER, size=FontSize.MEDIUM, color=Colors.DARK)
        
        # Define individual links
        link1 = CardAction(title="FMC - Architecture", type=ActionType.OpenUrl, value="https://confluence-eng-rtp2.cisco.com/conf/display/DEV/FMC+-Architecture")
        link2 = CardAction(title="UM New Hire Trainings", type=ActionType.OpenUrl, value="https://wiki.cisco.com/display/DRAMBUIE/UM+New+Hire+Trainings")
        link3 = CardAction(title="FMC Quick Start Guide", type=ActionType.OpenUrl, value="https://www.cisco.com/c/en/us/td/docs/security/asa/quick_start/sfr/firepower-qsg.html")
        link4 = CardAction(title="Onboarding FMC to CDO using SecureX", type=ActionType.OpenUrl, value="https://confluence-eng-rtp2.cisco.com/conf/display/NTD/Onboarding+an+On-Prem+FMC+to+CDO+using+SecureX")
        link5 = CardAction(title="FMC Documentation", type=ActionType.OpenUrl, value="https://confluence-eng-rtp2.cisco.com/conf/pages/viewpage.action?pageId=487509705")
        link6 = CardAction(title="FMC backup - FMC Documentation", type=ActionType.ShowCard, value="backup_fmc")

        # Define backup FMC section
        backup_fmc_section = Section(title="Available info about FMC backup:", facts=[
            Fact(name="FMC - Architecture", value="https://confluence-eng-rtp2.cisco.com/conf/display/DEV/FMC+-Architecture"),
            Fact(name="FMC Documentation", value="https://confluence-eng-rtp2.cisco.com/conf/pages/viewpage.action?pageId=487509705"),
        ])
        
        # Create the main adaptive card
        card = AdaptiveCard(
            body=[
                ColumnSet(columns=[Column(items=[text1])]),
                ColumnSet(columns=[Column(items=[text2])]),
                ColumnSet(columns=[Column(items=[text3])]),
            ],
            actions=[
                link1,
                link2,
                link3,
                link4,
                link5,
                link6
            ]
        )

        # Create the backup FMC adaptive card
        backup_fmc_card = AdaptiveCard(body=[backup_fmc_section])

        # Create response with both cards
        response = {
            "cards": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": card.to_dict()
                },
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": backup_fmc_card.to_dict(),
                    "action": "backup_fmc"
                }
            ]
        }

        return response"""








import logging
from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, Text, HorizontalAlignment
from webexteamssdk.models.cards.actions import Submit
from webex_bot.formatting import quote_info
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

log = logging.getLogger(__name__)

class FMCCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="fm",
            help_message="fm",
            )

    
        
    def execute(self, message, attachment_actions, activity):
        text1 = TextBlock("FMC (Firepower Management Center)", weight=FontWeight.BOLDER, wrap=True, size=FontSize.MEDIUM, color=Colors.DARK)
        text2 = TextBlock("FMC manages the network security, detects and prevents intrusion attempts.FMC has a robust architecture for managing security policies and network events.", wrap=True, color=Colors.DARK)
        text3 = TextBlock("Additional Resources", weight=FontWeight.BOLDER, size=FontSize.MEDIUM, color=Colors.DARK)
        



        
        link1 = TextBlock("- [FMC Architecture](https://confluence-eng-rtp2.cisco.com/conf/display/DEV/FMC+-Architecture)", wrap=True, color=Colors.DARK)
        link2 = TextBlock("- [FMC Documentation](https://www.youtube.com/watch?v=8Y2Zw2wh62k&t=1313s)", wrap=True, color=Colors.DARK)
        link3 = TextBlock("- [FMC NewHire Trainings](https://wiki.cisco.com/display/DRAMBUIE/UM+New+Hire+Trainings)", wrap=True, color=Colors.DARK)
        link4 = TextBlock("- [FMC Module Quick Start Guide](https://www.cisco.com/c/en/us/td/docs/security/asa/quick_start/sfr/firepower-qsg.html)", wrap=True, color=Colors.DARK)
        link5 = TextBlock("- [Onboarding an On-Prem FMC to CDO using SecureX](https://confluence-eng-rtp2.cisco.com/conf/display/NTD/Onboarding+an+On-Prem+FMC+to+CDO+using+SecureX)", wrap=True, color=Colors.DARK)
        link6 = TextBlock("- [FMC/FTD Deployment videos](https://confluence-eng-rtp2.cisco.com/conf/pages/viewpage.action?pageId=487509705)", wrap=True, color=Colors.DARK)
        link7 = TextBlock("- [FTD Device Configuration Import / Export in FMC](https://confluence-eng-rtp2.cisco.com/conf/pages/viewpage.action?pageId=344072453)", wrap=True, color=Colors.DARK)
        link8 = TextBlock("- [Confluence Engineering - RTP2](https://confluence-eng-rtp2.cisco.com/conf/)", wrap=True, color=Colors.DARK)
        
        card = AdaptiveCard(
            body=[
                ColumnSet(columns=[Column(items=[text1])]),
                ColumnSet(columns=[Column(items=[text2])]),
                ColumnSet(columns=[Column(items=[text3, link1, link2,link3,link4,link5,link6,link7,link8])]),
            ]
        )


        return response_from_adaptive_card(card)




