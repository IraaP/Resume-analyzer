import spacy
import json
from textblob import TextBlob

# Load pre-trained NLP model
nlp = spacy.load('en_core_web_sm')

# Load predefined job skills (for AI roles)
with open("models/job_skills.json", "r") as file:
    job_skills = json.load(file)

def analyze_resume(text):
    doc = nlp(text)
    words = set([token.text.lower() for token in doc])

    # Identify missing skills
    required_skills = set(job_skills["AI Engineer"])
    missing_skills = required_skills - words

    # Grammar analysis
    readability_score = round(TextBlob(text).sentiment.polarity, 2)

    # Job Match Score (simple heuristic)
    match_score = round(100 * (1 - len(missing_skills) / len(required_skills)), 2)

    return {
        "missing_skills": list(missing_skills),
        "readability_score": readability_score,
        "job_match_score": match_score
    }