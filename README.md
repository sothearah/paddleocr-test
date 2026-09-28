# PaddleOCR Test

Extract English text from receipt and document images using PaddleOCR and a Flask web interface.

## Setup and run

Run in PowerShell from the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000, upload an image, and click **Extract text**. These commands use the virtual environment directly.