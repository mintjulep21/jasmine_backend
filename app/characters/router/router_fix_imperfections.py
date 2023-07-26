from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/fix_imperfections")
def fix_imperfections(
    text: str,
    svc: Service = Depends(get_service),
):

    corrected_script = svc.openai_service.fix_imperfections(text)

    result = svc.repository.save_corrected_script(text, corrected_script)

    if result:
        return {"status": "success", "corrected_script": corrected_script}
    else:
        raise HTTPException(status_code=500, detail="Failed to correct script")
