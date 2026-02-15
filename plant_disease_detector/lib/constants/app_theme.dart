import 'package:flutter/material.dart';

class AppColors {
  // Primary green shades
  static const Color primaryGreen = Color(0xFF2E7D32);
  static const Color primaryGreenDark = Color(0xFF1B5E20);
  static const Color primaryGreenLight = Color(0xFF4CAF50);

  // Accent colors
  static const Color accentOrange = Color(0xFFFF6F00);
  static const Color accentYellow = Color(0xFFFFC107);

  // Background colors
  static const Color backgroundLight = Color(0xFFF1F8E9);
  static const Color cardBackground = Colors.white;

  // Text colors
  static const Color textPrimary = Color(0xFF212121);
  static const Color textSecondary = Color(0xFF757575);

  // Status colors
  static const Color healthy = Color(0xFF4CAF50);
  static const Color diseased = Color(0xFFE53935);
  static const Color warning = Color(0xFFFFA726);

  // Gradient colors
  static const List<Color> primaryGradient = [primaryGreen, primaryGreenLight];

  static const List<Color> accentGradient = [accentOrange, accentYellow];
}

class AppTheme {
  static ThemeData lightTheme = ThemeData(
    primaryColor: AppColors.primaryGreen,
    scaffoldBackgroundColor: AppColors.backgroundLight,
    colorScheme: ColorScheme.light(
      primary: AppColors.primaryGreen,
      secondary: AppColors.accentOrange,
      surface: AppColors.cardBackground,
      error: AppColors.diseased,
    ),
    appBarTheme: AppBarTheme(
      backgroundColor: AppColors.primaryGreen,
      elevation: 0,
      centerTitle: true,
      iconTheme: IconThemeData(color: Colors.white),
      titleTextStyle: TextStyle(
        color: Colors.white,
        fontSize: 20,
        fontWeight: FontWeight.bold,
      ),
    ),
    cardTheme: CardThemeData(
      color: AppColors.cardBackground,
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.primaryGreen,
        foregroundColor: Colors.white,
        padding: EdgeInsets.symmetric(horizontal: 32, vertical: 16),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        elevation: 4,
      ),
    ),
    floatingActionButtonTheme: FloatingActionButtonThemeData(
      backgroundColor: AppColors.primaryGreen,
      foregroundColor: Colors.white,
    ),
    iconTheme: IconThemeData(color: AppColors.primaryGreen),
  );
}
