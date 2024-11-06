import PyPDF2
import nltk
from typing import List
import hashlib

class PDFProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

    def extract_text(self, pdf_path: str) -> str:
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text

    def process_document(self, pdf_path: str) -> dict:
        text = self.extract_text(pdf_path)
        sentences = nltk.sent_tokenize(text)
        
        # Create content hash
        content_hash = hashlib.md5(text.encode()).hexdigest()
        
        # Basic question extraction (enhance this based on your needs)
        questions = [s for s in sentences if '?' in s]
        
        return {
            'content': text,
            'content_hash': content_hash,
            'questions': questions
        }