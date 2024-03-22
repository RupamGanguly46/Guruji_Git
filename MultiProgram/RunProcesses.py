import subprocess as subp
import keyboard
import sys

file_path1 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\sensor_reader_msg_sender.py"
file_path2 = r"C:\Users\HP\Desktop\Computer Programming\MultiProgram\actuator_writer_msg_reciever.py"

processes = {
    'a': subp.Popen(["start", "cmd", "/c", "python", file_path1], shell=True),
    'b': subp.Popen(["start", "cmd", "/c", "python", file_path2], shell=True)
}

def get_cmd_pid(process_name):
    cmd = subp.Popen(["tasklist", "/FI", f"IMAGENAME eq {process_name}", "/FO", "CSV", "/NH"], stdout=subp.PIPE, stderr=subp.PIPE, stdin=subp.PIPE)
    output, _ = cmd.communicate()
    for line in output.decode().split('\n'):
        if line.strip():
            parts = line.split(',')
            pid = parts[1].strip().strip('"')  # Strip both leading and trailing quotes
            return int(pid)
    return None




def on_key_pressed(event):
    if event.name in processes.keys():
        process = processes[event.name]
        process.terminate()
        cmd_pid = get_cmd_pid("cmd.exe")
        if cmd_pid:
            subp.Popen(["taskkill", "/F", "/T", "/PID", str(cmd_pid)], shell=True)
    elif event.name == 'esc':
        for process in processes.values():
            process.terminate()
        sys.exit()

keyboard.on_press(on_key_pressed)

# Continuously check for 'esc' key press to exit
while True:
    if keyboard.is_pressed('esc'):
        for process in processes.values():
            process.terminate()
        sys.exit()
