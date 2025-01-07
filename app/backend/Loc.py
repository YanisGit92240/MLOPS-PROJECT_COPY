import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

# Function to add markers to the map
def add_markers(map_obj, data, marker_type):
    # Define color mapping based on the warning provided
    color_mapping = {
        'Colonnes enterées': 'gray',
        'Déchetterie': 'red',
        'Benne tri jaune': 'orange',
        'Benne tri vert': 'darkgreen',
        'Benne tri bleu': 'blue'
    }

    
    for index, row in data.iterrows():
        if row['Type'] == marker_type:
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Description'],
                # Use the color mapping
                icon=folium.Icon(color=color_mapping.get(marker_type, 'lightgray'))
            ).add_to(map_obj)

# Function to create the map
def create_map(checked_types, center_coords=None):
    if not center_coords:
        center_coords = [48.9226, 2.2530]  # Default to Colombes
    m = folium.Map(location=center_coords, zoom_start=14)

    # Dummy data for waste collection points
    data = pd.DataFrame({
        'Type': [
            'Colonnes enterées', 'Déchetterie', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', 'Déchetterie', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu',
            'Colonnes enterées', '-', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu'
        ],
        'Latitude': [
                48.9160, 48.9250, 48.9205, 48.9190, 48.9275, 
                48.9075, 48.9215, 48.9175, 48.9185, 48.9175,
                48.9270, 48.9175, 48.9260, 48.9160, 48.9280, 
                48.9165, 48.9175, 48.9205, 48.9160, 48.9265,
                48.9195, 48.9245, 48.9275, 48.9280, 48.9170, 
                48.9240, 48.9195, 48.9160, 48.9160, 48.9285,
                48.9255, 48.9290, 48.9205, 48.9180, 48.9205, 
                48.9210, 48.9225, 48.9280, 48.9220, 48.9235,
                48.9230, 48.9275, 48.9280, 48.9200, 48.9205
        ],
        'Longitude': [
                2.2500, 2.2540, 2.2515, 2.2570, 2.2490, 
                2.2510, 2.2530, 2.2570, 2.2500, 2.2490,
                2.2505, 2.2495, 2.2560, 2.2520, 2.2520, 
                2.2490, 2.2510, 2.2550, 2.2485, 2.2480,
                2.2560, 2.2570, 2.2525, 2.2520, 2.2500, 
                2.2480, 2.2540, 2.2535, 2.2570, 2.2510,
                2.2530, 2.2535, 2.2560, 2.2530, 2.2560, 
                2.2480, 2.2550, 2.2510, 2.2550, 2.2480,
                2.2575, 2.2490, 2.2525, 2.2510, 2.2555

        ],
        'Description': [
            'Colonnes enterées 1', 'Déchetterie locale 1', 'Benne tri jaune 1', 'Benne tri verre 1', 'Benne tri papier 1',
            'Colonnes enterées 2', 'Déchetterie locale 2', 'Benne tri jaune 2', 'Benne tri verre 2', 'Benne tri papier 2',
            'Colonnes enterées 3', 'Déchetterie locale 3', 'Benne tri jaune 3', 'Benne tri verre 3', 'Benne tri papier 3',
            'Colonnes enterées 4', 'Déchetterie locale 4', 'Benne tri jaune 4', 'Benne tri verre 4', 'Benne tri papier 4',
            'Colonnes enterées 5', 'Déchetterie locale 5', 'Benne tri jaune 5', 'Benne tri verre 5', 'Benne tri papier 5',
            'Colonnes enterées 6', 'Déchetterie locale 6', 'Benne tri jaune 6', 'Benne tri verre 6', 'Benne tri papier 6',
            'Colonnes enterées 7', 'Déchetterie locale 7', 'Benne tri jaune 7', 'Benne tri verre 7', 'Benne tri papier 7',
            'Colonnes enterées 8', 'Déchetterie locale 8', 'Benne tri jaune 8', 'Benne tri verre 8', 'Benne tri papier 8',
            'Colonnes enterées 9', 'Déchetterie locale 9', 'Benne tri jaune 9', 'Benne tri verre 9', 'Benne tri papier 9'
        ]
    })

    for t in checked_types:
        add_markers(m, data, t)

    return m

# Main app
def main():
    st.title("Localisation des points de collecte à proximité")

    # Filters and address input at the top
    col1, col2 = st.columns(2)

    with col1:
        benne_ordures = st.checkbox('Colonnes enterées', True)
        dechetterie = st.checkbox('Déchetteries', True)
        benne_tri_vert = st.checkbox('Benne de tri vert', True)
        
    with col2:
        benne_tri_jaune = st.checkbox('Benne de tri jaune', True)
        benne_tri_bleu = st.checkbox('Benne de tri bleu', True)
    
    # Map creation with selected filters
    checked_types = [
        t for t, checked in zip(
            ['Colonnes enterées', 'Déchetterie', 'Benne tri jaune', 'Benne tri vert', 'Benne tri bleu'],
            [benne_ordures, dechetterie, benne_tri_jaune, benne_tri_vert, benne_tri_bleu]
        ) if checked
    ]

    # Address geocoding to get coordinates (Placeholder for actual implementation)
    center_coords = None

    # Displaying the map
    map_colombes = create_map(checked_types, center_coords)
    folium_static(map_colombes)

    # Displaying the image of the collection schedule
    st.header("INFORMATIONS")
    # CSS personnalisé pour le fond et les bordures arrondies des images
    st.markdown("""
    <style>
    .image-container {
        background-color: #003366; /* Bleu foncé */
        border-radius: 10px; /* Bordures arrondies */
        padding: 10px; /* Espace autour de l'image */
        margin-bottom: 20px; /* Espace en dessous du conteneur de l'image */
    }
    </style>
                
    """, unsafe_allow_html=True)
    
    # Conteneur pour les images avec un fond bleu et des bordures arrondies
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    
    # Création des colonnes pour les images avec les tailles ajustées
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        st.image('images/collecte.png', width=700)  # Image ajustée

    with col2:
        st.image('images/collecte2.png', width=500)  # Image ajustée

    st.markdown('</div>', unsafe_allow_html=True)  # Fermeture du conteneur d'image

    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # Fermeture du conteneur d'image

    st.markdown("""
        <div style="background-color: #003366; padding: 10px; border-radius: 10px; margin-top: 25px;">
            <h2 style="color: white; text-align: center;">SERVICE PROPRETÉ</h2>
            <p style="color: white; text-align: center;">Centre technique municipal, route de l'Ancienne digue<br>
            92700 Colombes</p>
            <p style="color: white; text-align: center;">📞 0 800 892 700</p>
            <p style="text-align: center;"><a href="https://www.colombes.fr/environnement/proprete-1022.html" target="_blank" style="color: #FFD700; font-weight: bold;">CONTACTER PAR INTERNET</a></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
