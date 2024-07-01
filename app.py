from flask import Flask, request, render_template_string
from rembg import remove
from io import BytesIO
import requests
import base64

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

    # Convert the output bytes to a base64 string to display in HTML
    output_base64 = base64.b64encode(output_bytes).decode('utf-8')
    img_tag = f'<img src="data:image/png;base64,{output_base64}"/>'

    return render_template_string(f"""
        <html>
        <body>
            <h1>Background Removed Image</h1>
            {img_tag}
        </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
