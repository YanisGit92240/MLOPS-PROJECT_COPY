# Étape 1 : Construire l'application avec Node.js
FROM node:18 AS build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers package.json et package-lock.json pour installer les dépendances
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier tout le projet dans le conteneur
COPY . .

# Construire le projet pour la production
RUN npm run build

# Étape 2 : Utiliser une image légère pour servir les fichiers
FROM nginx:alpine AS serve

# Copier le dossier `dist` généré dans l'étape précédente vers le dossier par défaut de Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Exposer le port 80 (par défaut pour Nginx)
EXPOSE 80

# Commande pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
