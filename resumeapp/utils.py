import os
import spacy
import pandas as pd
import docx
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# ---------------------------
# SKILL KEYWORDS LIST
# ---------------------------
SKILL_KEYWORDS = [
    # Languages
    "python", "java", "c++", "scala", "r", "matlab", "bash",

    # ML Libraries
    "scikit-learn", "xgboost", "lightgbm", "catboost", "mlflow", "joblib",

    # Deep Learning
    "tensorflow", "keras", "pytorch", "torchvision", "fastai", "onnx", "jax",

    # NLP
    "nltk", "spacy", "transformers", "huggingface", "gensim", "bert", "gpt", "llama", "t5", "langchain", "haystack",

    # Data Analysis
    "pandas", "numpy", "scipy", "dask", "polars",

    # Visualization
    "matplotlib", "seaborn", "plotly", "dash", "power bi", "tableau", "superset",

    # Cloud
    "aws", "gcp", "azure", "sagemaker", "ec2", "s3", "bigquery", "vertex ai", "lambda", "cloud functions",

    # Data Engineering
    "airflow", "luigi", "spark", "kafka", "hadoop", "databricks", "snowflake", "redshift",

    # MLOps / Deployment
    "docker", "kubernetes", "dvc", "git", "github actions", "flask", "fastapi", "streamlit", "gradio",

    # Databases
    "mysql", "postgresql", "mongodb", "sqlite", "elasticsearch", "redis", "neo4j",

    # Evaluation
    "cross-validation", "gridsearch", "f1 score", "precision", "recall", "confusion matrix"
]

# ---------------------------
# TEXT EXTRACTION FUNCTIONS
# ---------------------------
def extract_text_from_pdf(path):
    text = ""
    with fitz.open(path) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs]).strip()

def extract_resume_text(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(path)
    elif ext == '.docx':
        return extract_text_from_docx(path)
    return ""

# ---------------------------
# NLP EXTRACTION FUNCTIONS
# ---------------------------
def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILL_KEYWORDS if skill in text]
    return list(set(found_skills))

def extract_education(text):
    degrees = ["bachelor", "master", "b.tech", "bsc", "msc", "phd", "engineering", "computer science"]
    text = text.lower()
    return [deg for deg in degrees if deg in text]

# ---------------------------
# JOB MATCHING FUNCTION
# ---------------------------
def match_jobs(resume_skills, top_n=3):
    df = pd.read_csv("jobs.csv")

    # Normalize headers
    df.columns = df.columns.str.strip().str.lower()  # → ensures lowercase column access

    # Replace commas in job skills with spaces
    df['skills'] = df['skills'].str.lower().str.replace(",", " ")

    resume_text = " ".join(resume_skills).lower()
    corpus = [resume_text] + df['skills'].tolist()

    # Vectorize and compute cosine similarity
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Add scores and return top matches
    df['match_score'] = similarity_scores
    top_matches = df[df['match_score'] > 0.0].sort_values(by='match_score', ascending=False).head(top_n)

    return top_matches[['role', 'company', 'skills', 'match_score']]
