{
    "rasa_nlu_data": {
        "common_examples": [## 1                    
* _greet
   - utter_greet
* _request_for_password_reset
   - utter_email
* _inform_email[email=tarun.kumar@gmail.com]
   - utter_PSAID                        
* _inform_PSAID[PSAID=214145]
   - utter_password
* _inform_password[password=adsafa122]
   - action_change_password
* _goodbye
  - utter_goodbye
],
        "regex_features" : ["name": "PSAID",
                "pattern": "[0-9]{6}"],
				
				
        "entity_synonyms": []
    }
}

{
    "rasa_nlu_data": {
        "common_examples": [* _greet
   - utter_greet
* _request_for_password_reset
   - utter_email
* _inform_email[email=sameer.sam@gmail.com]
   - utter_PSAID                        
* _inform_PSAID[PSAID=211245]
   - utter_password
* _inform_password[password=adglgfa122]
   - action_change_password
* _goodbye
  - utter_goodbye],
        "regex_features" : ["name": "PSAID",
                "pattern": "[0-9]{6}"],
        "entity_synonyms": []
    }
}

{
    "rasa_nlu_data": {
        "common_examples": [## reset_password                    
* _greet
   - utter_greet
* _request_for_password_reset
   - utter_email
* _inform_email[email=abcxy@gmail.com]
   - utter_PSAID                        
* _inform_PSAID[PSAID=218735]
   - utter_password
* _inform_password[password=fnsai214]
   - action_change_password
* _goodbye
  - utter_goodbye],
        "regex_features" : ["name": "PSAID",
                "pattern": "[0-9]{6}"],
        "entity_synonyms": []
    }
}