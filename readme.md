# Text Editor with Text-to-Speech Feature

This is a simple text editor application with an added Text-to-Speech (TTS) feature. The application is built using Python and the Tkinter library for the graphical user interface. The TTS functionality is implemented using the gTTS (Google Text-to-Speech) library.

## Features

- Basic text editing functionalities (Open, Save, Edit)
- Text-to-Speech functionality to read aloud the text content
- Random motivation sentence at the top of the editor just for fun and good mood

## How to Use

1. **Open the Text Editor:**
   - Run the `text_editor.py` script.
   - The application window will open with a text editor interface.

2. **Basic Text Editing:**
   - Use the Open and Save buttons or keyboard shortcuts (Ctrl + O, Ctrl + S) to manage text files.
   - Edit the text content in the main editor area.

3. **Text-to-Speech:**
   - Click the "Read Aloud" button or use the Ctrl + R shortcut to have the current text content read aloud.
   - Change the speed of the speach, the default sets to normal speed.

## Shortcuts

- **Ctrl + O:** Open a text file
- **Ctrl + S:** Save the text content to a file
- **Ctrl + R:** Read aloud the text content using Text-to-Speech

## Requirements
- See requirements.txt file
- I used Python 3.10
- Tkinter (should be included with Python)
- gTTS library: Install using `pip install gtts`

## How to Run

1. Install the required dependencies:
2. Simply run text_editor.py


## Extra

#### Creating a Desktop Shortcut (For Linux)

If you're using Linux, you can create a desktop shortcut for easy access to the Text Editor application. Follow these steps:

1. Navigate to the Desktop Directory:**
   Open your terminal and navigate to your desktop directory using the `cd` command:

   ```bash
   cd ~/Desktop
   
2. Create a new desktop shortcut file using your preferred text editor. For example, you can use nano:
   ```bash
   nano text_editor.desktop
   
3. Inside the text_editor.desktop file, paste the following content:
   ```bash
   [Desktop Entry]
    Name=Text Editor
    Exec=python3 /path/to/your/project/text_editor.py
    Type=Application
    Icon=/path/to/your/project/icon.png
Replace /path/to/your/project/ with the actual path to your Text Editor project directory. Also, provide the correct path to the icon file (if you have one).
4. Make the desktop shortcut file executable using the following command:
   ```bash
   chmod +x text_editor.desktop
