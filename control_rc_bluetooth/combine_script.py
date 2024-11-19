from pynput import keyboard
import serial
import time

############  Keys To send  ######################################################################################

Keys = ['w','a','s','d','+','-']

############  Keys To send  ######################################################################################


############  Bluetooth  ######################################################################################

bluetooth_port = 'COM10'
baud_rate = 9600  # Must match the HC-05 module's baud rate

# Establish serial connection
try:
    bluetooth = serial.Serial(bluetooth_port, baud_rate)
    print(f"Connected to HC-05 on {bluetooth_port}")
except serial.SerialException as e:
    print(f"Could not connect to {bluetooth_port}: {e}")
    exit()

time.sleep(2)  # Allow time for connection setup

############  Bluetooth  ######################################################################################


############  Keyboard  ######################################################################################

def on_press(key):
    try:
        # For regular characters, print the character
        # print(f"Key pressed: {key.char}")
        key_pressed = key.char.lower()
        # print(key_pressed)
        if key_pressed in Keys:
            # Send data to HC-05
            data_to_send = key_pressed
            bluetooth.write(data_to_send.encode())  # Send data as bytes
            print(f"Sent: {data_to_send}")

    except AttributeError:
        # For special keys (e.g., ctrl, alt, space)
        # print(f"Special Key pressed: {key}")
        pass

def on_release(key):
    # Stop listener when escape key is pressed
    if key == keyboard.Key.esc:
        print("Exiting...")

        # Close connection
        bluetooth.close()
        print("Disconnected")
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


############  Keyboard  ######################################################################################
