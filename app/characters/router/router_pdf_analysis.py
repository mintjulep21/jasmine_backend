# router_pdf_analysis.py

from fastapi import Depends, HTTPException, UploadFile, File
from ..service import Service, get_service
from . import router


@router.post("/analyze_pdf")
async def analyze_pdf(
    file: UploadFile = File(...),
    svc: Service = Depends(get_service),
):
    if file.filename.endswith(".pdf"):
        analysis = svc.pdf_service.analyze_pdf(file.file)
        return {"status": "success", "analysis": analysis}
    else:
        raise HTTPException(status_code=400, detail="Please upload a PDF file")
