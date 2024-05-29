# Image to Text Converter

This project is a web application that allows users to upload an image and convert it to text using a Python script. The application is built using Flask and provides a simple and user-friendly interface for image upload and text extraction.

## Project Structure

The project consists of the following files:

```
1.py
app.py
templates/index.html
static/css/styles.css
static/js/scripts.js
requirements.txt
README.md
```

### File Descriptions

- **1.py**: The main processing file for the application. It takes an image as input and outputs text. You need to add your image processing and text extraction code here.
- **app.py**: The Flask application that handles file uploads and calls the `1.py` script to process the image.
- **templates/index.html**: The HTML template for the main page of the application.
- **static/css/styles.css**: The CSS file for styling the application.
- **static/js/scripts.js**: The JavaScript file for client-side validation and interactions.
- **requirements.txt**: The list of Python dependencies required for the project.
- **README.md**: This file, which provides an overview and instructions for the project.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/1sh1ro/detect-system.git
    cd detect-system
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Run the Flask application**:
    ```sh
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to access the application.

### Usage

1. **Upload an image**: On the main page, click the "Choose File" button to select an image file from your computer.
2. **Convert the image**: Click the "Convert" button to upload the image and process it. The extracted text will be displayed on the result page.

### Customizing the Image Processing

- Open the `1.py` file and add your image processing and text extraction code in the `process_image` function. This function should take the path to the uploaded image as input and return the extracted text.

```python
# 1.py
def process_image(image_path):
    # Add your image processing and text extraction code here
    return "Processed text from the image"
```

### Example

Here is an example of how you might modify the `process_image` function to use an OCR library like Tesseract:

```python
# 1.py
import pytesseract
from PIL import Image

def process_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    return text
```

### Dependencies

The project requires the following Python packages:

- Flask==2.0.1
- Werkzeug==2.0.1

You can install these dependencies using the `requirements.txt` file provided.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

Feel free to contribute to this project by submitting issues or pull requests.
