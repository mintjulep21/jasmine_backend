# adapters/replicate_service.py
from typing import Any, Dict
import replicate
import os


os.environ["REPLICATE_API_TOKEN"] = "r8_ETuXWhy82eXqkVC6p5od1Npt6y6N6F82IWr9P"


class ReplicateService:
    def generate_image(self, prompt: str):
        output = replicate.run(
            "prompthero/dreamshaper:\
                6197db9cdf865a7349acaf20a7d20fe657d9c04cc0c478ec2b23565542715b95",
            input={"prompt": prompt}
        )
        return output
