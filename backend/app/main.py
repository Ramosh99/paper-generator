from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .services.pdf_processor import PDFProcessor
from .services.vector_db import VectorDB
from .services.question_generator import QuestionGenerator

app = FastAPI()
pdf_processor = PDFProcessor()
vector_db = VectorDB()
question_generator = QuestionGenerator(vector_db)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/document")
async def upload_document(file: UploadFile = File(...)):
    # Save file temporarily
    temp_path = f"temp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Process document
    doc_data = pdf_processor.process_document(temp_path)
    return {"message": "Document processed successfully", "hash": doc_data['content_hash']}

@app.post("/generate/paper")
async def generate_paper(topics: List[str], difficulty: int, num_questions: int):
    paper = question_generator.generate_paper(
        topics=topics,
        difficulty=difficulty,
        num_questions=num_questions
    )
    return {"paper": paper}