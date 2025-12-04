from fastapi import FastAPI, UploadFile, File
from app.extraction.extractor import extract_pdf_sections

app = FastAPI()

@app.get("/health")
async def read_root():
    return {"status": "ok"}

@app.post("/compare")
async def compare_pdfs(pdf_a: UploadFile = File(...),
                       pdf_b: UploadFile = File(...)):
    
    """
    Endpoint to compare two PDFs.
    V0: we only parse them into sections and return the raw sections.
    Later we will add similarity + pharma logic.
    """
 
    # Use our extractor on the underlying file-like object (.file)
    # Note: extract_pdf_sections expects a file-like object, not UploadFile directly.

    a_sections = extract_pdf_sections(pdf_a.file)
    b_sections = extract_pdf_sections(pdf_b.file)
    
    return {
        "message": "pdf received",
        "pdf_a_sections": a_sections,
        "pdf_b_sections": b_sections,
    }