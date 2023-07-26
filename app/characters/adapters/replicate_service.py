# adapters/replicate_service.py
# adapters/replicate_image_service.py
from typing import Any, Dict
import os
from dotenv import load_dotenv
import replicate

load_dotenv()


class ReplicateService:
    def __init__(self):
        self.replicate_model_key = os.getenv('REPLICATE_MODEL_KEY')

    def generate_image(self, prompt: str) -> Dict[str, Any]:
        output = replicate.run(
            self.replicate_model_key,
            input={"prompt": prompt}
        )
        return output
