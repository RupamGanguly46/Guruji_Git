# ipc (inter-process communication)
import win32pipe
import win32file
import struct
import time

pipe_path = r'\\.\pipe\sensor_actuator_pipe'

# Create a named pipe
pipe = win32pipe.CreateNamedPipe(
    pipe_path,
    win32pipe.PIPE_ACCESS_DUPLEX,  # acess to both read and write
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT, # pipe type is message, and reading or writing will wait till a message exists
    1 , 65536, 65536, # max_instances of pipe, out_buffer_size, in_buffer_size
    0, # default timeout
    None  # security attributes
)

# Connect to the named pipe
win32pipe.ConnectNamedPipe(pipe, None)

while True:
    # Simulate sensor data (e.g., temperature and humidity)
    temperature = 25.0
    humidity = 50.0

    # Pack the sensor data into a binary message
    message = struct.pack('ff', temperature, humidity)

    # Write the message to the named pipe
    win32file.WriteFile(pipe, message)

    # Wait for some time before sending the next message
    time.sleep(1)