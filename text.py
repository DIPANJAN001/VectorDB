import PyPDF2
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

def tokenize_and_embed(text):
    # Process the text using spaCy
    doc = nlp(text)

    # Tokenize sentences
    sentences = [sent.text for sent in doc.sents]

    # Embed sentences
    embeddings = [sent.vector for sent in doc.sents]

    return embeddings