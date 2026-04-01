# Motivation
I got a copy of my mom's blood and urine test and wanted to see how [paddleOCR](https://github.com/PADDLEPADDLE/PADDLEOCR) works.
I redacted any personally identifiable information (PII) from the report before running it through the OCR.
This project is also a chance to get hands-on experience with:
- UV package manager
- Nvidia CUDA
- Nvidia cuDNN

> **Note:** 
> Most of the code snippets in this report are vibe-coded.
> This project is not for medical diagnosis, only OCR demonstration.

# Prerequisites
- [UV package manager](https://docs.astral.sh/uv/getting-started/installation/) (skip this if you're already familiar with it)
  1. Clean up existing UV installations:
    ```powershell
    uv cache clean
    uv python uninstall --all
    ```
  2. Set these environment variables to force UV to use external disk and save space:
    - ```UV_CACHE_DIR=E:\uv\cache```
    - ```UV_PYTHON_INSTALL_DIR=E:\uv\python```
    - ```UV_TOOL_DIR=E:\uv\tools```
    - ```UV_LINK_MODE=hardlink```
  3. Install Python versions from 3.08 to 3.14:
    ```powershell
    uv python install 3.08
    uv python install 3.09
    ...
    uv python install 3.14
    ```
- [Nvidia CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
- [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive) (choose the version that matches CUDA 11.8)


# Getting Started
Run the following commands in order:
```powershell
# Init project with Python 3.10
uv init --python 3.10

# Create a virtual environment
uv venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install pip if not available
curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
python "D:\Python\Tools\get-pip.py"

# Install dependencies
pip install numpy==1.26.4
pip install paddlepaddle-gpu==2.6.1.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
pip install paddleocr==2.6.1.3

# Run the Python file
cd src
python extract.py
```

# Findings/Limitations
The text output from PaddleOCR was manually reviewed to evaluate the current state-of-the-art open-source OCR performance. Some observations:
- Overall text recognition is quite good, with most content accurately identified.
- Small or blurred characters (e.g., colons ":", small letters like "e") can be misrecognized.
- Text in languages not supported by the OCR is often interpreted as unusual fonts, with confidence levels around 0.5 (normal text confidence is typically above 0.8).
- PaddleOCR does not automatically capture the layout or ordering of the text, so reconstructing complex tables or multi-column structures remains challenging. This confirms that extracting accurate information from structured documents like tables or PDFs is still difficult with off-the-shelf OCR.

## Disclaimer
This project is for educational and demonstration purposes only.
It **is not intended for medical diagnosis or treatment**.
Always consult a licensed healthcare professional for medical advice.
