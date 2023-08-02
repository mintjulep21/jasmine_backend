import os
import replicate
from typing import Any, Dict


class ReplicateService:
    def __init__(self):
        self.replicate_model_key = "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"
        self.replicate_api_token = os.getenv('REPLICATE_API_TOKEN')

    def generate_image(self, prompt: str) -> Dict[str, Any]:
        # Assuming you need to pass the API token to replicate.run
        output = replicate.run(
            self.replicate_model_key,
            input={"prompt": prompt},
            api_token=self.replicate_api_token
        )
        return output
