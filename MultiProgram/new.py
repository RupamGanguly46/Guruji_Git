import subprocess as subp
import sys
import psutil  # You may need to install the psutil package

file_path1 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\sensor_reader_msg_sender.py"
file_path2 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\actuator_writer_msg_reciever.py"

processes = {
    'a': subp.Popen(["start", "cmd", "/c", "python", file_path1], shell=True),
    'b': subp.Popen(["start", "cmd", "/c", "python", file_path2], shell=True)
}

def get_cmd_pid(parent_pid):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'cmd.exe' and proc.ppid() == parent_pid:
            return proc.pid
    return None

def terminate_processes():
    for key, process in processes.items():
        cmd_pid = get_cmd_pid(process.pid)
        print(cmd_pid)
        if cmd_pid:
            subp.Popen(["taskkill", "/F", "/T", "/PID", str(cmd_pid)], shell=True)
        process.terminate()
    sys.exit()

print("Press 'a' to terminate process 1, 'b' to terminate process 2, or 'esc' to exit.")

while True:
    key = input("Enter key: ")
    if key == 'a' and 'a' in processes:
        cmd_pid = get_cmd_pid(processes['a'].pid)
        print(cmd_pid)
        if cmd_pid:
            subp.Popen(["taskkill", "/F", "/T", "/PID", str(cmd_pid)], shell=True)
        processes['a'].terminate()
    elif key == 'b' and 'b' in processes:
        cmd_pid = get_cmd_pid(processes['b'].pid)
        print(cmd_pid)
        if cmd_pid:
            subp.Popen(["taskkill", "/F", "/T", "/PID", str(cmd_pid)], shell=True)
        processes['b'].terminate()
    elif key == 'esc':
        terminate_processes()
