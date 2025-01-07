# Utiliser une image Python 3.10
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR ./app

# Copier les fichiers nécessaires
COPY . ./app

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5001

# Lancer l'application
CMD ["python", "app.py"]
