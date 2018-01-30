from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.events import SlotSet

logger = logging.getLogger(__name__)


class ActionPasswordReset(Action):
    def name(self):
        return 'action_change_password'

    def run(self, dispatcher, tracker, domain):
	password = tracker.get_slot('password')
        dispatcher.utter_message("Your password is reset.")
        return []