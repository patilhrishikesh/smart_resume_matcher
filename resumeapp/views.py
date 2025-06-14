from django.shortcuts import render, redirect
from .forms import Resumeform
from .models import Resume
from .utils import (
    extract_resume_text,  # handles .pdf and .docx
    extract_skills,
    extract_education,
    match_jobs
)

def resume_upload_view(request):
    if request.method == 'POST':
        form = Resumeform(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            file_path = resume.file.path
            print("Uploaded file path:", file_path)

            # STEP 1: Extract resume text (PDF or DOCX)
            resume_text = extract_resume_text(file_path)

            # STEP 2: Run NLP analysis
            extracted_skills = extract_skills(resume_text)
            extracted_education = extract_education(resume_text)

            print("[DEBUG] Extracted Resume Skills:", extracted_skills)

            # STEP 3: Match jobs
            matched_jobs = match_jobs(extracted_skills)

            # STEP 4: Render results
            return render(request, 'resumeapp/resume_result.html', {
                'text': resume_text,
                'skills': extracted_skills,
                'education': extracted_education,
                'jobs': matched_jobs.to_dict(orient='records')
            })
    else:
        form = Resumeform()

    return render(request, 'resumeapp/upload.html', {'form': form})

def home_view(request):
    return render(request, 'resumeapp/home.html')