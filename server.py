from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io
import os # <-- Import the 'os' module

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS to allow frontend to communicate with the backend
CORS(app)

@app.route('/api/remove-background', methods=['POST'])
def remove_background_api():
    # ... (rest of your code is perfect, no changes needed here)
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    allowed_extensions = {'png', 'jpg', 'jpeg', 'webp'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({"error": "Invalid file type. Please upload a PNG, JPG, JPEG, or WEBP image."}), 400
    try:
        input_image_bytes = file.read()
        output_image_bytes = remove(input_image_bytes)
        output_buffer = io.BytesIO(output_image_bytes)
        output_buffer.seek(0)
        return send_file(
            output_buffer,
            mimetype='image/png',
            as_attachment=True,
            download_name='background_removed.png'
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred during image processing."}), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5001 for local development
    port = int(os.environ.get('PORT', 5001))
    # Run the app
    app.run(host='0.0.0.0', port=port, debug=True)
