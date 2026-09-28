# PaddleOCR Test

A small English text extraction demo using PaddleOCR and Flask. Upload an image in the browser to see recognized text, or run the command-line script to save an annotated image and JSON results.

The interface is labeled **Receipt OCR Test**, but it also accepts other document images, such as the student analytics worksheet discussed below.

## Setup

Use a Python environment compatible with the pinned packages in `requirements.txt`.

From the project directory, run these commands in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install Flask
```

Flask is imported by `app.py` but is currently missing from `requirements.txt`, so it must be installed separately. The installation commands have not been verified in a fresh environment.

## Run the web app

```powershell
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000, choose an image, and click **Extract text**. Recognized lines appear under **Recognized text**. If no text is detected, the page displays a corresponding message.

The app initializes PaddleOCR once at startup with English recognition. Document orientation classification, document unwarping, text-line orientation detection, and MKL-DNN are disabled in the current configuration.

Each upload is saved in a temporary directory and passed to `ocr.predict()`. The app reads `rec_texts` from the generated JSON and renders each recognized entry as a separate HTML element. Temporary files are removed after processing. The web page does not display bounding boxes or recognition confidence scores.

## Run the command-line example

Place the input image at `receipt.jpg`, then run:

```powershell
.\.venv\Scripts\python.exe test_ocr.py
```

The script prints results and saves an annotated image and JSON data in `output/`. Despite its name, `test_ocr.py` is a manual OCR example, not an automated test suite.

## Project files

| Path | Purpose |
| --- | --- |
| `app.py` | Flask upload route and OCR processing |
| `templates/index.html` | Upload form and recognized-text display |
| `test_ocr.py` | Command-line OCR example |
| `requirements.txt` | Pinned dependencies; Flask must currently be installed separately |
| `receipt.jpg` | Input image used by the command-line example |
| `output/` | Saved command-line OCR results |

## Comparison of the supplied screenshots

The source image is an **EXCEL & POWER QUERY DATA ANALYTICS** worksheet titled **Part 1: Student Performance Analytics (Excel Formulas)**. The other screenshot shows its recognized text in the app.

This comparison is a visual review of the two supplied screenshots, not a new OCR run or an automated accuracy measurement. The small output screenshot limits character-level verification.

| Element | Original image | Visible OCR result | Assessment |
| --- | --- | --- | --- |
| Title and section headings | Main title, part title, and `I. Questions` | All appear in the output | Heading content appears preserved |
| Numbered questions | Questions 1 through 16 | All 16 appear in the same order | No whole question appears missing |
| Question wording | Student scores, counts, school types, attendance, and ranking tasks | Main wording appears substantially preserved | Useful extraction of the document's content |
| Field names and IDs | `Pass_Status`, `Grade_Letter`, `STU_0018`, `STU_0042` | These strings appear in the output | Visually preserved; check raw text before downstream use |
| Grade thresholds | 90 or higher: A; 80–89: B; 70–79: C; 60–69: D; below 60: F | The five thresholds and letters appear | Grading meaning appears preserved |
| Grade-list bullets | Hollow circular bullets | Separate `o`-like characters before grade entries | Recognition artifact; bullets become unwanted text |
| Line breaks | Wrapped questions with aligned continuation lines | Extra short lines such as `score is`, `the`, and `following scale:` | Text needs joining for clean paragraphs |
| Visual formatting | Blue title background, bold emphasis, green identifiers, and indentation | Plain text in a narrow result panel | Source styling and list hierarchy are not reproduced |

### Interpretation

The result appears to capture the worksheet's main text and reading order well, but it does not reconstruct the document layout. Some visual differences come from the app itself: it renders only recognized strings, and its narrow panel adds browser wrapping. Those differences should not all be counted as OCR recognition errors.

The clearest visible recognition issue is the conversion of hollow grade-list bullets into letter-like text. Paragraph reconstruction is also needed to make the output easier to read or reuse. The app extracts the worksheet's questions; it does not answer them or analyze the student dataset.

### How to measure accuracy reliably

For a reproducible comparison, save the OCR text from this exact worksheet image and manually transcribe a reference. Compare both using a stated whitespace and punctuation normalization policy, then calculate character error rate (CER) and word error rate (WER). Lower values indicate fewer transcription errors. Evaluate layout separately from text accuracy.

No accuracy percentage is claimed here because the screenshots alone do not provide a verified, character-level transcription comparison.

## Current limitations

- The browser output is plain recognized text, without paragraph or nested-list reconstruction.
- The app has no explicit upload size limit, server-side file-type validation, or custom handling for OCR failures.
- Orientation correction and document unwarping are disabled, so rotated or distorted documents are not corrected by those stages.
- `app.py` starts Flask's development server for local testing.
