from paddleocr import PaddleOCR

# Initialize once
ocr = PaddleOCR(use_angle_cls=True, lang="en")


def extract_text(image_path: str):
    result = ocr.ocr(image_path, cls=True)

    if not result or result[0] is None:
        return []

    return result[0]
