import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Clean the transcript text and extract key information.

def clean_transcript(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # ------------------------------------------
    
    # TODO: Remove noise tokens like [Music], [inaudible], [Laughter]
    # TODO: Strip timestamps [00:00:00]
    # TODO: Find the price mentioned in Vietnamese words ("năm trăm nghìn")
    # TODO: Return a cleaned dictionary for the UnifiedDocument schema.
    
    return {}

