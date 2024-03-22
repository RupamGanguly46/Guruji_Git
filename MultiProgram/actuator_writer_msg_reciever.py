import win32pipe
import win32file
import struct

# Path to the named pipe
pipe_path = r'\\.\pipe\sensor_actuator_pipe'

# Connect to the named pipe
pipe = win32file.CreateFile(
    pipe_path,
    win32file.GENERIC_READ,
    0, None,
    win32file.OPEN_EXISTING,
    0, None
)

while True:
    # Read a message from the named pipe
    message = win32file.ReadFile(pipe, 4096)[1]
    if not message:
        break

    # Unpack the message into sensor data (temperature and humidity)
    temperature, humidity = struct.unpack('ff', message)

    # Perform actions based on the received data
    if temperature > 30.0:
        print("Temperature is too high, cooling system activated")
    if humidity > 60.0:
        print("Humidity is too high, ventilation system activated")
