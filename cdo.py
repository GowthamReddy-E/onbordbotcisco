import logging
from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, Text, HorizontalAlignment
from webexteamssdk.models.cards.actions import Submit
from webex_bot.formatting import quote_info
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

log = logging.getLogger(__name__)

class CDFMCCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="cd",
            help_message="cd",
            )

    
        
    def execute(self, message, attachment_actions, activity):
        text1 = TextBlock("CDFMC (Cloud Firepower Management Center)", weight=FontWeight.BOLDER, wrap=True, size=FontSize.MEDIUM, color=Colors.DARK)
        text2 = TextBlock("CDFMC is a cloud-based platform for managing network security, detecting and preventing intrusion attempts. It provides a scalable and flexible solution for managing security policies and network events in the cloud environment.", wrap=True, color=Colors.DARK)
        text3 = TextBlock("Additional Resources", weight=FontWeight.BOLDER, size=FontSize.MEDIUM, color=Colors.DARK)




        link1 = TextBlock("- [CDO/cdFMC Documentation](https://www.cisco.com/c/en/us/support/docs/security/defense-orchestrator/218171-deploy-a-cloud-delivered-fmc-in-cdo.html)", wrap=True, color=Colors.DARK)
        link2 = TextBlock("- [CDO Support for Firepower](https://confluence-eng-rtp2.cisco.com/conf/display/LH/CDO+Support+for+Firepower)", wrap=True, color=Colors.DARK)
        link3 = TextBlock("- [cdFMC NewHire trainings](https://wiki.cisco.com/display/DRAMBUIE/UM+New+Hire+Trainings)", wrap=True, color=Colors.DARK)
        link4 = TextBlock("- [cdFMC Cloud Onboarding](https://confluence-eng-rtp2.cisco.com/conf/display/IFT/FMC+Cloud+Onboarding)", wrap=True, color=Colors.DARK)
        link5 = TextBlock("- [Deploying/Upgrading cdFMC in CDO Tenant](https://confluence-eng-rtp2.cisco.com/conf/pages/viewpage.action?pageId=420517941)", wrap=True, color=Colors.DARK)
        link6 = TextBlock("- [CDO Support for Firepower](https://confluence-eng-rtp2.cisco.com/conf/display/LH/CDO+Support+for+Firepower)", wrap=True, color=Colors.DARK)
        link6 = TextBlock("- [cdFMC Architecture ](https://confluence-eng-rtp2.cisco.com/conf/display/NTD/cdFMC+Upgrade)", wrap=True, color=Colors.DARK)
        
        card = AdaptiveCard(
            body=[
                ColumnSet(columns=[Column(items=[text1])]),
                ColumnSet(columns=[Column(items=[text2])]),
                ColumnSet(columns=[Column(items=[text3, link1, link2,link3,link4,link5,link6])]),
            ]
        )


        return response_from_adaptive_card(card)
    
