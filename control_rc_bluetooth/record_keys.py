from pynput import keyboard

def on_press(key):
    try:
        # For regular characters, print the character
        # print(f"Key pressed: {key.char}")
        key_pressed = key.char
        print(key_pressed.lower())

    except AttributeError:
        # For special keys (e.g., ctrl, alt, space)
        # print(f"Special Key pressed: {key}")
        pass

def on_release(key):
    # Stop listener when escape key is pressed
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
