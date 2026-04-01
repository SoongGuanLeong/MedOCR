from helper import extract_text

files = [
    "E:/Desktop/medical_report_ocr/docs/1.jpg",
    "E:/Desktop/medical_report_ocr/docs/2.jpg",
    "E:/Desktop/medical_report_ocr/docs/3.jpg",
    "E:/Desktop/medical_report_ocr/docs/4.jpg",
]

for file in files:
    print(f"\n--- Checking: {file} ---")

    data = extract_text(file)

    if not data:
        print("No text detected")
        continue

    for line in data:
        text = line[1][0]
        conf = line[1][1]
        print(f"{text} | Confidence: {conf:.2f}")
