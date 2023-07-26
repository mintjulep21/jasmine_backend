# adapters/openai_service.py
# adapters/openai_service.py
from typing import Any, Dict
import os
from dotenv import load_dotenv
import openai

load_dotenv()


class OpenAIService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_prompt(self, text: str) -> Dict[str, Any]:
        instruction = "act like a script writer assistant with Hollywood expertise.\
            Build a character from the following description: "
        prompt_text = instruction + text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_text,
            temperature=0.5,
            max_tokens=1000,
        )
        return response.choices[0].text.strip()

    def imitate_style(self, text: str, author: str) -> Dict[str, Any]:
        instruction = f"Write a short script in the style of {author} about "
        prompt_text = instruction + text
        response = openai.Completion.create(
            engine="text-davinci-002", 
            prompt=prompt_text, 
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].text.strip()

    def fix_imperfections(self, text: str) -> Dict[str, Any]:
        instruction = "act like a script writer assistant with Hollywood expertise.\
              Fix the places of text where there is not enough character development: "
        prompt_text = instruction + text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_text,
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].text.strip()

    def build_stage(self, act: str) -> Dict[str, Any]:
        instruction = f"Act as a script writer assistant with Hollywood expertise.\
              Generate a detailed stage description for this script act: {act}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=instruction,
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].text.strip()

    def finish_thought(self, incomplete_text: str) -> Dict[str, Any]:
        instruction = f"Act as a script writer assistant with Hollywood expertise.\
            Extend the following incomplete thought or idea into a well-developed \
                  concept: {incomplete_text}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=instruction,
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].text.strip()