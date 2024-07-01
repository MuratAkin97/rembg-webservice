# Background Removal Web Service

This project sets up a web service to remove the background from images using the `rembg` library. The service accepts an image URL and returns the processed image with the background removed.

## Requirements

- Python 3.6+
- Flask
- rembg
- requests

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MuratAkin97/rembg-webservice.git
    cd rembg-webservice
    ```

2. Install the required Python packages:

    ```bash
    pip install rembg flask requests
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the service by navigating to:

    ```
    http://localhost:8080/remove-bg/<image-url>
    ```

    Replace `<image-url>` with the actual URL of the image you want to process. The processed image will be displayed directly on the page.


