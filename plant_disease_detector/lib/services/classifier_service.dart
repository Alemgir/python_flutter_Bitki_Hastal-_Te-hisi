import 'dart:io';
import 'package:flutter/services.dart';
import 'package:image/image.dart' as img;
import 'package:tflite_flutter/tflite_flutter.dart';
import '../models/disease_info.dart';
import 'dart:convert';

class PlantDiseaseClassifier {
  Interpreter? _interpreter;
  DiseaseDatabase? _diseaseDatabase;

  static const int INPUT_SIZE = 128;
  static const int NUM_CLASSES = 23;

  // Singleton pattern
  static final PlantDiseaseClassifier _instance =
      PlantDiseaseClassifier._internal();
  factory PlantDiseaseClassifier() => _instance;
  PlantDiseaseClassifier._internal();

  Future<void> loadModel() async {
    try {
      // Load TFLite model
      _interpreter = await Interpreter.fromAsset(
        'assets/bitki_hastalik_modeli.tflite',
      );
      print('✓ Model yüklendi');

      // Load disease info JSON
      final jsonString = await rootBundle.loadString(
        'assets/disease_info.json',
      );
      final jsonData = json.decode(jsonString);
      _diseaseDatabase = DiseaseDatabase.fromJson(jsonData);
      print(
        '✓ Hastalık bilgileri yüklendi: ${_diseaseDatabase!.classes.length} sınıf',
      );
    } catch (e) {
      print('❌ Model yükleme hatası: $e');
      rethrow;
    }
  }

  Future<Map<String, dynamic>> classifyImage(File imageFile) async {
    if (_interpreter == null || _diseaseDatabase == null) {
      await loadModel();
    }

    try {
      // Read and decode image
      final imageBytes = await imageFile.readAsBytes();
      img.Image? image = img.decodeImage(imageBytes);

      if (image == null) {
        throw Exception('Görüntü okunamadı');
      }

      // Resize image to 128x128
      img.Image resizedImage = img.copyResize(
        image,
        width: INPUT_SIZE,
        height: INPUT_SIZE,
      );

      // Normalize pixel values to [0, 1] and create input tensor
      var input = _preprocessImage(resizedImage);

      // Prepare output tensor
      var output = List.filled(1 * NUM_CLASSES, 0.0).reshape([1, NUM_CLASSES]);

      // Run inference
      _interpreter!.run(input, output);

      // Get predictions
      List<double> predictions = output[0].cast<double>();

      // Find class with highest probability
      int maxIndex = 0;
      double maxProb = predictions[0];
      for (int i = 1; i < predictions.length; i++) {
        if (predictions[i] > maxProb) {
          maxProb = predictions[i];
          maxIndex = i;
        }
      }

      // Get disease info
      DiseaseInfo? diseaseInfo = _diseaseDatabase!.getById(maxIndex);

      if (diseaseInfo == null) {
        throw Exception('Sınıf bilgisi bulunamadı');
      }

      // Check if it's a supported plant
      if (!diseaseInfo.isSupportedPlant) {
        return {
          'success': false,
          'message': 'unsupported_plant',
          'confidence': maxProb,
        };
      }

      return {
        'success': true,
        'diseaseInfo': diseaseInfo,
        'confidence': maxProb,
        'classIndex': maxIndex,
      };
    } catch (e) {
      print('❌ Sınıflandırma hatası: $e');
      return {'success': false, 'message': 'error', 'error': e.toString()};
    }
  }

  List<List<List<List<double>>>> _preprocessImage(img.Image image) {
    var input = List.generate(
      1,
      (_) => List.generate(
        INPUT_SIZE,
        (_) => List.generate(INPUT_SIZE, (_) => List.filled(3, 0.0)),
      ),
    );

    for (int y = 0; y < INPUT_SIZE; y++) {
      for (int x = 0; x < INPUT_SIZE; x++) {
        var pixel = image.getPixel(x, y);
        input[0][y][x][0] = pixel.r / 255.0; // Red channel normalized
        input[0][y][x][1] = pixel.g / 255.0; // Green channel normalized
        input[0][y][x][2] = pixel.b / 255.0; // Blue channel normalized
      }
    }

    return input;
  }

  void dispose() {
    _interpreter?.close();
  }
}
