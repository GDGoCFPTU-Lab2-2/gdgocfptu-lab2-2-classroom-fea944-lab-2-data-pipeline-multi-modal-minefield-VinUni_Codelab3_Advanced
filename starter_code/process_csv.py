import pandas as pd

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Process sales records, handling type traps and duplicates.

def process_sales_csv(file_path):
    # --- FILE READING (Handled for students) ---
    df = pd.read_csv(file_path)
    # ------------------------------------------
    
    # TODO: Remove duplicate rows based on 'id'
    # TODO: Clean 'price' column: convert "$1200", "250000", "five dollars" to floats
    # TODO: Normalize 'date_of_sale' into a single format (YYYY-MM-DD)
    # TODO: Return a list of dictionaries for the UnifiedDocument schema.
    
    return []

