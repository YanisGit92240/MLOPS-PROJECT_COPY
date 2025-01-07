# Étape 1 : Utiliser une image Node.js pour la construction
FROM node:18 AS build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers package.json et package-lock.json pour installer les dépendances
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier tous les fichiers du projet dans le container
COPY . .

# Construire le frontend pour la production
RUN npm run build

# Étape 2 : Utiliser une image plus légère pour servir les fichiers statiques
FROM node:18 AS serve

# Installer `serve` pour servir les fichiers
RUN npm install -g serve

# Définir le répertoire de travail
WORKDIR /app

# Copier le dossier `dist` généré dans l'étape précédente
COPY --from=build /app/dist ./dist

# Exposer le port 80 pour servir le frontend
EXPOSE 80

# Commande pour démarrer le serveur
CMD ["serve", "-s", "dist", "-l", "3000"]

