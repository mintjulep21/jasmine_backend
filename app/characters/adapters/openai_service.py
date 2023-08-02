from typing import Any, Dict
import os
from dotenv import load_dotenv
import openai

load_dotenv()


class OpenAIService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_prompt(self, text: str) -> Dict[str, Any]:
        instruction = "Act like a script writer assistant with Hollywood expertise.\
            Build a character from the following description: "
        prompt_text = instruction + text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            temperature=0.9,
            max_tokens=1000,
        )
        return response.choices[0].text.strip()

    def imitate_style(self, text: str, author: str) -> Dict[str, Any]:
        instruction = f"Rewrite the following script in the style of the director {author}, extremely detailed and close to the director style, do not add too much content: "
        prompt_text = instruction + text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            temperature=0.9,
            max_tokens=1000,
        )
        return response.choices[0].text.strip()

    def fix_imperfections(self, text: str) -> Dict[str, Any]:
        instruction = "Act like a script writer with Hollywood expertise.\
              Fix the places of text where there is not enough character development, \
                write very creatively and detailedly, do not add too much new content: "
        prompt_text = instruction + text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            temperature=0.9,
            max_tokens=1000,
        )
        return response.choices[0].text.strip()

    def build_stage(self, act: str) -> Dict[str, Any]:
        instruction = f"Act as a script writer assistant with Hollywood expertise.\
              Generate a detailed stage description for this script act: {act}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=instruction,
            temperature=0.9,
            max_tokens=1000,   
        )
        return response.choices[0].text.strip()

    def finish_thought(self, incomplete_text: str) -> Dict[str, Any]:
        instruction = f"Act as a script writer assistant with Hollywood expertise.\
        Add 1-2 sentences to extend idea, make it extremely detailed like you would write a screenplay, and do NOT change the original text: \
                    {incomplete_text}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=instruction,
            temperature=0.9,
            max_tokens=1000,
        )
        return response.choices[0].text.strip()
