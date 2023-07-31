from app.config import database

from .adapters.openai_service import OpenAIService
from .repository.repository import ScriptRepository
from .adapters.pdf_service import PDFService
from .adapters.replicate_service import ReplicateService


class Service:
    def __init__(self):
        self.repository = ScriptRepository(database)
        self.openai_service = OpenAIService()
        self.pdf_service = PDFService()
        self.replicate_service = ReplicateService()


def get_service():
    svc = Service()
    return svc
