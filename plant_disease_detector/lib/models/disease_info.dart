class DiseaseInfo {
  final int id;
  final String name;
  final String plant;
  final String disease;
  final String description;
  final List<String> symptoms;
  final List<String> treatment;
  final List<String> pesticides;

  // Türkçe çeviri map'i
  static const Map<String, String> turkishTranslations = {
    'Apple Scab': 'Elma Kaşıntısı',
    'Apple___Apple_scab': 'Elma Kaşıntısı',
    'Black Rot': 'Siyah Çürüklük',
    'Apple___Black_rot': 'Siyah Çürüklük',
    'Cedar Apple Rust': 'Sedir Elma Pas Hastalığı',
    'Apple___Cedar_apple_rust': 'Sedir Elma Pas Hastalığı',
    'Cercospora Leaf Spot': 'Cercospora Yaprak Lekesi',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
        'Cercospora Yaprak Lekesi',
    'Common Rust': 'Yaygın Pas',
    'Corn_(maize)___Common_rust': 'Yaygın Pas',
    'Northern Leaf Blight': 'Kuzey Yaprak Yanıklığı',
    'Corn_(maize)___Northern_Leaf_Blight': 'Kuzey Yaprak Yanıklığı',
    'Bacterial Spot': 'Bakteri Lekesi',
    'Pepper__bell___Bacterial_spot': 'Biber Bakteri Lekesi',
    'Early Blight': 'Erken Yanıklık',
    'Potato___Early_blight': 'Patates Erken Yanıklık',
    'Tomato_Early_blight': 'Domates Erken Yanıklık',
    'Late Blight': 'Geç Yanıklık',
    'Potato___Late_blight': 'Patates Geç Yanıklık',
    'Tomato_Late_blight': 'Domates Geç Yanıklık',
    'Target Spot': 'Hedef Lekesi',
    'Tomato__Target_Spot': 'Domates Hedef Lekesi',
    'Tomato Mosaic Virus': 'Domates Mozaik Virüsü',
    'Tomato__Tomato_mosaic_virus': 'Domates Mozaik Virüsü',
    'Yellow Leaf Curl Virus': 'Sarı Yaprak Kıvrım Virüsü',
    'Tomato__Tomato_YellowLeaf__Curl_Virus': 'Sarı Yaprak Kıvrım Virüsü',
    'Tomato Bacterial Spot': 'Domates Bakteri Lekesi',
    'Tomato_Bacterial_spot': 'Domates Bakteri Lekesi',
    'Leaf Mold': 'Yaprak Küfü',
    'Tomato_Leaf_Mold': 'Domates Yaprak Küfü',
    'Septoria Leaf Spot': 'Septoria Yaprak Lekesi',
    'Tomato_Septoria_leaf_spot': 'Septoria Yaprak Lekesi',
    'Spider Mites': 'Kırmızı Örümcek Akarı',
    'Tomato_Spider_mites_Two_spotted_spider_mite': 'Kırmızı Örümcek Akarı',
    'Healthy': 'Sağlıklı',
    'Apple___healthy': 'Elma (Sağlıklı)',
    'Corn_(maize)___healthy': 'Mısır (Sağlıklı)',
    'Pepper__bell___healthy': 'Biber (Sağlıklı)',
    'Potato___healthy': 'Patates (Sağlıklı)',
    'Tomato_healthy': 'Domates (Sağlıklı)',
  };

  DiseaseInfo({
    required this.id,
    required this.name,
    required this.plant,
    required this.disease,
    required this.description,
    required this.symptoms,
    required this.treatment,
    required this.pesticides,
  });

  factory DiseaseInfo.fromJson(Map<String, dynamic> json) {
    return DiseaseInfo(
      id: json['id'],
      name: json['name'],
      plant: json['plant'],
      disease: json['disease'],
      description: json['description'],
      symptoms: List<String>.from(json['symptoms']),
      treatment: List<String>.from(json['treatment']),
      pesticides: List<String>.from(json['pesticides']),
    );
  }

  bool get isHealthy => disease.toLowerCase() == 'healthy';

  bool get isSupportedPlant {
    final supportedPlants = ['apple', 'corn', 'pepper', 'potato', 'tomato'];
    return supportedPlants.contains(plant.toLowerCase());
  }

  // Hastalık adını Türkçeye çevir
  String get diseaseTurkish {
    return turkishTranslations[disease] ?? disease;
  }

  // Bitki adını Türkçeye çevir
  String get plantTurkish {
    final plants = {
      'apple': 'Elma',
      'corn': 'Mısır',
      'pepper': 'Biber',
      'potato': 'Patates',
      'tomato': 'Domates',
    };
    return plants[plant.toLowerCase()] ?? plant;
  }
}

class DiseaseDatabase {
  final List<DiseaseInfo> classes;

  DiseaseDatabase({required this.classes});

  factory DiseaseDatabase.fromJson(Map<String, dynamic> json) {
    return DiseaseDatabase(
      classes: (json['classes'] as List)
          .map((item) => DiseaseInfo.fromJson(item))
          .toList(),
    );
  }

  DiseaseInfo? getById(int id) {
    try {
      return classes.firstWhere((disease) => disease.id == id);
    } catch (e) {
      return null;
    }
  }
}
