# nanoKEY2 MIDI to F5 Key Mapper

This Python script listens for MIDI input from a Korg nanoKEY2 and maps specific MIDI notes to keyboard actions. In this case, pressing a specific key on the nanoKEY2 will trigger an F5 keypress on the computer.

## Features

- Detects nanoKEY2 MIDI input
- Maps **C4 (Note 72)** to the **F5 key**
- Pressing **C2 (Note 48)** stops the listener

## Requirements

- Python 3.x
- `mido` library for MIDI input
- `pynput` library for keyboard emulation
- `rtmidi` backend for `mido` (on Windows)

## Installation

1. Install Python if not already installed: [Download Python](https://www.python.org/downloads/)
2. Install required dependencies:
   ```sh
   pip install mido pynput python-rtmidi
   ```

## Usage

Run the script with:

```sh
python midi_listener.py
```

If the nanoKEY2 is connected, it will listen for MIDI input and trigger key events.

## Creating a Windows Executable

To generate a standalone `.exe` file:

```sh
pip install pyinstaller
pyinstaller --onefile midi_listener.py
```

This will create a `dist/midi_listener.exe` that can run without Python.

## Publishing on GitHub

1. Create a new GitHub repository.
2. Initialize Git and push the project:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/nanokey2-midi-mapper.git
   git push -u origin main
   ```


This project is released under the MIT License.

