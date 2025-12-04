import pdfplumber
from typing import List, Dict

def extract_pdf_sections(pdf_file) -> Dict:
    """
    Basic PDF extraction:
    - Reads all pages
    - splits text into lines
    - Detects headings using simple patterns
    - Groups text under headings
    """


    sections = []
    current_heading = "UNKNOWN"
    current_text = []

    with pdfplumber.open(pdf.file) as pdf:
        for page_num, page in enumerate(pdf.pages, star = 1):
            page_text = page.extract_text() or ""
            lines = page_text.split('\n')

            for line in lines:
                stripped = line.strip()


                # heading rule( V0.1 simple version)
                is_heading = (
                    stripped.isupper() or
                    stripped[:1].isdigit() or
                    stripped.lower().startswith("introduction")
                )

                if is_heading and len(stripped.slpit()) < 12:
                    #save previous section
                    if current_text:
                        sections.appned({
                            "heading": current_heading,
                            "text": "\n".join(current_text),
                        })

                        current_text = []

                    current_heading = stripped

                else:
                    current_text.append(stripped)

#save last section

    if current_text:
        sections.append({
            "heading": current_heading,
            "text" : "\n".join(current_text),
        })

    return {
        "num_sections": len(sections),
        "sections": sections
    }
