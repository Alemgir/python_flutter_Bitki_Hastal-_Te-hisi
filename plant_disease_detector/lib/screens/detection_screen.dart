import 'dart:io';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:image_picker/image_picker.dart';
import '../constants/app_theme.dart';
import '../services/classifier_service.dart';
import 'result_screen.dart';

class DetectionScreen extends StatefulWidget {
  const DetectionScreen({Key? key}) : super(key: key);

  @override
  State<DetectionScreen> createState() => _DetectionScreenState();
}

class _DetectionScreenState extends State<DetectionScreen> {
  File? _selectedImage;
  bool _isProcessing = false;
  final PlantDiseaseClassifier _classifier = PlantDiseaseClassifier();

  @override
  void initState() {
    super.initState();
    _loadModel();
  }

  Future<void> _loadModel() async {
    try {
      await _classifier.loadModel();
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Model yüklenirken hata oluştu: $e'),
            backgroundColor: Colors.red,
          ),
        );
      }
    }
  }

  Future<void> _pickImage(ImageSource source) async {
    try {
      final ImagePicker picker = ImagePicker();
      final XFile? image = await picker.pickImage(
        source: source,
        maxWidth: 800,
        maxHeight: 800,
        imageQuality: 85,
      );

      if (image != null) {
        setState(() {
          _selectedImage = File(image.path);
        });
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Görüntü seçilirken hata oluştu: $e'),
            backgroundColor: Colors.red,
          ),
        );
      }
    }
  }

  Future<void> _analyzeImage() async {
    if (_selectedImage == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Lütfen önce bir görüntü seçin!'),
          backgroundColor: Colors.orange,
        ),
      );
      return;
    }

    setState(() {
      _isProcessing = true;
    });

    try {
      final result = await _classifier.classifyImage(_selectedImage!);

      setState(() {
        _isProcessing = false;
      });

      if (!mounted) return;

      if (result['success'] == true) {
        // Navigate to result screen
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ResultScreen(
              image: _selectedImage!,
              diseaseInfo: result['diseaseInfo'],
              confidence: result['confidence'],
            ),
          ),
        );
      } else if (result['message'] == 'unsupported_plant') {
        _showUnsupportedPlantDialog(result['confidence']);
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              'Analiz sırasında hata oluştu: ${result['error'] ?? 'Bilinmeyen hata'}',
            ),
            backgroundColor: Colors.red,
          ),
        );
      }
    } catch (e) {
      setState(() {
        _isProcessing = false;
      });

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Analiz hatası: $e'),
            backgroundColor: Colors.red,
          ),
        );
      }
    }
  }

  void _showUnsupportedPlantDialog(double confidence) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: Row(
          children: [
            Icon(Icons.info_outline, color: AppColors.warning, size: 32),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                'Üzgünüz! 🌿',
                style: GoogleFonts.poppins(
                  fontWeight: FontWeight.bold,
                  fontSize: 20,
                ),
              ),
            ),
          ],
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Bu görüntü desteklenen bitki yapraklarından birine ait görünmüyor.',
              style: GoogleFonts.poppins(fontSize: 15, height: 1.5),
            ),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: AppColors.backgroundLight,
                borderRadius: BorderRadius.circular(12),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Desteklenen Bitkiler:',
                    style: GoogleFonts.poppins(
                      fontWeight: FontWeight.bold,
                      fontSize: 14,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🍎 Elma\n🌽 Mısır\n🌶️ Biber\n🥔 Patates\n🍅 Domates',
                    style: GoogleFonts.poppins(fontSize: 14, height: 1.6),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),
            Text(
              'Lütfen yukarıdaki bitkilerden birinin yaprak fotoğrafını çekmeyi deneyin. 📸',
              style: GoogleFonts.poppins(
                fontSize: 13,
                color: AppColors.textSecondary,
                fontStyle: FontStyle.italic,
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text(
              'Tamam',
              style: GoogleFonts.poppins(
                fontWeight: FontWeight.bold,
                color: AppColors.primaryGreen,
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(context);
              _pickImage(ImageSource.camera);
            },
            child: Text(
              'Yeni Fotoğraf Çek',
              style: GoogleFonts.poppins(fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Hastalık Tespiti',
          style: GoogleFonts.poppins(fontWeight: FontWeight.bold),
        ),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [AppColors.backgroundLight, Colors.white],
          ),
        ),
        child: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Image Preview Area
                Card(
                  elevation: 8,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Container(
                    height: 350,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(20),
                      color: AppColors.backgroundLight,
                    ),
                    child: _selectedImage == null
                        ? Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(
                                Icons.add_photo_alternate,
                                size: 80,
                                color: AppColors.primaryGreen.withOpacity(0.5),
                              ),
                              const SizedBox(height: 16),
                              Text(
                                'Fotoğraf Seç veya Çek',
                                style: GoogleFonts.poppins(
                                  fontSize: 18,
                                  color: AppColors.textSecondary,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ],
                          )
                        : ClipRRect(
                            borderRadius: BorderRadius.circular(20),
                            child: Image.file(
                              _selectedImage!,
                              fit: BoxFit.cover,
                            ),
                          ),
                  ),
                ),

                const SizedBox(height: 30),

                // Action Buttons
                Row(
                  children: [
                    Expanded(
                      child: _buildAnimatedButton(
                        onPressed: _isProcessing
                            ? null
                            : () => _pickImage(ImageSource.camera),
                        icon: Icons.camera_alt,
                        label: 'Kamera',
                        backgroundColor: Colors.blue,
                        isEnabled: !_isProcessing,
                      ),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: _buildAnimatedButton(
                        onPressed: _isProcessing
                            ? null
                            : () => _pickImage(ImageSource.gallery),
                        icon: Icons.photo_library,
                        label: 'Galeri',
                        backgroundColor: AppColors.accentOrange,
                        isEnabled: !_isProcessing,
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 24),

                // Analyze Button
                SizedBox(
                  height: 60,
                  child: _buildAnimatedButton(
                    onPressed: _isProcessing ? null : _analyzeImage,
                    icon: _isProcessing
                        ? Icons.hourglass_bottom
                        : Icons.science,
                    label: _isProcessing ? 'Analiz Ediliyor...' : 'Analiz Et',
                    backgroundColor: AppColors.primaryGreenDark,
                    isEnabled: !_isProcessing,
                    isLarge: true,
                  ),
                ),

                const SizedBox(height: 24),

                // Info Card
                Card(
                  elevation: 4,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(20.0),
                    child: Column(
                      children: [
                        Icon(
                          Icons.lightbulb_outline,
                          color: AppColors.accentYellow,
                          size: 32,
                        ),
                        const SizedBox(height: 12),
                        Text(
                          'İpucu',
                          style: GoogleFonts.poppins(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                            color: AppColors.textPrimary,
                          ),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          'En iyi sonuçlar için:\n'
                          '• Yaprağın tamamını çekin\n'
                          '• Parlak ışıkta çekim yapın\n'
                          '• Net ve bulanık olmayan fotoğraf çekin',
                          textAlign: TextAlign.center,
                          style: GoogleFonts.poppins(
                            fontSize: 13,
                            color: AppColors.textSecondary,
                            height: 1.5,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // Animated button wrapper
  Widget _buildAnimatedButton({
    required VoidCallback? onPressed,
    required IconData icon,
    required String label,
    required Color backgroundColor,
    required bool isEnabled,
    bool isLarge = false,
  }) {
    return GestureDetector(
      onTap: isEnabled ? onPressed : null,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 150),
        curve: Curves.easeOut,
        transform: Matrix4.identity()..scale(isEnabled ? 1.0 : 0.95),
        child: ElevatedButton.icon(
          onPressed: isEnabled ? onPressed : null,
          icon: Icon(icon, size: isLarge ? 28 : 24),
          label: Text(
            label,
            style: GoogleFonts.poppins(
              fontSize: isLarge ? 18 : 16,
              fontWeight: FontWeight.bold,
            ),
          ),
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor,
            disabledBackgroundColor: backgroundColor.withOpacity(0.5),
            padding: EdgeInsets.symmetric(
              vertical: isLarge ? 20 : 16,
              horizontal: 12,
            ),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(isLarge ? 16 : 12),
            ),
            elevation: 6,
            shadowColor: backgroundColor.withOpacity(0.6),
          ),
        ),
      ),
    );
  }
}
