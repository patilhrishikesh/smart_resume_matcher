from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Resumeform
from .models import Resume
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
            print("Uploaded file path:", file_path)

            text = extract_text_from_pdf(file_path)
            print("[DEBUG] Extracted text preview:", text[:300])

            if not text:
                return render(request, 'resumeapp/resume_result.html', {
                    'error': 'No text could be extracted from the resume.'
                })

            return render(request, 'resumeapp/resume_result.html', {
                'text': text,
                'resume': resume
            })
    else:
        form = Resumeform()

    return render(request, 'resumeapp/upload.html', {'form': form})
