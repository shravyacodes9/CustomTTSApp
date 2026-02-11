# Personalized Reading Aid for Dyslexics 📖

A sophisticated Text-to-Speech application designed specifically for dyslexic readers, featuring advanced text preprocessing, customizable UI, and high-quality speech synthesis.

## 🎯 Features

### Core Functionality
- **Text Input & Upload**: Paste text directly or upload from files
- **Advanced Text Preprocessing**: Cleans and normalizes text for optimal TTS quality
- **High-Quality Text-to-Speech**: Powered by pyttsx3 engine with multiple voice options
- **Real-Time Highlighting**: Word or line-by-line highlighting during speech playback
- **Export Functionality**: Save processed text to files

### Customization Options
- **Font Selection**: Multiple font families (OpenDyslexic optimized, Arial, Sans-serif)
- **Font Size Control**: Adjustable from 12pt to 32pt
- **Spacing Control**: 
  - Word spacing (0-8 units)
  - Letter spacing (0-4 units)
- **Color Customization**:
  - Background color picker
  - Text color picker
  - Highlight color picker
- **Highlight Modes**: Switch between word-level and line-level highlighting
- **Speed Control**: Adjustable reading speed (120-250 WPM)
- **Settings Persistence**: Automatically saves your preferences

## 📋 System Requirements

- **Python**: 3.11 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 2GB minimum
- **Storage**: 500MB for dependencies

## 🚀 Installation

### Step 1: Clone or Download the Repository
```bash
git clone <repository-url>
cd CustomTTSapp
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv ttsenv
# On Windows:
ttsenv\Scripts\activate
# On macOS/Linux:
source ttsenv/bin/activate
```

### Step 3: Install Dependencies
All required libraries are pre-installed in the virtual environment. If you need to install manually:

```bash
pip install pyttsx3 nltk numpy scipy
```

## 🎮 Usage

### Running the Application

```bash
cd CustomTTSapp
ttsenv/Scripts/python.exe gui_main.py
```

### Basic Workflow

1. **Input Text**
   - Paste text using the "Paste" button
   - Or upload a `.txt` file using the "Upload File" button

2. **Preprocess**
   - Click "Preprocess" to clean and normalize the text
   - Text will appear in the "Processed & Adapted Text" box

3. **Customize**
   - Adjust font, size, spacing, and colors in the Customization panel
   - Try different highlight modes (Word/Line)
   - Set your preferred reading speed

4. **Listen**
   - Click "Play" to start text-to-speech
   - Use "Pause", "Resume", and "Stop" buttons to control playback
   - Watch the highlighted text as it's read

5. **Export**
   - Click "Export Text" to save the processed text to a file
   - Use "Save Prefs" to remember your customization settings

## 📁 Project Structure

```
CustomTTSapp/
├── gui_main.py              # Main GUI application
├── input_module.py          # File I/O handling
├── preprocessing.py         # Text cleaning & normalization
├── customization.py         # UI customization & settings
├── tts_module.py            # Text-to-speech engine wrapper
├── tts_settings.json        # User preferences (auto-created)
├── app.py                   # Additional app configuration
├── README.md                # This file
└── ttsenv/                  # Virtual environment
```

## 📚 Module Documentation

### `gui_main.py`
Main GUI application using Tkinter. Manages the user interface, handles all button clicks, and coordinates between other modules.

**Key Classes:**
- `TTSApp`: Main application class

### `input_module.py`
Handles file operations for reading and writing text files.

**Functions:**
- `upload_text_file(text_widget)`: Load text from file
- `export_text_file(text_widget)`: Save text to file

### `preprocessing.py`
Cleans and preprocesses text for better TTS output.

**Functions:**
- `preprocess_text(text)`: Full text preprocessing
- `clean_text(text)`: Light text cleaning
- `tokenize_sentences(text)`: Split text into sentences

### `customization.py`
Manages UI styling and user settings persistence.

**Functions:**
- `load_settings()`: Load saved preferences
- `save_settings(settings)`: Save user preferences
- `apply_custom_style(text_widget, settings)`: Apply styling
- `get_default_settings()`: Get default configuration

### `tts_module.py`
Text-to-speech engine wrapper around pyttsx3.

**Key Class:**
- `TextToSpeech`: Main TTS engine class

**Methods:**
- `speak(text)`: Convert text to speech
- `pause()`: Pause playback
- `stop()`: Stop playback
- `set_rate(rate)`: Set speaking speed
- `set_volume(volume)`: Set volume level

## ⚙️ Configuration

### Default Settings
Settings are stored in `tts_settings.json`:

```json
{
    "font_family": "Arial",
    "font_size": 14,
    "word_spacing": 1,
    "letter_spacing": 0,
    "bg_color": "#ffffff",
    "fg_color": "#000000",
    "highlight_color": "#ffe599",
    "highlight_mode": "word"
}
```

### Customizing Defaults
Edit `customization.py` in the `get_default_settings()` function to change default values.

## 🐛 Troubleshooting

### Issue: "No module named 'pyttsx3'"
**Solution**: Install pyttsx3
```bash
pip install pyttsx3
```

### Issue: GUI window won't open
**Solution**: Ensure tkinter is installed. On Linux:
```bash
sudo apt-get install python3-tk
```

### Issue: No sound output
**Solution**: Check your system audio settings and ensure speakers are connected and unmuted.

### Issue: Text not highlighting
**Solution**: Ensure the "Highlight Mode" is set correctly (Word or Line) and click Play to start reading.

## 🎨 Customization Tips

### For Dyslexic Users
- **Recommended Font**: OpenDyslexic (highly specialized for dyslexia)
- **Recommended Spacing**: Word spacing 2-3, Letter spacing 1-2
- **Recommended Speed**: 150-170 WPM (slower for better comprehension)
- **Highlight Mode**: Word-level highlighting for better tracking

### Optimal Colors
- Light background (white, cream)
- High contrast text (black, dark blue)
- Warm highlight colors (yellow, orange)

## 📦 Dependencies

- **pyttsx3**: Text-to-speech engine
- **nltk**: Natural Language Toolkit for text processing
- **numpy**: Numerical computing
- **scipy**: Scientific computing
- **tkinter**: GUI framework (built-in with Python)

## 📝 Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Paste Text | N/A (use button) |
| Save Settings | Click "Save Prefs" button |
| Play/Pause | Use GUI buttons |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Credits

**Development Team**: Team DyslexiaAid

Special thanks to:
- The OpenDyslexic font creators for accessibility support
- pyttsx3 developers for the text-to-speech engine
- NLTK team for natural language processing tools

## 📞 Support

For issues, questions, or suggestions:
1. Check the Troubleshooting section above
2. Review the application's "About" section (click "About" button)
3. Open an issue on the project repository

## 🎯 Future Enhancements

- [ ] Multi-language support
- [ ] Voice selection UI
- [ ] Recording output to audio file
- [ ] PDF file support
- [ ] Dark mode theme
- [ ] Advanced text analysis
- [ ] Custom vocabulary dictionary

---

**Designed with ❤️ for accessibility and inclusivity**
