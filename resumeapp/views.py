from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Resumeform
from .models import Resume
from .utils import extract_skills, extract_education #extract_experience_entities
import fitz
import os
# Create your views here.


def extract_text_from_pdf(path):
    try:
        print("[INFO] Extracting text from PDF:", path)
        text = ""
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        print("[ERROR] Failed to extract PDF text:", e)
        return ""

def resume_upload_view(request):
    if request.method == 'POST':
        form = Resumeform(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            file_path = resume.file.path
            
             # STEP 1: Extract raw text from file
            text =extract_text_from_pdf(file_path)

            # STEP 2: Run NLP Analysis
            skills = extract_skills(text)
            education = extract_education(text)
            # experience = extract_experience_entities(text)
            print("Uploaded file path:", file_path)

           # text = extract_text_from_pdf(file_path)
            return render(request, 'resumeapp/resume_result.html', {
                'text': text,
                'skills': skills,
                'education': education,
                # 'experience': experience
            })
    else:
        form = Resumeform()

    return render(request, 'resumeapp/upload.html', {'form': form})
