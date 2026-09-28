import json
import tempfile
from pathlib import Path

from flask import Flask, render_template, request
from paddleocr import PaddleOCR

app = Flask(__name__)

ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    enable_mkldnn=False,
)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    uploaded_file = request.files.get("image")

    if not uploaded_file or not uploaded_file.filename:
        return render_template("index.html", error="Please choose an image.")

    with tempfile.TemporaryDirectory() as folder:
        image_path = Path(folder) / "receipt.jpg"
        uploaded_file.save(image_path)

        results = ocr.predict(str(image_path))

        lines = []
        for result in results:
            json_path = Path(folder) / "result.json"
            result.save_to_json(str(json_path))

            data = json.loads(json_path.read_text(encoding="utf-8"))
            ocr_data = data.get("res", data)
            lines.extend(ocr_data.get("rec_texts", []))

    return render_template("index.html", lines=lines)


if __name__ == "__main__":
    app.run(debug=False)