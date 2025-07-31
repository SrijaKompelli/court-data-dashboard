# Court-Data Fetcher & Mini-Dashboard

This is a mock-enabled web app that simulates court data retrieval from an Indian District Court (e.g., Gurugram) using Case Type, Number, and Year.

> 🔧 Uses Python, Flask, Bootstrap, and SQLite

## ✅ Features

- User-friendly form to enter case details
- Scraper (mock-mode enabled for demo)
- Displays:
  - Parties involved
  - Filing date
  - Next hearing date
  - Latest order PDF (link)
- Logs each query to SQLite database

---

## 🎥 Demo Input

To simulate a real court record, use this input:

| Field        | Value         |
|--------------|---------------|
| Case Type    | CS            |
| Case Number  | 100           |
| Filing Year  | 2022          |

This returns a hardcoded mock result.

---

## 🚀 Setup Instructions

```bash
git clone <your-repo-url>
cd court_data_dashboard
pip install -r requirements.txt
python app.py
