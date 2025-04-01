import mido
import time
from pynput import keyboard
from pynput.keyboard import Controller, Key

# Initialize keyboard controller
kb_controller = Controller()
stop_app = False  # Flag to control stopping the app

# Find the nanoKEY2 MIDI input port
midi_port_name = None
for name in mido.get_input_names():
    print(name)
    if "nanoKEY2" in name:  # Adjust if needed
        midi_port_name = name
        break

# Function to stop the application with a message and delay
def stop_application():
    global stop_app
    print("Stopping the application...")
    time.sleep(3)  # Sleep for a few seconds before stopping
    stop_app = True

# Function to trigger F5 key in a way compatible with most browsers
def trigger_refresh():
    print("Triggering F5...")
    kb_controller.press(Key.f5)
    kb_controller.release(Key.f5)

# Keyboard event listener
def on_press(key):
    try:
        # Print the key that was pressed
        print(f"Key pressed: {key.char}")
    except AttributeError:
        # Special keys (e.g., arrows, function keys) don't have 'char' attribute
        print(f"Special key pressed: {key}")
    if key == Key.right:
        print("Right arrow pressed. Triggering F5...")
        trigger_refresh()
    elif key == keyboard.KeyCode.from_char('q'):
        print("Q key pressed.")
        stop_application()

# If the MIDI port is not found, use right arrow key and q to stop
if midi_port_name is None:
    print("nanoKEY2 not found! Using right arrow key to trigger F5 and Q to stop.")

    # Start listening to keyboard events
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Keep the application running and checking for the stop flag
    while not stop_app:
        time.sleep(0.1)

    listener.stop()

else:
    # Open the MIDI input port
    with mido.open_input(midi_port_name) as port:
        print(f"Listening for MIDI input on {midi_port_name}...")

        # Also listen to keyboard inputs for the 'q' key
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        for msg in port:
            if msg.type == 'note_on':  # Detect key press
                print(f"Nano Key pressed: {msg.note}")

                # Assign a specific key (change note number as needed)
                if msg.note == 72:  # Middle C (C4)
                    print("Triggering right arrow...")
                    kb_controller.press(Key.right)
                    kb_controller.release(Key.right)
                elif msg.note == 48:
                    print("MIDI note 48 detected.")
                    stop_application()

            # Check if the app should stop
            if stop_app:
                break

        listener.stop()

