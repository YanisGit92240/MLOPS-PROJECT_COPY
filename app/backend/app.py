from flask import Flask, jsonify, request, send_file
from Photo import process_photo  # Fonction pour traiter les photos
from werkzeug.utils import secure_filename
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dossier temporaire pour sauvegarder les images
UPLOAD_FOLDER = 'uploaded_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return jsonify({'message': 'API is working!'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400

        image = request.files['image']
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

        # Traitement de l'image (renvoie une image annotée)
        annotated_image_path = process_photo(image_path)  # Retourne le chemin de l'image annotée

        return send_file(annotated_image_path, mimetype='image/jpeg')  # Retourne l'image
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/collection-points', methods=['GET'])
def collection_points():
    points = [
        {"type": "Colonnes enterées", "latitude": 48.9160, "longitude": 2.2500},
        {"type": "Déchetterie", "latitude": 48.9250, "longitude": 2.2540},
        {"type": "Benne tri jaune", "latitude": 48.9205, "longitude": 2.2515},
    ]
    return jsonify(points)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
