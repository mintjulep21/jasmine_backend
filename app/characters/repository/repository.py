from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId
from pymongo.database import Database


# repository.py
class ScriptRepository:
    def __init__(self, database: Database):
        self.database = database

    def save_character_description(self, original_text: str,
                                   character_description: str):
        payload = {
            "original_text": original_text,
            "character_description": character_description,
            "created_at": datetime.utcnow(),
        }
        return self.database["character_descriptions"].insert_one(payload)

    def save_script(self, original_text: str, author: str, script: str):
        payload = {
            "original_text": original_text,
            "author": author,
            "script": script,
            "created_at": datetime.utcnow(),
        }
        return self.database["scripts"].insert_one(payload)

    def save_corrected_script(self, original_text: str, corrected_script: str):
        payload = {
            "original_text": original_text,
            "corrected_script": corrected_script,
            "created_at": datetime.utcnow(),
        }
        return self.database["corrected_scripts"].insert_one(payload)

    def save_stage_description(self, act: str, stage_description: str):
        payload = {
            "act": act,
            "stage_description": stage_description,
            "created_at": datetime.utcnow(),
        }
        return self.database["stage_descriptions"].insert_one(payload)

    def save_extended_idea(self, incomplete_text: str, extended_idea: str):
        payload = {
            "incomplete_text": incomplete_text,
            "extended_idea": extended_idea,
            "created_at": datetime.utcnow(),
        }
        return self.database["extended_ideas"].insert_one(payload)
