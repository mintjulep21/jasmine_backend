# router_build_stage.py
from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/build_stage")
def build_stage(
    act: str,
    svc: Service = Depends(get_service),
):
    # Use OpenAI to generate a stage description
    stage_description = svc.openai_service.build_stage(act)

    # Save to the database
    result = svc.repository.save_stage_description(act, stage_description)

    if result:
        return {"status": "success", "stage_description": stage_description}
    else:
        raise HTTPException(status_code=500, detail="Failed to build stage description")
