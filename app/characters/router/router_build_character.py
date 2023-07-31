# router_build_character.py
from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/")
def build_character(
    text: str,
    svc: Service = Depends(get_service),
):
    # Generate prompt using OpenAI
    character_description = svc.openai_service.generate_prompt(text)

    # Save to the database
    result = svc.repository.save_character_description(text, character_description)

    #image_data = svc.replicate_service.generate_image(text)

    if result:
        return {
            "status": "success",
            "character description": character_description,
           # "character image": image_data
        }

    else:
        raise HTTPException(status_code=500, detail="Failed to build character")
