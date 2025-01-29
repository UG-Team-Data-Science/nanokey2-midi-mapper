import mido
from pynput.keyboard import Controller, Key

# Initialize keyboard controller
keyboard = Controller()

# Find the nanoKEY2 MIDI input port
midi_port_name = None
for name in mido.get_input_names():
    print(name)
    if "nanoKEY2" in name:  # Adjust if needed
        midi_port_name = name
        break

if midi_port_name is None:
    print("nanoKEY2 not found!")
    exit(1)

# Open the MIDI input port
with mido.open_input(midi_port_name) as port:
    print(f"Listening for MIDI input on {midi_port_name}...")

    for msg in port:
        if msg.type == 'note_on':  # Detect key press
            print(f"Key pressed: {msg.note}")

            # Assign a specific key (change note number as needed)
            if msg.note == 72:  # Middle C (C4)
                print("Triggering F5...")
                keyboard.press(Key.f5)
                keyboard.release(Key.f5)
            if msg.note == 48:
                print("MIDI listener stopped")
                break