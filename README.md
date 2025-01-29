# nanoKEY2 MIDI to F5 Key Mapper

This Python script listens for MIDI input from a Korg nanoKEY2 and maps specific MIDI notes to keyboard actions. In this case, pressing a specific key on the nanoKEY2 will trigger an F5 keypress on the computer.

## Features

- Detects nanoKEY2 MIDI input
- Maps **C4 (Note 72)** to the **F5 key**
- Pressing **C2 (Note 48)** stops the listener

## Requirements
Before using this project, ensure that you have the **KORG nanoKEY2/KORG USB-MIDI Driver** installed on your Windows machine.

1. **Download the KORG USB-MIDI Driver**:
   - Go to the official [nanoKEY2/KORG USB-MIDI Driver download page](https://www.korg.com/us/support/download/driver/0/156/3541/) (or the relevant page if the link changes over time).
   - Look for **Version 1.15 r56e** or the latest version compatible with the nanoKEY2 device.

2. **Install the Driver**:
   - Run the downloaded installer (`KORG_USB_MIDI_Driver_v1.15_r56e.exe`).
   - Follow the on-screen instructions to complete the installation.

3. **Connect Your nanoKEY2**:
   - Plug in the **KORG nanoKEY2** to your computer using the included USB cable.
   - The system should recognize the device and initialize it as a MIDI controller.

## Option1: Running the source code (using a python environment)

- Python 3.x
- `mido` library for MIDI input
- `pynput` library for keyboard emulation
- `rtmidi` backend for `mido` (on Windows)

```
pip install mido pynput python-rtmidi
```

### Usage

Run the script with:

```sh
python midi_listener.py
```

If the nanoKEY2 is connected, it will listen for MIDI input and trigger key events.

### Option 2: Download the Latest Binary from the Releases

You can also download the latest precompiled binary from the **releases page** of this repository.

1. **Download the Binary**:
   - Navigate to the [Releases section](https://github.com/UG-Team-Data-Science/nanokey2-midi-mapper/releases) of this GitHub repository.
   - Download the latest release binary suitable for your platform (e.g., `nanokey2-midi-mapper-v0.0.1-alpha.exe` for Windows).

2. **Run the Binary**:
   - After downloading, locate the binary file (e.g., `nanokey2-midi-mapper-v0.0.1-alpha.exe`).
   - Double-click the `.exe` file to run the application.

3. **Usage**:
   - Once the application is running, it will automatically detect the connected **KORG nanoKEY2** and allow you to start using the MIDI functions.
   - If any additional configuration is required, follow the on-screen instructions or refer to the documentation provided in the release.


## Creating a Windows Executable

To generate a standalone `.exe` file:

```sh
pip install pyinstaller
pyinstaller --hidden-import=mido.backends.rtmidi midi_listener.py
```

This will create a `dist/midi_listener.exe` that can run without Python.


This project is released under the MIT License.

