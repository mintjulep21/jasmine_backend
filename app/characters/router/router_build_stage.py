# router_build_stage.py
from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/build_stage")
def build_stage(
    act: str,
    svc: Service = Depends(get_service),
):

    image = svc.replicate_service.generate_image(act)
    result = svc.repository.save_stage_image(act, image)

    if result:
        return {"status": "success", "image": image}
    else:
        raise HTTPException(status_code=500, detail="Failed to generate stage image")
