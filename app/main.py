from fastapi import FastAPI, UploadFile, File
from app.extraction.extractor import extract_pdf_sections

app = FastAPI()

@app.get("/health")
async def read_root():
    return {"status": "ok"}

@app.post("/compare")
async def compare_pdfs(pdf_a: UploadFile = File(...),
                       pdf_b: UploadFile = File(...)):
    
    # Read file Objects

    a_sections = extract_pdf_sections(pdf_a.file)
    b_sections = extract_pdf_sections(pdf_b.file)
    
    return {
        "message": "pdf received",
        "pdf_a_sections": a_sections,
        "pdf_b_sections": b_sections,
    }