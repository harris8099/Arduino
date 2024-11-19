import serial
import time

# Replace 'COM3' with the Bluetooth COM port on your laptop
# On macOS or Linux, this could be '/dev/tty.HC-05-DevB' or similar
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

# Send data to HC-05
data_to_send = "Hello, Arduino!"
bluetooth.write(data_to_send.encode())  # Send data as bytes
print(f"Sent: {data_to_send}")

# Optional: Read response from Arduino if it sends data back
time.sleep(1)  # Give Arduino time to respond
if bluetooth.in_waiting > 0:
    response = bluetooth.read(bluetooth.in_waiting).decode()
    print(f"Received: {response}")

# Close connection
bluetooth.close()
print("Disconnected")
