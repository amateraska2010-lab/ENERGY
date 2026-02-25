from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_report(student_text, job_text):
    # Считаем общий процент соответствия
    emb1 = model.encode(student_text)
    emb2 = model.encode(job_text)
    score = util.cos_sim(emb1, emb2).item()
    
    # Очень простая логика поиска недостающих навыков (на основе ключевых слов)
    keywords = ["Python", "SQL", "Docker", "Git", "FastAPI", "React", "Machine Learning"]
    missing = [word for word in keywords if word.lower() in job_text.lower() and word.lower() not in student_text.lower()]
    
    recommendations = [f"Пройти курс по {skill}" for skill in missing]
    
    return {
        "match_percent": round(score * 100, 2),
        "missing_skills": missing,
        "recommendations": recommendations
    }
