

---

# Smart Curtain Voice-Controlled System

This project implements a smart curtain that responds to voice commands in multiple languages (English, French, and Arabic) and displays memorable images behind the curtain. It is designed using a **Raspberry Pi 3 B+** that communicates with an **ESP32** to control a **Nema17 motor**, which opens or closes the curtain. This project was created to showcase memories from ENSI (École Nationale des Sciences de l'Informatique).

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Raspberry Pi Configuration](#raspberry-pi-configuration)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Credits](#credits)

## Project Overview

The smart curtain system uses **Kaldi** for speech recognition to understand voice commands in English, French, and Arabic. When commands are given, the Raspberry Pi sends instructions to the ESP32, which then activates the Nema17 motor to open or close the curtain.

## Features

- **Voice Recognition**: Supports commands in English, French, and Arabic.
- **Automatic Language Detection**: Changes command language based on user input.
- **Motor Control**: Controls a Nema17 motor to open or close the curtain.
- **ESP32 Communication**: Sends commands from Raspberry Pi to ESP32 over WiFi.
- **Image Display**: Displays stored images associated with ENSI memories.

## Hardware Requirements

- **Raspberry Pi 3 B+** (for voice processing and control)
- **ESP32** (for motor control)
- **Nema17 Motor** (to open and close the curtain)
- **Voice Recognition Microphone**
- **Power Supply**
- **Curtain with track or rail**

## Software Requirements

- **Python 3.7+**
- **Kaldi Speech Recognition Model**
- **Googletrans** (for translation)
- **PyAudio** (for audio processing)
- **Pyttsx3** (for text-to-speech)
- **Vosk API** (for offline speech-to-text)
- **Pygame** (for audio playback)
- **ESP32 Firmware** (custom, for WiFi communication)

## Raspberry Pi Configuration

### 1. Setting Up SSH

1. **Enable SSH** on the Raspberry Pi to allow remote access:
   - Open Raspberry Pi Configuration from the main menu.
   - Go to the **Interfaces** tab.
   - Enable **SSH** and click **OK**.

2. **Find the Raspberry Pi's IP address**:
   - Run `hostname -I` in the terminal or find it on your network router.

3. **Connect to Raspberry Pi via SSH**:
   - Open a terminal on your computer and type:
     ```bash
     ssh pi@<Raspberry_Pi_IP_Address>
     ```
   - Replace `<Raspberry_Pi_IP_Address>` with the actual IP address of your Raspberry Pi.
   - Enter the default password `raspberry` (or your custom password if you’ve changed it).

### 2. Setting Up VNC for Remote Desktop Access

1. **Enable VNC**:
   - Open Raspberry Pi Configuration from the main menu.
   - Go to the **Interfaces** tab.
   - Enable **VNC** and click **OK**.

2. **Download VNC Viewer** on your computer:
   - Install [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) on your computer.

3. **Connect to Raspberry Pi via VNC Viewer**:
   - Open VNC Viewer and enter `<Raspberry_Pi_IP_Address>` in the address bar.
   - Connect using the same credentials as SSH (username `pi` and your password).

### 3. Autostart Program on Boot (Optional)

To run the smart curtain program automatically on startup:

1. Open the autostart file:
   ```bash
   sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
   ```

2. Add the following line to start the program on boot:
   ```bash
   @lxterminal -e python3 /home/pi/smart_curtain_project/vosk_chat.py
   ```

3. Save and close the file with `Ctrl+X`, `Y`, then `Enter`.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd smart_curtain_project
   ```

2. Install required Python packages:
   ```bash
   pip install pyttsx3 pyaudio googletrans==4.0.0-rc1 pygame vosk
   ```

3. Set up the **Kaldi** speech recognition models for English and French. Download the Vosk models and place them in the project directory. Update paths as needed in the code:
   ```python
   english_model = r"path_to_english_model"
   french_model = r"path_to_french_model"
   ```

4. Load the ESP32 with the firmware that receives TCP commands to control the Nema17 motor.

5. Connect the ESP32 to the Raspberry Pi’s network and update the ESP32's IP address in `send_data.py`:
   ```python
   ESP32_IP = "192.168.xxx.xxx"  # Replace with your ESP32's IP address
   ESP32_PORT = 12345            # Replace with the correct port
   ```

## Usage

1. Start the application on the Raspberry Pi:
   ```bash
   python vosk_chat.py
   ```

2. Give commands:
   - **"Open"**: Opens the curtain to display ENSI memories.
   - **"Close"**: Closes the curtain to hide the memories.
   - Language commands: Say "English," "Français," or "Arabic" to switch languages.

3. To stop the program, use a voice command like "Goodbye."

## Project Structure

- `vosk_chat.py`: Main program file handling voice recognition and command processing.
- `tools.py`: Utility functions for speech synthesis, translation, and music playback.
- `send_data.py`: Handles TCP communication with the ESP32.
- `models/`: Directory containing the Vosk speech models.
- `sounds/`: Folder for music and sound effects.

## Credits

This project was developed by Ayman Ben Amor as a showcase of memories at ENSI, integrating embedded systems, IoT, and speech recognition.

## Demo Video

Watch the [demo video](https://drive.google.com/file/d/11hWDxoL5hE4GUlSv5FmhiAty7iTtSWFM/view?usp=drive_link) of the smart curtain system in action.

[![Watch the video](https://img.icons8.com/color/48/000000/google-drive--v1.png)](https://drive.google.com/file/d/11hWDxoL5hE4GUlSv5FmhiAty7iTtSWFM/view?usp=drive_link)

---
