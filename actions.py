# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from typing import Dict, Text, Any, List

from typing import Dict, List, Text, Any, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import re

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class UserDetailForm(FormAction):
    """Collects  information from user"""

    def name(self):
        return "user_detail_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "first_name",
            "last_name",
            "dob",
            "address",
            "phone",
            "email",
        ]



    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "first_name": [self.from_text()],
            "last_name": [self.from_text(intent=None)],
            "dob":[self.from_text(intent=None)],
            "address":[self.from_text(intent=None)],
            "phone":[self.from_text(intent=None)],
            "email":[self.from_text(intent=None)]
        }

    def validate_first_name (
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.strip().isalpha():
            return {"first_name": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"first_name": None}

    def validate_last_name (
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.strip().isalpha():
            return {"last_name": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"last_name": None}

    def validate_dob (
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_string = "^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$"

        if re.search(reg_string,value):
            return {"dob": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"dob": None}

    def validate_phone (
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:


        if value.strip().isdigit() and len(value.strip())==10:
            return {"phone": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"phone": None}

    def validate_email(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        reg_email="[^@]+@[^@]+\.[^@]+"

        if re.search(reg_email,value):
            return {"email": value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            return {"email": None}

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch")
        return []