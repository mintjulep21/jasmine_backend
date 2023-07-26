# router_finish_thought.py
from fastapi import Depends, HTTPException
from ..service import Service, get_service
from . import router


@router.post("/finish_thought")
def finish_thought(
    incomplete_text: str,
    svc: Service = Depends(get_service),
):
    # Use OpenAI to extend the incomplete thought
    extended_idea = svc.openai_service.finish_thought(incomplete_text)

    # Save to the database
    result = svc.repository.save_extended_idea(incomplete_text, extended_idea)

    if result:
        return {"status": "success", "extended_idea": extended_idea}
    else:
        raise HTTPException(status_code=500, detail="Failed to finish thought")
