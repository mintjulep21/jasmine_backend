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
            input={"prompt": "extremely detailed face, masterpiece, cinematography, hyper realistic, extremely detailed, 4k, award-winning, drama movie" + prompt, "width": 768, "height": 512, "negative_prompt": "(worst quality:2),(low quality:2),(blurry:2),bad_prompt,text, disfigured, ugly face, (bad and mutated hands:1.3),(bad hands),badhandv4,mutated hands, bad anatomy, missing fingers,extra fingers,fused fingers,too many fingers,(interlocked fingers:1.2), extra limbs,malformed limbs,multiple limbs, extra arms, extra legs, long neck, cross-eyed, negative_hand, negative_hand-neg, text, label, caption, ugly, black and white"},
            api_token=self.replicate_api_token
        )
        return output
