from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
import cv2
from skimage.metrics import structural_similarity
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Set up upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to detect tampering using SSIM
def is_fraudulent_pan(uploaded_path):
    # Load the uploaded image
    uploaded = cv2.imread(uploaded_path)

    # Assuming a reference image is available in the uploads folder
    reference_path = os.path.join(app.config['UPLOAD_FOLDER'], 'reference_pan_card.png')
    if not os.path.exists(reference_path):
        raise FileNotFoundError("Reference PAN card image not found.")

    reference = cv2.imread(reference_path)

    # Convert to grayscale
    uploaded_gray = cv2.cvtColor(uploaded, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)

    # Compute SSIM
    (score, _) = structural_similarity(reference_gray, uploaded_gray, full=True)

    # Return result based on SSIM score
    return score > 0.75

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Detect tampering
            result = is_fraudulent_pan(filepath)
            os.remove(filepath)  # Clean up uploaded file

            if result:
                return jsonify({'tampered': True, 'message': 'The PAN card is most likely tampered.'})
            else:
                return jsonify({'tampered': False, 'message': 'The PAN card is not tampered.'})
        except FileNotFoundError as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
