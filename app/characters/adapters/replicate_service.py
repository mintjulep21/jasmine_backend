import os
import replicate
from typing import Any, Dict


class ReplicateService:
    def __init__(self):
        self.replicate_model_key = "prompthero/dreamshaper:6197db9cdf865a7349acaf20a7d20fe657d9c04cc0c478ec2b23565542715b95"
        self.replicate_api_token = os.getenv('REPLICATE_API_TOKEN')

    def generate_image(self, prompt: str) -> Dict[str, Any]:
        # Assuming you need to pass the API token to replicate.run
        output = replicate.run(
            self.replicate_model_key,
            input={"prompt": prompt + "masterpiece, cinematography, hyper realistic, award-winning, drama movie", "width": 768, "height": 512, "num_outputs": 4},
            api_token=self.replicate_api_token
        )
        return output
