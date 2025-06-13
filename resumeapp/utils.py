import spacy
import os
# Load spaCy English NLP model (do once)
nlp = spacy.load("en_core_web_sm")

# Hardcoded skill set (could be replaced by a DB later)
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


def extract_skills(text):
    text = text.lower()
    
    founded_skills = [skill for skill in SKILL_KEYWORDS if skill in text]
    return list(set(founded_skills))

def extract_education(text):
    
    degrees = ["bachelor", "master", "b.tech", "bsc", "msc", "phd", "engineering", 'computer scinece']
    text = text.lower()
    return [deg for deg in degrees if deg in text]

# def extract_experience_entities(text):
#     doc = nlp(text)
#     return [ent.text for ent in doc.ents if ent.label_ == "ORG"]