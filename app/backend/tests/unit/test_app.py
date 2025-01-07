import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from app.backend.app import app

from app import app

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
