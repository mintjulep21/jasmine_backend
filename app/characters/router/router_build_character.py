# router_build_character.py
from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/")
def build_character(
    text: str,
    svc: Service = Depends(get_service),
):

    image = svc.replicate_service.generate_image(text)
    result = svc.repository.save_character_image(text, image)

    if result:
        return {"status": "success", "image": image}
    else:
        raise HTTPException(status_code=500, detail="Failed to generate character image")
