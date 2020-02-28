from rasa_sdk.events import AllSlotsReset
from typing import Dict, List, Text, Any, Union
import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



class ReferFriendForm(FormAction):

    def name(self):
        return "refer_friend_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "FriendName",
            "FriendEmail",
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "FriendName": [self.from_text(intent=None)],
            "FriendEmail": [self.from_text(intent=None)]
        }

    # first name alphabetical text only validation
    def validate_FriendName(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.strip().isalpha():
            return {"FriendName": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"FriendName": None}

    # email validation
    def validate_FriendEmail(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_email="[^@]+@[^@]+\.[^@]+"

        if re.search(reg_email,value):
            return {"FriendEmail": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"FriendEmail": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch with Hsenid Mobile")
        return [AllSlotsReset()]
