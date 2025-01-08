# Tests unitaires
# Test 1: Vérifier si l'API racine répond avec un statut 200
def test_home_status_code():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

# Test 2: Vérifier si le message de l'API racine est correct
def test_home_message():
    with app.test_client() as client:
        response = client.get('/')
        assert response.json == {'message': 'API is working!'}

# Test 3: Vérifier qu'une route inexistante retourne un statut 404
def test_404_error():
    with app.test_client() as client:
        response = client.get('/nonexistent')
        assert response.status_code == 404


# Tests d'intégration
import io
import os
from app.backend import app

def test_home():
    """Test de la route racine (/)"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {'message': 'API is working!'}

def test_collection_points():
    """Test de la route /collection-points"""
    with app.test_client() as client:
        response = client.get('/collection-points')
        assert response.status_code == 200
        data = response.json
        assert isinstance(data, list)  # Vérifie que la réponse est une liste
        assert len(data) == 3  # Vérifie qu'il y a 3 points de collecte
        for point in data:
            assert "type" in point
            assert "latitude" in point
            assert "longitude" in point

def test_predict_with_image(mocker):
    """Test de la route /predict avec une image"""
    # Mock de la fonction process_photo pour éviter un traitement réel
    mocker.patch('Photo.process_photo', return_value='uploaded_images/annotated_image.jpg')

    with app.test_client() as client:
        # Simule un fichier image
        img_data = io.BytesIO(b"fake image data")
        img_data.name = 'test.jpg'

        # Envoie une requête POST avec une image
        response = client.post(
            '/predict',
            data={'image': (img_data, 'test.jpg')},
            content_type='multipart/form-data'
        )

        # Vérifie la réponse
        assert response.status_code == 200
        assert response.content_type == 'image/jpeg'

        # Vérifie que le fichier a été sauvegardé
        saved_path = os.path.join('uploaded_images', 'test.jpg')
        assert os.path.exists(saved_path)

        # Nettoyage du fichier après le test
        if os.path.exists(saved_path):
            os.remove(saved_path)
