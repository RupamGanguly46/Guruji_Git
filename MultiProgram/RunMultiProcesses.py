import subprocess as subp

file_path1 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\sensor_reader_msg_sender.py"
file_path2 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\actuator_writer_msg_reciever.py"

processes = {
    'a': subp.Popen(["start", "cmd", "/c", "python", file_path1], shell=True),
    'b': subp.Popen(["start", "cmd", "/c", "python", file_path2], shell=True)
}
# process1 = subp.Popen(["start", "cmd", "/k", "python", file_path1], shell=True)
# process2 = subp.Popen(["start", "cmd", "/k", "python", file_path2], shell=True)

import keyboard
import sys
import os

def on_key_pressed(event):
    if event.name in processes.keys():
        print(event.name, "is pressed")
        processes[event.name].terminate()
    elif event.name == 'esc':
        print(event.name, "is pressed")
        for process in processes.values():
            process.terminate()
        sys.exit()

keyboard.on_press(on_key_pressed)
keyboard.wait('esc')

# while True:
#     event = keyboard.read_event()
#     if event.name in processes.keys():
#         processes[event.name].terminate()
#     elif event.name == 'esc':
#         for process in processes.values():
#             process.terminate()
#         sys.exit()



# Keyboard Tester

# def on_key_pressed(event):
#     print("Key pressed:", event.name)

# keyboard.on_press(on_key_pressed)
# keyboard.wait('esc')

