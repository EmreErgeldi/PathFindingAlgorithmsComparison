import math
import random

# Veri seti
data = [
    (1, 'Türkiye', 'Adana', 36.98542, 35.32502),
    (2, 'Türkiye', 'Adıyaman', 37.762990, 38.277298),
    (3, 'Türkiye', 'Afyonkarahisar', 38.756217, 30.537846),
    (4, 'Türkiye', 'Ağrı', 39.718993, 43.047663),
    (5, 'Türkiye', 'Amasya', 40.656314, 35.837068),
    (6, 'Türkiye', 'Ankara', 39.942928, 32.860481),
    (7, 'Türkiye', 'Antalya', 36.896126, 30.713081),
    (8, 'Türkiye', 'Artvin', 41.181310, 41.820537),
    (9, 'Türkiye', 'Aydın', 37.838044, 27.845571),
    (10, 'Türkiye', 'Balıkesir', 39.644878, 27.885361),
    (11, 'Türkiye', 'Bilecik', 40.142960, 29.979159),
    (12, 'Türkiye', 'Bingöl', 38.88472, 40.496391),
    (13, 'Türkiye', 'Bitlis', 38.400664, 42.108971),
    (14, 'Türkiye', 'Bolu', 40.732006, 31.607052),
    (15, 'Türkiye', 'Burdur', 37.718293, 30.282248),
    (16, 'Türkiye', 'Bursa', 40.182816, 29.066148),
    (17, 'Türkiye', 'Çanakkale', 40.146777, 26.408220),
    (18, 'Türkiye', 'Çankırı', 40.600190, 33.616304),
    (19, 'Türkiye', 'Çorum', 40.549853, 34.953694),
    (20, 'Türkiye', 'Denizli', 37.783026, 29.096246),
    (21, 'Türkiye', 'Diyarbakır', 37.9137, 40.224899),
    (22, 'Türkiye', 'Edirne', 41.675907, 26.553608),
    (23, 'Türkiye', 'Elazığ', 38.6763, 39.221802),
    (24, 'Türkiye', 'Erzincan', 39.75, 39.5),
    (25, 'Türkiye', 'Erzurum', 39.905994, 41.273784),
    (26, 'Türkiye', 'Eskişehir', 39.766724, 30.525608),
    (27, 'Türkiye', 'Gaziantep', 37.062931, 37.378159),
    (28, 'Türkiye', 'Giresun', 40.917921, 38.389876),
    (29, 'Türkiye', 'Gümüşhane', 40.458673, 39.478961),
    (30, 'Türkiye', 'Hakkari', 37.578120, 43.73380531),
    (31, 'Türkiye', 'Hatay', 36.202621, 36.160045),
    (32, 'Türkiye', 'Isparta', 37.762627, 30.553612),
    (33, 'Türkiye', 'Mersin', 36.810307, 34.620414),
    (34, 'Türkiye', 'İstanbul', 41.046419, 29.033115),
    (35, 'Türkiye', 'İzmir', 38.423652, 27.142797),
    (36, 'Türkiye', 'Kars', 40.601469, 43.097496),
    (37, 'Türkiye', 'Kastamonu', 41.378133, 33.776539),
    (38, 'Türkiye', 'Kayseri', 38.722100, 35.489122),
    (39, 'Türkiye', 'Kırklareli', 41.735547, 27.224502),
    (40, 'Türkiye', 'Kırşehir', 39.146209, 34.160577),
    (41, 'Türkiye', 'Kocaeli', 40.765600, 29.940659),
    (42, 'Türkiye', 'Konya', 37.872817, 32.491991),
    (43, 'Türkiye', 'Kütahya', 39.419993, 29.985721),
    (44, 'Türkiye', 'Malatya', 38.355390, 38.333476),
    (45, 'Türkiye', 'Manisa', 38.614027, 27.429533),
    (46, 'Türkiye', 'Kahramanmaraş', 37.582047, 36.926934),
    (47, 'Türkiye', 'Mardin', 37.313051, 40.732555),
    (48, 'Türkiye', 'Muğla', 37.215266, 28.363718),
    (49, 'Türkiye', 'Muş', 38.732415, 41.489878),
    (50, 'Türkiye', 'Nevşehir', 38.623861, 34.712756),
    (51, 'Türkiye', 'Niğde', 37.969110, 34.678619),
    (52, 'Türkiye', 'Ordu', 40.985592, 37.879123),
    (53, 'Türkiye', 'Rize', 41.025113, 40.516397),
    (54, 'Türkiye', 'Sakarya', 40.773626, 30.403235),
    (55, 'Türkiye', 'Samsun', 41.28157, 36.33812),
    (56, 'Türkiye', 'Siirt', 37.927462, 41.942270),
    (57, 'Türkiye', 'Sinop', 42.026596, 35.151245),
    (58, 'Türkiye', 'Sivas', 39.750528, 37.015028),
    (59, 'Türkiye', 'Tekirdağ', 40.978127, 27.511091),
    (60, 'Türkiye', 'Tokat', 40.323397, 36.55214961),
    (61, 'Türkiye', 'Trabzon', 41.001289, 39.716549),
    (62, 'Türkiye', 'Tunceli', 39.108101, 39.548199),
    (63, 'Türkiye', 'Şanlıurfa', 37.1586, 38.797901),
    (64, 'Türkiye', 'Uşak', 38.678883, 29.404976),
    (65, 'Türkiye', 'Van', 38.501287, 43.372931),
    (66, 'Türkiye', 'Yozgat', 39.820954, 34.808617),
    (67, 'Türkiye', 'Zonguldak', 41.452650, 31.790032),
    (68, 'Türkiye', 'Aksaray', 38.370386, 34.026986),
    (69, 'Türkiye', 'Bayburt', 40.250858, 40.202831),
    (70, 'Türkiye', 'Karaman', 37.181200, 33.222315),
    (71, 'Türkiye', 'Kırıkkale', 39.849998, 33.5),
    (72, 'Türkiye', 'Batman', 37.882999, 41.130901),
    (73, 'Türkiye', 'Şırnak', 37.522781, 42.459438),
    (74, 'Türkiye', 'Bartın', 41.633178, 32.338396),
    (75, 'Türkiye', 'Ardahan', 41.112875, 42.702389),
    (76, 'Türkiye', 'Iğdır', 39.895802, 44.040821),
    (77, 'Türkiye', 'Yalova', 40.657659, 29.268905),
    (78, 'Türkiye', 'Karabük', 41.200069, 32.629601),
    (79, 'Türkiye', 'Kilis', 36.717999, 37.116901),
    (80, 'Türkiye', 'Osmaniye', 37.074695, 36.246347),
    (81, 'Türkiye', 'Düzce', 40.839377, 31.159454)
]

# İlleri temsil eden sözlük
cities = {row[2]: {'id': row[0], 'lat': row[3], 'lon': row[4], 'neighbors': []} for row in data}


# Gerçek uzaklık hesaplama fonksiyonu
def calculate_distance(lat1, lon1, lat2, lon2):
    radius = 6371  # Dünya yarıçapı (km)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(
        math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c


# Uzaklık ve komşuluk bilgilerini oluştur
for city1_name, city1 in cities.items():
    for city2_name, city2 in cities.items():
        if city1_name != city2_name:
            distance = calculate_distance(city1['lat'], city1['lon'], city2['lat'], city2['lon'])
            # Uzaklığı 1.1 ile 1.5 arasında rastgele bir değerle çarp
            multiplied_distance = distance * random.uniform(1.1, 1.5)
            cities[city1_name]['neighbors'].append({
                'id': city2['id'],
                'distance': multiplied_distance,
                'lat': city2['lat'],
                'lon': city2['lon']
            })

# Ayrıca her ilin kendi kendine komşu olmadığını varsayalım
for city in cities.values():
    city['neighbors'] = sorted(city['neighbors'], key=lambda x: x['distance'])
    city['neighbors'] = city['neighbors'][:5]  # İlk 5 en yakın komşuyu alalım

# Dictionary array oluştur
graph = [{
    'id': city['id'],
    'name': city_name,
    'lat': city['lat'],
    'lon': city['lon'],
    'neighbors': [{
        'id': neighbor['id'],
        'distance': neighbor['distance'],
        'lat': neighbor['lat'],
        'lon': neighbor['lon']
    } for neighbor in city['neighbors']]
} for city_name, city in cities.items()]

# Oluşan data structure
print(graph)
