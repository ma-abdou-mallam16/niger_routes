import geopandas as gpd # type: ignore
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString # type: ignore

# Chemin vers le fichier téléchargé
shapefile_path = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'

# Charger les données géographiques
world = gpd.read_file(shapefile_path)

# Utiliser le bon nom de colonne
country_column = 'NAME_FR'

# Filtrer pour obtenir le Niger et les pays voisins
niger = world[world[country_column] == "Niger"]
neighbors = world[world.geometry.touches(niger.unary_union)]

# Définir les coordonnées des points clés
locations = {
    'Ayourou (NE)': Point(2.5, 14.8),
    'Labbezanga (ML)': Point(0.25, 14.9),
    'Bamako (ML)': Point(-7.98, 12.63),
    'Kourémalé (ML/GN)': Point(-8.43, 11.35),
    'Conakry (GN)': Point(-13.70, 9.52),
    'Kamsar (GN)': Point(-14.61, 10.67),
    'Kayes (ML)': Point(-11.44, 14.45),
    'Rosso (MR)': Point(-15.81, 16.52),
    'Nouakchott (MR)': Point(-15.98, 18.08),
    'Nioro du Sahel (ML)': Point(-9.57, 15.24),
    'Nouadhibou (MR)': Point(-17.03, 20.93),
    'Kantchari (NE)': Point(1.47, 12.8),
    'Kantchari (BF)': Point(0.47, 12.8),  # Ajouté
    'Ouagadougou (BF)': Point(-1.52, 12.37),
    'Cinkassé (TG)': Point(0.40, 10.97),
    'Lomé (TG)': Point(1.22, 6.14),
    'Makalondi (NE)': Point(1.42, 12.73),
    'Makalondi (BF)': Point(1.42, 12.73),  # Ajouté
    'Paga (GH)': Point(-1.11, 10.98),
    'Tema (GH)': Point(-0.02, 5.67),
    'Takoradi (GH)': Point(-1.75, 4.88),
    'Diffa (NE)': Point(12.62, 13.32),
    'Bol (TD)': Point(14.71, 13.46),
    'N\'Djamena (TD)': Point(15.05, 12.13),
    'Kousseri (CM)': Point(15.02, 12.08),
    'Douala (CM)': Point(9.70, 4.05),
    'Kribi (CM)': Point(9.95, 2.95),
    'Gaya (NE)': Point(3.32, 11.88),
    'Kamba (NG)': Point(4.33, 11.85),
    'Birnin Konni (NE)': Point(5.25, 13.8),
    'Illela (NG)': Point(5.29, 13.73),
    'Maradi (NE)': Point(7.10, 13.50),
    'Jibia (NG)': Point(7.13, 13.08),
    'Lagos (NG)': Point(3.38, 6.52),
    'Port Harcourt (NG)': Point(7.00, 4.75),
    'Warri (NG)': Point(5.75, 5.52),
    'Calabar (NG)': Point(8.32, 4.97),
    'Madama (NE)': Point(12.72, 21.96),
    'Tumu (LY)': Point(13.20, 22.82),
    'Benghazi (LY)': Point(20.06, 32.12),
    'Assamaka (NE)': Point(5.40, 20.2),
    'Tamanrasset (DZ)': Point(5.53, 22.78),
    'Oran (DZ)': Point(-0.64, 35.69),
}

# Définir les trajets avec les distances
routes = [
    (['Ayourou (NE)', 'Labbezanga (ML)', 'Bamako (ML)', 'Kourémalé (ML/GN)', 'Conakry (GN)'], [10, 460, 130, 600], 'Port de Conakry (GN)'),
    (['Ayourou (NE)', 'Labbezanga (ML)', 'Bamako (ML)', 'Kourémalé (ML/GN)', 'Kamsar (GN)'], [10, 460, 130, 540], 'Port de Kamsar (GN)'),
    (['Ayourou (NE)', 'Labbezanga (ML)', 'Bamako (ML)', 'Kayes (ML)', 'Rosso (MR)', 'Nouakchott (MR)'], [10, 460, 500, 300, 200], 'Port de Nouakchott (MR)'),
    (['Ayourou (NE)', 'Labbezanga (ML)', 'Bamako (ML)', 'Kayes (ML)', 'Nioro du Sahel (ML)', 'Nouadhibou (MR)'], [10, 460, 500, 160, 750], 'Port de Nouadhibou (MR)'),
    (['Kantchari (NE)', 'Kantchari (BF)', 'Ouagadougou (BF)', 'Cinkassé (TG)', 'Lomé (TG)'], [10, 250, 200, 600], 'Port de Lomé (TG)'),
    (['Makalondi (NE)', 'Makalondi (BF)', 'Ouagadougou (BF)', 'Cinkassé (TG)', 'Lomé (TG)'], [10, 100, 200, 600], 'Port de Lomé (TG) via Makalondi'),
    (['Kantchari (NE)', 'Kantchari (BF)', 'Ouagadougou (BF)', 'Paga (GH)', 'Tema (GH)'], [10, 250, 170, 750], 'Port de Tema (GH)'),
    (['Kantchari (NE)', 'Kantchari (BF)', 'Ouagadougou (BF)', 'Paga (GH)', 'Takoradi (GH)'], [10, 250, 170, 850], 'Port de Takoradi (GH)'),
    (['Diffa (NE)', 'Bol (TD)', 'N\'Djamena (TD)', 'Kousseri (CM)', 'Douala (CM)'], [150, 260, 5, 1400], 'Port de Douala (CM)'),
    (['Diffa (NE)', 'Bol (TD)', 'N\'Djamena (TD)', 'Kousseri (CM)', 'Kribi (CM)'], [150, 260, 5, 1600], 'Port de Kribi (CM)'),
    (['Gaya (NE)', 'Kamba (NG)', 'Lagos (NG)'], [900], 'Port de Lagos (NG)'),
    (['Birnin Konni (NE)', 'Illela (NG)', 'Lagos (NG)'], [1000], 'Port de Lagos (NG)'),
    (['Maradi (NE)', 'Jibia (NG)', 'Lagos (NG)'], [60, 830], 'Port de Lagos (NG) from Maradi'),
    (['Madama (NE)', 'Tumu (LY)', 'Benghazi (LY)'], [100, 1200], 'Port de Benghazi (LY)'),
    (['Assamaka (NE)', 'Tamanrasset (DZ)', 'Oran (DZ)'], [420, 1500], 'Port d\'Oran (DZ)'),
]

# Créer une GeoDataFrame pour les points et les lignes
points = gpd.GeoDataFrame(geometry=[locations[name] for name in locations])
lines = []
for route, distances, description in routes:
    points_in_route = [locations[point] for point in route]
    line = LineString(points_in_route)
    lines.append(line)
lines_gdf = gpd.GeoDataFrame(geometry=lines)

# Tracer la carte
fig, ax = plt.subplots(1, 1, figsize=(35, 30))
# Définir les limites de la carte pour zoomer sur le Niger et les pays voisins
minx, miny, maxx, maxy = -30, 0, 35, 37
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)

world.boundary.plot(ax=ax, linewidth=1)
niger.plot(ax=ax, color='orange')
neighbors.plot(ax=ax, color='lightgreen')

# Tracer les points et les lignes
points.plot(ax=ax, color='blue')
lines_gdf.plot(ax=ax, color='red', linestyle='--')

# Annoter les points et les distances
for route, distances, description in routes:
    points_in_route = [locations[point] for point in route]
    for i in range(len(points_in_route) - 1):
        if i < len(distances): # <--- Ligne ajoutée pour vérifier l'index
            mid_x = (points_in_route[i].x + points_in_route[i + 1].x) / 2
            mid_y = (points_in_route[i].y + points_in_route[i + 1].y) / 2
            ax.text(mid_x, mid_y, f"{distances[i]} km", fontsize=9, ha='center')

# Ajouter les étiquettes pour les points
for name, point in locations.items():
    mx, my = point.x, point.y
    ax.plot(mx, my, marker='o', color='blue')
    ax.text(mx, my, name, fontsize=9, ha='right')

# Ajouter les noms des pays voisins au centre de chaque pays
for idx, row in neighbors.iterrows():
    country_center = row['geometry'].centroid
    ax.text(country_center.x, country_center.y, row[country_column], fontsize=12, ha='center', color='black')

# Ajouter le nom du Niger au centre
niger_center = niger.geometry.centroid.iloc[0]
ax.text(niger_center.x, niger_center.y, 'Niger', fontsize=12, ha='center', color='black')

plt.suptitle('Itinéraires du Niger vers les pays et ports voisins avec distances')
plt.title('NB : Les distances sont des estimations, elles peuvent ne pas être exactes')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()