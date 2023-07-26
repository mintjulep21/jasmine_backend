# router_imitate.py
from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/imitate")
def imitate(
    text: str,
    author: str,
    svc: Service = Depends(get_service),
):
    # Generate script imitating author's style using OpenAI
    script = svc.openai_service.imitate_style(text, author)

    # Save to the database
    result = svc.repository.save_script(text, author, script)

    if result:
        return {"status": "success", "script": script}
    else:
        raise HTTPException(status_code=500, detail="Failed to generate script")
