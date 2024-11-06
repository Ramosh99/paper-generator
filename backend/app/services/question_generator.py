from typing import List
import random
from .vector_db import VectorDB

class QuestionGenerator:
    def __init__(self, vector_db: VectorDB):
        self.vector_db = vector_db

    def generate_paper(self, 
                      topics: List[str], 
                      difficulty: int,
                      num_questions: int) -> List[dict]:
        questions = []
        
        for topic in topics:
            # Get topic-specific questions
            topic_questions = self.vector_db.search_similar(
                query=topic,
                n_results=num_questions // len(topics)
            )
            
            # Filter by difficulty and add to paper
            filtered_questions = [
                q for q in topic_questions 
                if q['metadata']['difficulty'] == difficulty
            ]
            questions.extend(filtered_questions)
        
        # Randomize question order
        random.shuffle(questions)
        return questions[:num_questions]