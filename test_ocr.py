from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    enable_mkldnn=False,
)

results = ocr.predict("receipt.jpg")

for result in results:
    result.print()
    result.save_to_img("output")
    result.save_to_json("output")