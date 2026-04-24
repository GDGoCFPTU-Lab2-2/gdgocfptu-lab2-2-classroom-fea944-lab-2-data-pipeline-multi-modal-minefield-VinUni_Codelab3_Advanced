# Codelab 03 v1: The Multi-Modal Minefield (Advanced Edition)
**Author**: Võ Tự Đức (VinUni AI Lab)
**Duration**: 3 Hours (10:00 – 13:00)

## Overview
Welcome to the advanced edition of the Data Pipeline Engineering lab. You are now working on a "Production Reality" project. The data is real, messy, and multi-source. The expectations are high.

📖 **Student Guides**: [English](STUDENT_GUIDE.md) | [Vietnamese](STUDENT_GUIDE_VN.md)


## Your Team & Roles
You must split into 4 roles. You will be graded both on your individual contribution (tracked via GitHub commits) and the final performance of the pipeline.

1. **Lead Data Architect (Role 1)**: Defines the Data Contract (`schema.py`). Must anticipate the mid-lab schema migration.
2. **ETL/ELT Builder (Role 2)**: The primary coder. Responsible for the 5 processing scripts. Uses Gemini API for PDF extraction.
3. **Observability & QA Engineer (Role 3)**: The Watchman. Writes semantic gates and captures business logic from legacy code.
4. **DevOps & Integration Specialist (Role 4)**: The Connector. Orchestrates the DAG and ensures the final JSON is valid.

## The Challenges

### 1. Real Data Extraction (Gemini API)
You must use the Gemini API to extract structured metadata from `lecture_notes.pdf`. 
- **Task**: Pass the PDF to Gemini with a prompt asking for: Title, Author, Main Topics, and any Tables.
- **Trap**: Gemini's response is a string. You must parse it into your `UnifiedDocument` schema.
- **SLA**: Implement Exponential Backoff for `429` errors.

### 2. Multi-Source Ingestion
You must process 5 different sources:
- **PDF**: Real layout, tables, footnotes.
- **Transcript**: Noise tokens, speaker labels, Vietnamese words.
- **HTML**: Boilerplate (nav/footer) vs. Content (table).
- **CSV**: Type traps, duplicates, mixed date formats.
- **Legacy Code**: Business rules hidden in docstrings.

### 3. The Mid-Lab Incident (T+60m)
At 11:00 AM, a breaking change will be announced. You must migrate your schema and all processing scripts to **v2** (e.g., field renames) without breaking the pipeline.

### 4. Forensic Debrief
After submission, an automated `agent_forensic.py` will ask your data questions. If your pipeline allowed garbage through, your Agent will fail.

## Setup
1. `pip install -r requirements.txt`
2. Set your `GEMINI_API_KEY` as an environment variable.
3. Add `lecture_notes.pdf` to `raw_data/`.
4. Start with `starter_code/schema.py`.
