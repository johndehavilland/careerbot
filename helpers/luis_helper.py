# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from botbuilder.ai.luis import LuisRecognizer, LuisApplication
from botbuilder.core import TurnContext

from jobsearch import JobSearch

class LuisHelper:
    
    @staticmethod
    async def excecute_luis_query(configuration: dict, turn_context: TurnContext) -> JobSearch:
        job_search = JobSearch()
        
        #try:
        luis_application = LuisApplication(
            configuration['LUIS_APP_ID'],
            configuration['LUIS_API_KEY'],
            configuration['LUIS_API_HOST_NAME']
        )

        recognizer = LuisRecognizer(luis_application)
        recognizer_result = await recognizer.recognize(turn_context)
        print("recognizer")
        print(recognizer_result);
        if recognizer_result.intents:
            intent = sorted(recognizer_result.intents, key=recognizer_result.intents.get, reverse=True)[:1][0]
            
            if intent == 'FindJob':
                # We need to get the result from the LUIS JSON which at every level returns an array.
                jobtype_entity = recognizer_result.entities.get("$instance", {}).get("jobtype", [])
                if len(jobtype_entity) > 0:
                    job_search.jobtype = jobtype_entity[0]['text']
                location_entities = recognizer_result.entities.get("$instance", {}).get("location", [])
                if len(location_entities) > 0:
                    job_search.location = location_entities[0]['text']

        # except Exception as e:
        #     print("ERROR")
        #     print(e)
            
        return job_search

