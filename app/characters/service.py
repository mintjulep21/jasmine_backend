from app.config import database

from .adapters.openai_service import OpenAIService
from .repository.repository import ScriptRepository


class Service:
    def __init__(self):
        self.repository = ScriptRepository(database)
        self.openai_service = OpenAIService()


def get_service():
    svc = Service()
    return svc
