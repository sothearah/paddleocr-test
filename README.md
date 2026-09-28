# PaddleOCR Test

Extract English text from receipt and document images using PaddleOCR and a Flask web interface.

## Setup and run

Run in PowerShell from the project folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt --extra-index-url https://www.paddlepaddle.org.cn/packages/stable/cpu/
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000, upload an image, and click **Extract text**. These commands use the virtual environment directly.

## Notion Link

https://dust-seagull-cdd.notion.site/OCR-Implementation-3e9dc39ce06a80e4b8c0d2c9fa7e6452