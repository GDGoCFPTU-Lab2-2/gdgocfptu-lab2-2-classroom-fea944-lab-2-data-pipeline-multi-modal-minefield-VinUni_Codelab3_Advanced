import google.generativeai as genai
import os

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Use Gemini API to extract structured data from lecture_notes.pdf

def extract_pdf_data(file_path):
    # --- FILE CHECK (Handled for students) ---
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    # ------------------------------------------

    # TODO: Initialize Gemini API (make sure GEMINI_API_KEY is set)
    # TODO: Load the PDF file
    # TODO: Send a prompt to Gemini to extract: Title, Author, and a Summary.
    # TODO: Return a dictionary that fits the UnifiedDocument schema.
    
    return {}

