# PaddleOCR Test

Extract English text from receipt and document images using PaddleOCR and a Flask web interface.

## Setup and run

Run in PowerShell from the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000, upload an image, and click **Extract text**. These commands use the virtual environment directly; activation is optional.

## Command-line example

Save your image as `receipt.jpg`, then run:

```powershell
.\.venv\Scripts\python.exe test_ocr.py
```

The script saves an annotated image and JSON results in `output/`.

## Sample OCR comparison

Visual comparison of the supplied student analytics worksheet and recognized-text screenshots:

| Element | Result |
| --- | --- |
| Headings and questions | All 16 questions appear in order; most wording appears preserved |
| Field names, student IDs, and grades | Appear preserved |
| Circular bullets | Recognized as unwanted `o`-like characters |
| Layout | Fragmented lines; colors, bold text, and indentation are not preserved |

This is a visual review, not a measured accuracy score. The app displays plain text, so some layout differences come from browser rendering.

## Notes

- English OCR is enabled; orientation correction and document unwarping are disabled.
- Flask's built-in server is for local testing.
