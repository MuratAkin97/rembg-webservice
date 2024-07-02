from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
import requests

app = Flask(__name__)

@app.route('/remove-bg/<path:image_url>')
def remove_bg(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error fetching the image: {e}", 400

    input_bytes = response.content
    output_bytes = remove(input_bytes)

    # Determine the image format from the input URL
    image_format = image_url.split('.')[-1].lower()
    if image_format not in ['png', 'jpeg', 'jpg']:
        image_format = 'png'  # Default to PNG if the format is unknown

    return send_file(
        BytesIO(output_bytes),
        mimetype='image/png',
        as_attachment=False,
        download_name=f'removed-bg.{image_format}'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
