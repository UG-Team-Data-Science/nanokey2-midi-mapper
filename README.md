# nanoKEY2 MIDI to F5 Key Mapper

This Python script listens for MIDI input from a Korg nanoKEY2 and maps specific MIDI notes to keyboard actions. Additionally, if the nanoKEY2 is not connected, the application uses the `right arrow` key to trigger an `F5` key press, allowing for refreshing browser windows (e.g., Firefox). The app can be stopped by pressing the Q key or by playing a specific MIDI note.

## Features

- Detects nanoKEY2 MIDI input:  Automatically finds and listens to the nanoKEY2 MIDI input port.
- Maps **C4 (Note 72)** to the **F5 key**
- If the nanoKEY2 is not connected, pressing the `right arrow` key on the keyboard triggers `F5`.
- Pressing **C2 (Note 48)** stops the listener.
- Alternatively, pressing the `Q` key on the computer keyboard stops the application.

![image](https://github.com/user-attachments/assets/fc66778d-68a1-4dc0-b9f4-fb84fa55ec37)


## Requirements
Before using this project, ensure that you have the **nanoKEY2/KORG USB-MIDI Driver** installed on your Windows machine.

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
Requirements: 
- Python 3.x
- `mido` library for MIDI input
- `pynput` library for keyboard emulation
- `rtmidi` backend for `mido` (on Windows)

### Step 1: Create a Virtual Environment  
Open **PowerShell** or **CMD** and navigate to the project directory. Then, create a virtual environment using the following command:  

```powershell
python -m venv .venv
```

### Step 2: Activate the Virtual Environment
- PowerShell:
```powershell
.venv\Scripts\Activate
```
- CMD:
```cmd
.venv\Scripts\activate
```
### Step 3: Install Required Packages
```
pip install mido pynput python-rtmidi
```

### Usage

Run the script with:

```sh
python nanokey2-midi-mapper.py
```

If the nanoKEY2 is connected, it will listen for MIDI input and trigger key events.

## Option 2: Download the Latest Binary from the Releases

You can also download the latest precompiled binary from the **releases page** of this repository.

1. **Download the Binary**:
   - Navigate to the [Releases section](https://github.com/UG-Team-Data-Science/nanokey2-midi-mapper/releases) of this GitHub repository.
   - Download the latest release binary suitable for your platform (e.g., `nanokey2-midi-mapper-vx.x.x-alpha.exe` for Windows).

2. **Run the Binary**:
   - After downloading, locate the binary file (e.g., `nanokey2-midi-mapper-vx.x.x-alpha.exe`).
   - Double-click the `.exe` file to run the application.

3. **Usage**:
   - Once the application is running, it will automatically detect the connected **KORG nanoKEY2** and allow you to start using the MIDI functions.
   - If any additional configuration is required, follow the on-screen instructions or refer to the documentation provided in the release.


## Creating a Windows Executable

To generate a standalone `.exe` file:

```sh
pip install pyinstaller
pyinstaller --onefile --hidden-import=mido.backends.rtmidi nanokey2-midi-mapper.py
```

This will create a `dist/nanokey2-midi-mapper.exe` that can run without Python.


This project is released under the MIT License.

