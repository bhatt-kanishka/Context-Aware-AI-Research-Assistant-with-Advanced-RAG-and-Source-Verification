from pathlib import Path
from pypdf import PdfReader

def load_pdfs(data_folder= "data"):
    documents = []

    data_path = Path(data_folder)

    for pdf_file in data_path.glob("*.pdf"):

        reader = PdfReader(pdf_file)

        for pdf_file in data_path.glob("*.pdf"):

            reader = PdfReader(pdf_file)

            for page_number  , page in enumerate(reader.pages ,start=1):

                text = page.extract_text()

                if text and text.strip():
                    documents.append({
                        "text" : text,
                        "metadata": {
                        "source": pdf_file.name,
                        "page": page_number
                        }
                    })
    return documents 
    

