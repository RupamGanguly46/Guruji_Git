import subprocess as subp
import sys

file_path1 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\sensor_reader_msg_sender.py"
file_path2 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\actuator_writer_msg_reciever.py"

processes = {
    'a': subp.Popen(["python", file_path1]),
    'b': subp.Popen(["python", file_path2])
}

def terminate_processes():
    for process in processes.values():
        process.terminate()
    sys.exit()

print("Press 'a' to terminate process 1, 'b' to terminate process 2, or 'esc' to exit.")

while True:
    key = input("Enter key: ")
    if key == 'a' and 'a' in processes:
        processes['a'].terminate()
    elif key == 'b' and 'b' in processes:
        processes['b'].terminate()
    elif key == 'esc':
        terminate_processes()
